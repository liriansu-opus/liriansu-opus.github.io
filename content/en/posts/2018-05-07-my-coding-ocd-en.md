---
layout: post
title: "A Bit of My OCD"
date: '2018-05-07 22:07:44'
zhUrl: /my-coding-ocd
aliases:
  - /my-coding-ocd-en
---

Every programmer has their own OCD.
Once it's triggered,
you can't help but silently shout in your heart, "comfy".

<!--more-->


# Use spaces correctly

> Research shows
> that people who don't like adding spaces between Chinese and English when typing
> walk a difficult path in love,
> with 70% ending up married to someone they don't love by age 34,
> and the remaining 30% can only leave their inheritance to their cats.
> After all, both love and writing need timely whitespace.
>
> - [vinta/pangu.js][pangu]

Modern programmers always come into contact with English,
and many times we mix English into Chinese.

At times like these, if I see text without whitespace, I get really uncomfortable:

```
Wrong: 我今天带GF去吃了KFC的嫩牛五方。
Right: 我今天带 GF 去吃了 KFC 的嫩牛五方。
```


# Use full-width and half-width punctuation correctly

When I, in the JSON sample data from a WeChat public account documentation,
discovered full-width double quotes,
I was as horrified as A-Feng was in junior high,
when he saw a dead rat in the middle of the road on his way back to the dorm.

Chinese uses full-width punctuation,
English uses half-width punctuation with whitespace,
and the connection points use full-width punctuation.

```
Wrong: 你们搞信息竞赛(OI)的有句话叫"code is cheap,show me your boyfriend。"
Right: 你们搞信息竞赛（OI）的有句话叫"code is cheap, show me your boyfriend."
```


# Text files end with a newline character

`No newline at end of file` is as alarming as "your room isn't locked".

To be professional,
[in the POSIX standard, a line is defined as][posix-line]:

> 3.206 Line
> A sequence of zero or more non-\<newline\> characters plus a terminating \<newline\> character.


# Use the right words to describe things

> You guys are this **enthusiastic** (用"地"),
> but you still need to raise your level of knowledge (用"的"),
> understand or **understand-able** (用"得")?

The ancients had a saying,
"Learn de-di-de well, and you'll fear nothing in the world." (referring to the three Chinese particles 的/地/得)

Thinking about it this way,
that fly's question was rather thought-provoking:
"What if back then we'd called shit 'rice'?"

[pangu]: https://github.com/vinta/pangu.js
[posix-line]: https://stackoverflow.com/questions/729692
