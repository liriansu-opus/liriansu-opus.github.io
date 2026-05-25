---
title: "Solution for Jekyll build fail"
date: "2016-01-29 23:24:45"
zhUrl: /jekyll-build-fail-solution
aliases:
  - /jekyll-build-fail-solution-en
---

I always felt the `jekyll build` results were different on my laptop and desktop.
I guessed it was because Jekyll versions weren't consistent.
Turns out after `gem update`,
`jekyll build` actually started failing instead...

<!--more-->

## Jekyll build

It's annoying when `jekyll build` results aren't stable,
especially seeing a pile of red file names in `git status` after every build.
And in fact most of them are just differences in HTML tag positions.

I suspected this might be caused by different Jekyll versions on the two machines,
so I ran `gem update` to sync to the latest version.

After that command finished, when I ran `jekyll build` what I got was
ruby errors like `jekyll build fail`.


## Solution

A quick search showed it's actually simple—this is caused by having multiple versions of jekyll installed at the same time,
and they conflict with each other.

(I can't help asking, why doesn't `gem update` automatically uninstall the old version?)

That's right, the solution is to run a `gem cleanup` to uninstall old versions.
At least this solution worked for my problem.


## Gem sources

Also: sometimes the official gem source is very slow, and you can use the `gem sources` command to switch to the Taobao source.
(Though the Taobao source might not update as frequently.)

```
$ gem sources -l
*** CURRENT SOURCES ***

https://rubygems.org/

$ gem sources -r https://rubygems.org/
https://rubygems.org/ removed from sources

$ gem sources -a https://rubygems.org/
https://rubygems.org/ added to sources
```
