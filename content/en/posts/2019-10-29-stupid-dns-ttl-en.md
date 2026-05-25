---
title: "Yep, the DNS TTL field is lying to you"
date:      "2019-10-29 21:49:42"
zhUrl: /stupid-dns-ttl
aliases:
  - /stupid-dns-ttl-en
---

> By design,
> the Internet core is stupid,
> and the edge is smart.

<!--more-->

## Intro

A few days ago while surfing the web,
I came across a treasure article about DNS:
[DNS TTL Violations in the Wild][dns-ttl-violation].

The reason it's a treasure article for me is that
after reading just the first paragraph,
I realized that a notion I had taken for granted was actually wrong:
*The industry follows DNS TTL expiration logic.*

The reality is:
**The industry knows about DNS TTL expiration logic, but doesn't necessarily implement it that way.**


## Incident

A few weeks ago we had a bug
that affected the entire dev and test environment.

A big part of our business is doing all kinds of py (transactions) with WeChat.
[WeChat asks us to provide a callback domain][component-verify-ticket],
and every 10 minutes pushes a credential to us,
so that we can use the latest WeChat credential to call their APIs.

The earliest WeChat callback domain we configured pointed to an AWS ELB,
which is the older version of Amazon's cloud load balancer;
later we planned to switch to the new AWS ALB.

The operation was simple enough.
I looked it up in the DNS provider,
the TTL of the WeChat callback domain was 600 seconds,
and it was just a dev/test environment.
So we just directly switched the DNS to point to the new load balancer,
~~(in the spirit of saving money)~~ and casually deleted the old one too.

Oh boy.
WeChat didn't push the authorization credential to us for the whole day.
So our WeChat functionality on dev/test was down for a whole day.

Sometimes when problems happen in dev/test environments,
the suffering is just as much as in production.
Because you'll find your colleagues
asking you every 10 minutes:
"Bro, is WeChat working yet?"


## Question

After changing the DNS to 86400 seconds,
WeChat successfully resumed pushing credentials to us.

Once we judged from the symptoms it was a DNS problem,
while silently sneering at WeChat,
I also got a question in mind:
"This doesn't make sense — DNS is such a fundamental service, how could there be a bug?"

This brings us back to the opening of this article:
the industry knows about DNS TTL expiration logic, but doesn't necessarily implement it that way.

Each DNS record consists of two parts of data:
which domain should point to which destination?
And how long am I valid for?
These two pieces of data layer up and weave together in the internet's characteristic tree structure.
When a terminal does DNS resolution,
any DNS server along the link can implement a standard or non-standard logic.

For the TTL value,
there are only three possible implementation logics:

1. Cache time equals DNS TTL time.
2. Cache time is less than DNS TTL time.
3. Cache time is greater than DNS TTL time.


## World

If I were to write the logic of a DNS server,
I would, barring accidents, implement it strictly by definition.
Of course, due to limits of performance, time, and space,
the final implementation would have a few seconds of error,
but that's not the key.

The key is, [quite a few people think the current DNS design has flaws][state-manage].
And as the underlying architecture of the entire Internet,
whether to improve or replace the current DNS logic
is a massive undertaking.
Of course, this also makes it more attractive for engineers to devote themselves to.

So, domain resolution in the real world today
is not strictly implemented as "cache time equals DNS TTL time."

- When cache time is less than DNS TTL time:
  - The main point of contention is that this brings more resolution pressure on upstream servers
  - More frequent resolution also means more bandwidth and network costs
  - But this case doesn't harm end users
- When cache time is greater than DNS TTL time:
  - The main problem is that this causes users to access the wrong server
  - This not only brings logical errors but also potential security risks
  - The problem at the start of this article was actually a case of stale DNS caches along the WeChat link
  - The upside might be not having to pay as much in resolution fees (x


## Summary

Overall, DNS TTL is a convention widely used in internet infrastructure.
But in the real world there are also many non-standard implementations.
Due to the special nature of DNS, every non-standard domain provider affects a swath of users they can reach.
So when we operate on DNS, to solve problems gracefully we have to consider them too.

Engineering problems are like this —
there's both theoretical elegance,
mortal stupidity,
and the wisdom of distributed systems.

> By design,
> the Internet core is stupid,
> and the edge is smart.

(End)

[dns-ttl-violation]: https://labs.ripe.net/Members/giovane_moura/dns-ttl-violations-in-the-wild-with-ripe-atlas-2
[component-verify-ticket]: https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/Authorization_Process_Technical_Description.html
[state-manage]: https://mailarchive.ietf.org/arch/msg/dnsop/zRuuXkwmklMHFvl_Qqzn2N0SOGY/?qid=ff8e732c964b76fed3bbf333b89b111f
