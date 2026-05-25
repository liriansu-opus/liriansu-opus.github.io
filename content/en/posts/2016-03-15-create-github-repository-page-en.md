---
title: "Creating a GitHub Project Page"
date: "2016-03-15 21:19:53"
zhUrl: /create-github-repository-page
aliases:
  - /create-github-repository-page-en
---

Recently I finally figured out by chance how to set up a homepage for a GitHub project.

<!--more-->


## GitHub Pages

GitHub Pages is a service that lets users conveniently host project web pages on GitHub.
For example, [this blog of mine is built with GitHub Pages][build-blog].

But this way you can only host one project named
[GitHub username + ".github.com" (lki.github.io)][lki-github].

What if I have another project that I also want to access by domain name?

So clever me [used `git submodule` to solve this problem][git-submodule].


## Git Submodule

`git submodule` is actually a pretty silly solution:

1. To ensure the latest content, the parent project has to update along with subproject updates.

2. This approach actually hacks jekyll build—doesn't feel particularly reliable.

3. [Removing a git submodule][remove-submodule] is just way too painful!
So don't add git submodule unless necessary.


## A Better Solution

The other day while browsing [senior sister Xianzhe][zhangwenli]'s GitHub I found [this Issue][issue3].

It says:

> After pointing the homepage CNAME to zhangwenli.com, ovilia.github.io will redirect to zhangwenli.com.
The gh-pages branches of other projects xxx will automatically map to ovilia.github.io/xxx.

Oh! So GitHub by default maps the "gh-pages" branch of the some-repo project to some-one.github.com/some-repo.

So we can create a new branch to map [the menu][git-mymenu] to [/mymenu][mymenu].


## Summary

1. GitHub projects can create a `gh-pages` branch to map under github.com to github.com/repository-name.

2. Look more, learn more, try more.

3. Unless it's a brilliant hack, pursue best practice.

[build-blog]: /how-this-blog-was-built-en
[lki-github]: https://github.com/LKI/lki.github.io
[git-submodule]: https://github.com/LKI/lki.github.io/commit/86d73353e4b8f93ea7e759fb0d2f47b5d9ad8904
[remove-submodule]: https://stackoverflow.com/questions/1260748/how-do-i-remove-a-submodule
[zhangwenli]: https://zhangwenli.com/
[issue3]: https://github.com/Ovilia/cv/issues/3
[git-mymenu]: https://github.com/LKI/mymenu
[mymenu]: /mymenu-en
