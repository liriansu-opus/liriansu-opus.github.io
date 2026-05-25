---
title: "Five Years After Graduation: Technology"
date: 2020-07-12T23:45:58+08:00
zhUrl: /adult-life-code
aliases:
  - /adult-life-code-en
---

After touching the whole Web tech stack in 2016, I
decided to keep climbing this path,
until I find my technical ceiling.
Back then I wrote [《Backend Engineer Skill Tree》][tree].

<!--more-->

Now looking back,
I didn't follow the leaf-node order step by step.
Beyond systematically studying and understanding tech knowledge,
more often I was struggling in the bloody mud of "launching tomorrow" and "production is down."

This piece, from a different perspective,
will record my technical insights over these years.
Since this is more Web-focused,
this article basically uses Zaihui's actual development as the example.


## Project, Language, and Framework

In 2016, the company's business could be fully solved in a single big main site.
This single project included not just all backend code,
but all frontend code (though later frontend was split out).

Back then we used Python 2.7 + Django 1.8,
but since Python 2 was at the end of life,
we later [found a weekend to upgrade to Python 3.5][py3].
By the way, the reason we didn't upgrade to Python 3.6 was that Ubuntu 16's default was Python 3.5.

Python is a language very easy to pick up,
I hadn't seriously used it before joining Zaihui (didn't even know what virtualenv was, only knew print),
but I could start participating in business development very quickly.
Throughout the main site's dev cycle,
the framework didn't have major changes,
basically how the predecessors wrote it, the successors wrote it.

Things I was interested in language-wise back then mainly included:

