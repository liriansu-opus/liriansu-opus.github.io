---
title: "Writing Programs and Picking Names"
date: "2017-06-24 19:36:17"
zhUrl: /naming-variable
aliases:
  - /naming-variable-en
---

It's said that on average,
programmers spend 10% of their time picking names.

<!--more-->

Today when chatting with Junru,
we talked about something I'd seen on Zhihu,
about why *Kaku-San-Sei Million Arthur* shut down:

![ma][ma]

A chunibyo programmer of this caliber really can leave his name in history...
Large programs are usually group jobs,
so writing programs with "clear logic, self-explanatory naming"
is also a required skill for a programmer.

Following the routine of a normal article,
here we should introduce that
the vast majority of computer terms have a unique CN-EN correspondence:

```
服务器 - Server
表 - Table
事务 - Transaction
等等
```

Words like these generally don't have much dispute.
When writing programs you can just write them straightforwardly.
But sometimes programmers have to write code that's rich in requirements,
and then you can have some fun.


# Code Snippets

There was a piece of code before
that needed to implement features related to advertorials and soft ads.
So when picking a variable name,
Xiangshen slapped his thigh:
that'd be the word `advertorial`!
This word is super accurate,
it means exactly "advertorial."
The peanut-gallery crowd unanimously declared: awesome!

Then the code was written,
and we ran it in the browser:
turns out the backend API call broke...
On closer inspection,
the browser's ad-blocker plugin had automatically recognized the word advertorial
and blocked our API...
...
So later in the database,
advertorial was still `advertorial`,
but in the url,
advertorial became `soft_article`...
The peanut-gallery declared this even more awesome...


There was also another piece of code
that needed to implement a gift-bundle feature.
Similar to the Starbucks 88-yuan gift card,
giving coupons, points, stored value, etc...
So the question came:
what name should this "gift bundle" abstract class be given?

The existing English correspondences in the system already included:
`积分奖 reward`, `券 coupon`, `礼品卡 gift_card`, etc.
It felt like all the good names were taken,
we all paused our keyboards
and started brainstorming...

gift\_bag felt really stupid,
especially with gift\_card already existing.

This kind of reward is a stacking of a series of products,
could also be called production,
but that would be ambiguous with production environment.

In the end we named this thing:
`one_piece`.
Yep, OnePiece is the pirate treasure from *One Piece*.

Giving an abstract class a meaningless name
actually leaves a deep impression, with no ambiguity.
Explain it once and you'll never forget it...


# Faithful, Expressive, Elegant

Actually picking names when writing programs,
a lot of the time you can just pick one randomly and it's easy,
but if you want to pursue a faithful, expressive, elegant expression,
you've got to think carefully.

Recently in my spare time I've been writing some mahjong-related code,
and I really feel translation is hard!
Things like suit and rank can correspond to playing cards' `Suit` and `Rank`,
but I'm pretty lost on some of the yaku names:

* `Thirteen Orphans / Kokushi Musou`, according to [Wikipedia it's `ThirteenOrphans`][wiki-thirteen-orphans]
    * Then the terminal tiles are probably `OrphanTile`...
* `Nine Lotus Lamps`, some translate it as `Nine Gates`, I'll believe that for now...
* `Moon Fishing from Sea Bottom`, `Robbing a Kong`, how should these go...

:) So it looks like the saying that 10% of the time goes to picking variable names
is actually pretty conservative.

Just as programmers often say
`Talk is cheap, show me the code`,
there's a great translation:
`废话少说，放码过来`.

Got to keep training.

[ma]: /assets/pics/ma_dead_reason.jpg
[wiki-thirteen-orphans]: https://zh.wikipedia.org/wiki/%E5%8D%81%E4%B8%89%E5%B9%BA
