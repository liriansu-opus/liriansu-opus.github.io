---
title: "What's Fun About Those Little Badges on GitHub"
date: "2017-08-08 23:10:01"
zhUrl: /github-badges
aliases:
  - /github-badges-en
---

Lots of GitHub project homepages put on fun little badges (GitHub Badges),
this time we'll also play with some surface-level stuff.

<!--more-->

## First, we need a project

A while back [Brother Jing][jkzing] complain-but-actually-loved [lowdb][lowdb]:

> This lowdb,
> useful is useful,
> but it's also too low...

I was very curious
and went to check out [lowdb][lowdb]'s introduction:

> This is a tiny JSON-format database.

Hmm, tiny, sounds cute.
Does Python have a counterpart library?
Yes, that's [tinydb][tinydb]~

> tinydb has about 1200 lines of source code, plus 1000 lines of tests.

Huh?! This is tiny?
This is level-18 tiny?

So we decided,
**we need a database that's tinier than tinydb, and lower than lowdb.**

Picking a name was suddenly an issue.
Since we were undecided,
[then we should just forgive him][forgive-meme]~
So another wheel was born:

[Forgive DB (hui-z/ForgiveDB)][forgivedb]

![readme][readme]


## GitHub Badges

Ignore the README's self-glorification of the project itself,
that long string of green little badges under the Logo
are the Badges~
[Since programmers generally hang out on GitHub][github],
people are also used to calling these GitHub Badges
(even though they can also be used elsewhere)

Essentially these little badges are clickable images,
for example using [Markdown syntax][markdown] you can write it like this:

```markdown
[![ForgiveDB](https://img.shields.io/badge/ForgiveDB-HuiZ-brightgreen.svg)](https://github.com/hui-z/ForgiveDB)

*This long string is actually Markdown's image syntax combined with hyperlink syntax*

![image syntax](https://img.shields.io/badge/ForgiveDB-HuiZ-brightgreen.svg)

[hyperlink syntax](https://github.com/hui-z/ForgiveDB)
```

The above string will look like this:

[![ForgiveDB](https://img.shields.io/badge/ForgiveDB-HuiZ-brightgreen.svg)](https://github.com/hui-z/ForgiveDB)

*This long string is actually Markdown's image syntax combined with hyperlink syntax*

![image syntax](https://img.shields.io/badge/ForgiveDB-HuiZ-brightgreen.svg)

[hyperlink syntax](https://github.com/hui-z/ForgiveDB)


## Various Badges

Specifically,
the badges we used in [ForgiveDB][forgivedb] are these:

* [**shields.io**][shields.io].
This one is worth pulling out separately,
because they're a website specifically for making Badges,
and the images are SVG vector images,
no blur on any resolution screen.
If we want to pick all sorts of strange Badges,
(like star counts,
issue closed counts,
npm, pypi, nuget versions,
even custom arbitrary strings)
we can find them on [shields.io][shields.io].

* [**PyPI**][pypi].
This is Python's official package repository,
[shields.io][shields.io] also supports automatic version sniffing.
Versions below 1.0.0 seem to also turn into a shit-yellow color...

* [**pyup.io**][pyup].
This service is fun,
once authorized it'll automatically check if your requirements are up to date.
If there's an update,
[pyup-bot will directly submit a Pull Request to the project...][pyup-pr]
Simply awesome.

* [**travis-ci.org**][travis].
This is the well-known Travis automated CI tool,
Travis is free for open-source projects,
very friendly.
And the features are powerful,
[lots of integrations with GitHub][github-travis],
super comfortable to use.
(As long as you write some UTs)

* Others:
There's also [CodeCov test coverage][codecov],
[AppVeyor, another nice CI][appveyor],
[CircleCI, yet another nice CI][circle-ci]
etc., etc......


Roughly that's the journey of picking pretty badges for ForgiveDB.
This kind of feeling
is just like picking pretty keycaps for the keyboard you love.

[Last, welcome everyone to submit Pull Requests to ForgiveDB][forgivedb]~
Even if you [just edit the docs like Brother Jing][doc-only-pr],
[mixing in a contributor mention is fine][contributor]~

[jkzing]: https://www.jingkaizhao.com/
[lowdb]: https://github.com/typicode/lowdb
[tinydb]: https://tinydb.readthedocs.io/en/latest/intro.html
[forgive-meme]: /forgive-her-meme-en
[forgivedb]: https://github.com/hui-z/ForgiveDB
[readme]: /assets/pics/github/forgive.jpg
[github]: /how-i-use-github-en
[markdown]: /hrbp-and-markdown-en
[shields.io]: https://shields.io/
[pypi]: https://pypi.python.org/pypi/forgive
[pyup]: https://pyup.io/repos/github/hui-z/ForgiveDB/
[pyup-pr]: https://github.com/hui-z/ForgiveDB/pull/7
[travis]: https://travis-ci.org/hui-z/ForgiveDB
[github-travis]: https://github.com/marketplace/travis-ci
[codecov]: https://codecov.io/github/hui-z/ForgiveDB?branch=master
[appveyor]: https://www.appveyor.com/
[circle-ci]: https://circleci.com/
[doc-only-pr]: https://github.com/hui-z/ForgiveDB/pull/8
[contributor]: https://github.com/hui-z/ForgiveDB/graphs/contributors