- magic methods and metaprogramming: so I implemented a logic to generate APIs from config
- performance, concurrency, and processing capacity: so we often drew various network architecture diagrams on the small blackboard
- comparisons between different frameworks: so internally in later projects we tried flask/tornado and other frameworks
- topics about the language itself: so we'd discuss [Master Yin @wangyin's blog][wangyin] every day internally (x

Later business lines gradually multiplied,
and I had the chance to build a project from scratch.
Since I was starting from zero, I secretly thought:
"In the past I knew the 'what' of many things but not the 'why',
this time I want to fully understand every aspect of the project."
So that month I spent all my free time reading various docs...

Didn't know til I read it, but reading shocked me.
I discovered that many habitual usages I'd defaulted to
actually had better practices:

- **Light usage**:
  In previous projects we'd pair-use djangorestframework,
  but we always hand-wrote various serializer classes,
  not using the framework's built-in django model support.
  And we ourselves implemented a schema validation system,
  not using djangorestframework,
  nor libraries like marshmellow.
  (This caused supporting swagger later to be very difficult.)

- **Lacking checks**:
  The Python community has many check tools,
  but we only used the most basic flake8 to validate PEP8 style.
  In collaborative programming,
  because everyone's PyCharm config was different,
  we resolved countless import conflicts.
  (Not to mention conflicts about trailing commas in arrays.)

- **Outdated versions**:
  Many third-party libraries we used kept updating,
  but we kept using old versions (not to mention the language itself, we got f-string very late).

These problems I solved one by one in later project development.
Light usage is easy to address — find a brother to study correct usage and optimize.
(Sometimes this optimization touches hundreds of files, so we need a brother fluent in vim.)
Lacking checks is also easy — flake8/isort/pytest/pylint/yapf/black we've all tried,
later according to project scale we enabled different levels of checks,
in principle, the bigger the project the stricter the checks.
Regarding language and third-party library versions,
I basically keep up with community updates weekly,
maintaining code as a human dependency bot.
After solving these obvious problems,
in 2019 I happily sighed to my partners:
"I'm confident in saying that the project we wrote, even placed in the open source community, is first-class."

Framework-wise, we ultimately used Django at scale,
because Django's whole ORM is just so well-suited for CRUD business.
Performance-wise we later tried and ultimately used gevent,
making the whole project consistent to write,
and acceptable in runtime performance.

Now if asked to implement a standard Python Web service, I'd consider this tech combo:

- Use the latest versions, like Python3.8+/Django3+/Celery4.5+ etc.
- Enable a series of standard checks in CI, like flake8/isort/pytest/black
- Use toolchains like gnumake/pipenv/drf-yasg
- Use gunicorn+gevent as the runtime environment
- When language performance becomes a key problem, consider rewriting key parts in golang (though typically at that point the architecture needs a bigger update too)


## Platform

Over the past few years in my tech career,
I've mainly dealt with two platforms:
one is cloud platforms (AWS/Aliyun/Azure),
the other is business platforms (WeChat Open Platform).

Not much special to say about the business platform,
since the whole business piece I did is based on the WeChat ecosystem,
so I'm very familiar with the open platform, mini programs, OpenID/UnionID, payment callbacks, and so on.

The earliest cloud platform I touched was AWS (China).
I think the best thing about cloud platforms is flattened ops.
When hiring, I'd tell candidates,
in this position you'll touch everything from network, business, data, to deployment, monitoring.
And the foundation that enables this is
us "de-ops-ing" by letting everyone directly interface with the cloud platform
(some places might add a thin wrapper layer).

We earliest used AWS (China),
compared to international, China lacked some fundamental facilities
(like ACM/Route53 etc.)
which made libraries like zappa for serverless,
or higher-order services like AWS EKS unavailable.
At end of 2018 we switched from AWS to aliyun.
Architecturally there's no fundamental difference,
the feel of aliyun's service is indeed better,
though per @lxkaka's saying:
"This system can't be defended if there's no place to ask questions!"

Our current ways of using cloud platforms include:

- Most basic instance, load balancer, domain series
- Data-related MySQL/Redis/Mongo/EMR set
- Monitoring/alerting/log-related systems
- Fully managed K8S

As cloud platform usage deepens,
tech strongly bound to the cloud platform multiplies.
For example, the logging system basically abandoned ELK and embraced Aliyun's logging.
But from a cost perspective,
reducing redundant ops needs through tools
to some extent frees up engineer time and efficacy.

Now if asked to build cloud platform infra from scratch, I'd consider this combination:

- Split VPC subnets, generally three subnets for production, test, visitor are enough (with appropriate security group policies)
- Build the business system around managed K8S service, with supporting infra (cloud disk, logging, monitoring)
- Use LB/Gateway to constrain network ingress and egress, split traffic between subnets, minimize network overhead
- Prefer cloud-native features when choosing, like MySQL/ES/MQ


## Deployment

In the main site era,
our Python services ran via supervisor+virtualenv bare-deployed on three kinds of machines:

- Web: nginx+uwsgi+django
- Worker: celery worker
- Cron: celery beat

Updating code was using fabric to directly connect into machines for `git pull + supervisorctl restart` duo.

The problem here is seamless release (blue-green deployment) needed manual implementation.
For example, earliest we implemented a set of dynamic add/remove logic based on AWS LB.
This logic wasn't elegant,
and required self-maintenance.
Plus this had strong dependency on the machine environment,
in the Python version upgrade mentioned earlier,
we also had to do system-level upgrades together.

But soon afterwards we did full-site dockerization,
and had a brief period of seamless release based on docker network.
Deployment switched to `docker pull + docker(compose) restart`.
We removed supervisor/fabric/system dependencies from the whole tech chain.

Along with platform migration from AWS to aliyun,
most of our services went onto K8S.
Deployment also upgraded from machine-deploy to k8s-related deployment toolchain.

Most of the time projects use hand-written `envsubst + kubectl`,
but kubectl's version support is very limited,
so we often use kustomize in addition.
helm chart provides extra version control function for business systems
(we generally don't run many versions in production at the same time,
usually only keeping the latest version + canary).
But kustomize is only good at outputting deployment files,
no special features for showing deployment progress,
and [often misses a bunch of configmaps in projects][km-cm]...
So currently, many of our projects use kapp for deployment.

Build-wise, we fully migrated from earliest Jenkins CI to GitLab CI.
Besides integrating unit tests, auto-update of preview versions, canary releases as core flows,
we've also deeply tried many tool integrations GitLab CI provides.
Like kaniko/minio+artifacts/gitlab+sentry and series of auto-integration auto-deployment tools, we basically use them.

To this day, considering a new Python service I'd include this tech combo:

- Core deployment flow based on K8S, production/test use same config, distinguishing different business groups by namespace
- Don't use helm, use kubectl+kustomize+kapp for deployment
- Set up the new trio appropriately:
  - For HTTP/RESTful services, use gunicorn+django for Web (uwsgi is years out of maintenance)
  - For internal gRPC service calls, use internal djangrpc (based on django, supports one codebase running http+grpc)
  - For async tasks, simple celery
- For services mentioned above, consider in deployment full forward compatibility, traffic/user canary, standard monitoring/log/alerting setup


## Architecture

Early on our network topology was relatively simple,
the traffic route was `external ==> aws elb ==> nginx+uwsgi+django (single machine)`.
We only did minor configurations along the whole chain,
like configuring https handling on aws elb,
simple log collection on the machine.

Now our network topology has multiple paths.
Taking the relatively standard Aliyun-managed K8S Web service as example:
`external ==> ali slb ==> k8s ingress ==> nginx ==> gunicorn+django`.
By comparison you can see besides the k8s ingress layer,
the nginx layer is also separately split out.
This network topology gives us finer-grained control,
not only can each layer separately handle IP/traffic/logs/behavior logic,
but each layer is also removable and replaceable.
For example currently in our clusters,
some use `nginx-ingress-controller`,
others use `kong-ingress-controller`.

In the overall service architecture,
we split into three layers of services.
Top is Web layer, these services mainly serve externally, mainly public traffic RESTful calls;
middle is Service layer, mainly serving internally, mainly intranet RESTful/gRPC calls
(we're gradually replacing intranet RESTful with gRPC);
bottom is Tool layer, including a series of middleware we maintain, tool services, or wrapped cloud-native services.

With my current understanding, in a mid-sized technical team (100-person scale), I'd take this architecture tech combo:
- Use network as boundary to split internal/external traffic, external uses RESTful HTTP, internal uses gRPC
- When business is appropriate, use technology like Kong as a gateway, handling auth, canary, routing logic series
- Don't restrict tech selection between internal services (premise: do good people ladder training), but draw clear service boundaries, do appropriate layering
- Distinguish service levels at different layers, to define stability requirements, innovation room, network topology


## Collaboration

The core of team collaboration is human-to-human communication.

Because business lines are relatively many, we basically split teams at two pizza team granularity
(two pizza team meaning when ordering takeout, two pizzas can feed the whole team).
Each relatively small team owns several independent services,
team members are each other's backup, learn from each other, grow together.

Earliest our git dev flow was based on commit diffs,
in other words as long as your change is correct,
you could basically merge to the main branch.
— But we soon tasted the bitter fruit (this "soon" ≈ 3 years).
Some old code, because the product back then didn't leave behind a structured PRD,
and because our company makes B-end products, the logic is sometimes outrageously twisted in justifiable ways,
causing successors when blame-history-ing,
to often need to analyze whether this is bug or feature.

Currently, our whole team has (forcibly) reached consensus,
using "one PR has one commit doing one thing" rebase-based collaboration flow.
We produce a near-perfectly linear git history this way.

On the other hand, for version control we use internal little bots to manage based on git tags.
Because we don't need to consider backward compatibility maintenance,
in most cases we use date-style format (`v2020.07.01`).
Based on git tag we again integrated sentry-release/ticket-system with a series of toolchains,
including auto-generating changelogs between versions,
auto-categorizing and analyzing each version's release contents.

The whole collaboration mechanism of developing with git rebase and releasing with git tag benefited us a lot.
And to achieve this effect, we reached these agreements internally:

- In recognition, the project is based on rebase
  - There's no excuse like "I don't know how to use git," if you don't know you can learn.
  - Of course individuals can love merge, please use it in personal projects, in team projects we have unified specs
- In action, just do as we envisioned
  - Each PR contains one commit, each commit modifies one type of content
  - Submit PR then ask for Code Review, after review leave comments, after comments are addressed merge, no muddling around
- In tooling, we need a brother to solve collaboration tool improvement
  - We optimized Pipeline speed, running 97% coverage unit tests + all checks takes about 3 minutes
  - For linear history, we provide a series of release/merge/change-detection bot helper functions

Beyond the whole git-based dev flow,
we also collectively maintain a whole Newbie Village Quest (mentioned in a previous article).
And the Buddy system we promote lets an experienced classmate hand-hold the newcomer
(though this depends on how much each person puts their heart into it).


## Conclusion

Looking back, the technical discussions, choices, naming, dev, collaboration, retrospectives I participated in over these years all flash vividly before my eyes.
The more tech I know, the more I feel the breadth and fun of the tech world.
Actually doing tech is like playing games, essentially leveling up and equipping gear.
What's discussed in this article might also just be some fragmentary words from a corner of this world I can recall.

But if I had to delete the whole article,
keeping only one sentence,
I'd unhesitatingly keep this one:

**If you don't know, you can learn**

![u-can][u-can]

(To be continued)


[tree]: /backend-skill-tree-en
[py3]: /py2-to-py3-en
[wangyin]: https://www.yinwang.org/
[km-cm]: https://github.com/kubernetes-sigs/kustomize/issues/1806
[u-can]: /assets/u_can_learn.jpg
