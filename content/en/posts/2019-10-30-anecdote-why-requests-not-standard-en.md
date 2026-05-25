---
title: "[Anecdote] Why isn't requests a Python standard library?"
date:      "2019-10-30 22:32:20"
zhUrl: /anecdote-why-requests-not-standard
aliases:
  - /anecdote-why-requests-not-standard-en
---

A few years ago during a chat with brother Haozi,
he said: "One day you'll evolve from finding bugfixes on StackOverflow
to finding bugfixes in GitHub issues."
A prophecy come true.

<!--more-->

## Header notes

I really like [what @灵剑 said in this passage][why-jdk-6]:

> There are two completely opposite philosophies in software maintenance:
> one is to track all dependencies at their latest version,
> trying out the newest one as soon as it's released;
> the other is to pin all dependencies at a fixed version that won't change,
> avoiding upgrades whenever possible.

Seeing software's metabolism brings me, the code writer, endless love and motivation,
and at the same time brings me a lot of github issues...

Code is written by humans, bugs are written by humans, bugfixes are also written by humans.
The text inside github issues is full of all kinds of flesh-and-blood, déjà-vu-filled comments.
Even though the words in issues are separated by time and space,
just like [xkcd 979 - wisdom of the ancients][xkcd-979] expresses,
some emotions never change.

![wisdom-of-the-ancients][wisdom-of-the-ancients]

While debugging at work,
on specific issues,
my colleagues have left behind a lot of brilliant discussion.

Given this,
I decided to start an "Anecdote" column,
specifically to talk about those interesting issues.


## Why isn't requests a Python standard library?

> Original URL:
> [https://github.com/psf/requests/issues/2424][psf-requests-2424]

[Kenneth Reitz][kenneth] is an industry-famous programmer.
Many people may know him because [he transformed from a 400-pound fat guy into a super handsome photography-loving programmer][kenneth-story].
But in fact, this technically-solid guy has also written useful tools like [python-requests][python-requests] and [httpbin][httpbin].

How important is the requests library?
According to publicly available info,
GitHub references reach `389k`,
making it the most-referenced library in Python.

Naturally, I had this question:
"Why isn't requests a Python standard library?"
As the main developer of the project,
Kenneth tossed a question to the community back in early 2015,
when Python 3.5 was still the era:
"If requests were to join the Python 3.5 standard library, what would you all think?"

Indeed, having a library enter the standard library has pros and cons, and requires community discussion.
So actually my question should be tweaked,
from "Why isn't requests a Python standard library?"
to "Why doesn't requests enter the Python standard library?"

Reading through the whole thread, basically these were the opinions:

- Pros:
  - Lower cost of use: many newbies can directly use the standard library.
  - Wider reach: many projects that depend only on standard libraries could use requests too.
- Cons:
  - Development process issues: the strict process of the standard library is totally different from community development, which might cause developer attrition in the end.
  - Dependency issues: the current library depends on quite a few certificate files etc., requiring major refactoring to enter the standard library.
  - Evolution speed issues: once in the standard library, interface and implementation get frozen, hard to quickly adapt to the best state along with the changing outside world.
  - Other historical issues: the old urllib library is already quite bloated for compatibility reasons, and needs refactoring too.

Overall,
the community's objections and concerns were bigger.
The more original flavor of the comments — readers can check out the original thread.

There were a few other points in the discussion that interested me:

- @Lukasa opened the thread with an opener: "Let me first ask a few big names what they think."
  Then @-ed these five: `@shazow @kevinburke @dstufft @alex @sigmavirus24`.
  I only know alex who wrote `cryptography`; the others are all worth getting to know.
- Halfway through the discussion, `@dcramer` left some comments about "I only use standard library dependencies,"
  then dropped a `not sure what you're all bitching about` and walked away...
  I wouldn't dare be so brash...
- Kenneth once wrote this line in the requests documentation:
  `Essentially, the standard library is where a library goes to die.`
  Which got dragged out multiple times during the discussion as a "face-slap" callout.
  (Actually it's fine, design philosophies can be designed.)
- [This April another guy @4evermaat raised this question again][psf-requests-5057].
  After reading the four-year-old discussion, he left this sigh:
  `I didn't realize there was so much politics in getting a module included in the stdlib.`

Now, four years after the discussion ended,
the `requests` library still lives vibrantly as an independent community project, metabolizing along,
and Python 3.5+ also added the standard library `urllib.request` supporting some core functions.

Code is designed by humans,
and also used by humans.
The stories behind it
are also part of the program's inner logic.
This part of the logic once lived in discussion threads,
and ultimately also lets the code breathe, metabolize, and survive more vividly.

(End)


[why-jdk-6]: https://www.zhihu.com/question/30137699/answer/476916096
[xkcd-979]: https://xkcd.com/979/
[wisdom-of-the-ancients]: https://imgs.xkcd.com/comics/wisdom_of_the_ancients.png
[psf-requests-2424]: https://github.com/psf/requests/issues/2424
[kenneth]: https://github.com/kennethreitz
[kenneth-story]: https://zhuanlan.zhihu.com/p/20346580
[psf-requests-5057]: https://github.com/psf/requests/issues/5057
[python-requests]: https://github.com/psf/requests
[httpbin]: https://github.com/postmanlabs/httpbin
