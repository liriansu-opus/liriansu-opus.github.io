---
title: "Software Engineering Practice: Graceful Release"
date: 2019-12-09T23:39:28+08:00
zhUrl: /software-engineering-gracefully-upgrade
aliases:
  - /software-engineering-gracefully-upgrade-en
---

The Software Engineering Practice series of articles
focuses on how software is collaboratively developed in real engineering projects.
This article mainly introduces how to release versions without interruption.

<!--more-->

## outline

This article includes:

- why
- how: graceful release roughly divides into two parts.
  - service: just do switching management well at the service layer.
  - database: standard operations at the database layer.
- example: let's give an actual chestnut.
- conclusion

## why: why do graceful releases?

[ldsink][ldsink] once said back when he was at Baixing.com,
the practice they consistently kept was "always be ready to release,"
which not only keeps feature delivery agile,
but also prepares for various changes.

Back then our monolithic service had to stop for a few seconds every release,
those few seconds meant a pile of 5XX network errors triggered by users.
Not to mention the dev/test environments that release more frequently,
where our frontend brothers often exclaimed:
"Huh? Server 502'd! Huh, I refresh and it's fine again..."

After I seriously studied this, I found
that graceful release is actually a very universal topic;
any service involving network traffic distribution and request handling logic has this functionality.

The English term for graceful release is `gracefully upgrade/reload/restart`.
Common tools have thorough support for the graceful release process,
just search by tool name, like `nginx gracefully upgrade` or `k8s gracefully upgrade`.

Why do graceful release?
The core purpose is just one:
prevent service interruption caused by releases.

## how: how to do graceful release?

In real engineering,
most web services essentially accept requests from outside,
query and process data from databases, and return.
This piece will follow this logic,
introducing graceful release by service/database in turn.

### service: graceful release at the service layer

Our team's backend uses python/django,
detailed introduction can be found in the previous article 《Software Engineering Practice: django/python》.
Our current network link is
_(cloud load balancer) -> (k8s-ingress-controller) -> k8s-pod(nginx+uwsgi)_

The cloud load balancer and k8s-ingress-controller (currently kong) don't change frequently,
so I won't elaborate.
What changes every release is the business service, which in the link above is k8s-pod(nginx/uwsgi).

Whether it's k8s/docker/systemctl/supervisord/pm2,
their common logic is system Signals.

| Signal  | x86 |
|---------|-----|
| SIGHUP  |  1  |
| SIGINT  |  2  |
| SIGQUIT |  3  |
| SIGKILL |  9  |
| SIGTERM |  15 |
> part of unix signal numbers

Taking k8s as an example, when the old pod is being terminated, k8s does the following:

1. Sends `SIGTERM`, then waits up to `terminationGracePeriodSeconds(default=30)` seconds
2. If the service stops during the wait, then proceeds with other termination operations
3. If the service doesn't stop during the wait, then sends a `SIGKILL` signal

In general, standard framework implementations support `SIGTERM` and `SIGKILL` semantics,
but specific extra custom logic you need to implement and control yourself.

To ensure no request interruption at the service layer,
signals must be handled correctly.

### database: graceful release at the database layer

Database-layer changes during release
mainly fall into data changes and schema changes.
**The core handling method is dual-write.**

Let me first talk about dual-write for data changes.

For example, we used to have a field A,
storing a boolean true/false,
later the meaning got richer and had to be changed to enum values 0/1/2/3.
Then the whole flow has to be:

1. Add an enum field B with default empty.
2. First release introduces dual-write: wherever the code logic writes field A, add the same logic to write field B.
3. Wash the data: convert all field A values into field B using the same logic.
4. Second release removes the dual-write: wherever the code reads field A, replace entirely with field B.
5. After confirming everything is normal, drop field A.

Steps 2~4 handle compatibility via dual-write,
the duration will vary greatly by situation:
maybe dual-write finishes in 10 minutes,
or it could last several days to leave enough time to wash a lot of data.

Now let's look at dual-write for schema changes,
the core logic is the same 1/2/3/4/5 five-step routine as above.

- Adding a field: very simple, add the field then release.
- Removing a field: also simple, release to remove related logic then drop.
- Modifying a field: if it's an incompatible change, handle it as add-new-field + dual-write + drop-old-field.

To ensure no request interruption at the database layer,
use dual-write to guarantee compatibility.

## example: a real chestnut

Our django service runs as nginx+uwsgi,
nginx/uwsgi themselves have good support for SIGTERM/SIGKILL semantics.
But within the same pod, race conditions often occur,
nginx sometimes terminates earlier than uwsgi,
ultimately causing request interruption issues.

Folks online have run into similar problems,
the solution is also simple to the point of being funny:
[add some sleep][sleep-in-k8s]

```
container:
  name: nginx
  lifecycle:
    preStop:
      exec:
        command: ["sh", "-c", "sleep 10 && kill -s HUP 1"]
```

Besides the regular service layer and database layer,
we also use celery as async workers.
celery's support for graceful release isn't particularly great,
so [as mentioned in the community][signal-in-celery],
we handle the signal at the task level ourselves.

## conclusion

Overall, the core ideas for engineering implementations of graceful release (zero-interruption release):

- Service layer: handle system signals properly.
- Database: use dual-write to maintain compatibility.
- Other: ensure every point in the link is interruption-free to achieve true graceful release.

Through this series of operations,
we can easily make users (including our frontend brothers DDOS-ing the test environment) unable to perceive that we're releasing,
ultimately achieving that state of "always ready to release."

Of course,
"always ready to release" only means technically feasible,
it doesn't mean in actual work we really release every moment :)

After all, software engineering involves not just software tech but also the engineering of people.

(End)


[ldsink]: https://ldsink.com/
[sleep-in-k8s]: https://github.com/kubernetes/ingress-nginx/issues/322#issuecomment-298016539
[signal-in-celery]: https://github.com/celery/celery/issues/2700
