---
title: "Hosting Static HTML Pages on GitHub"
date: '2017-02-03 21:59:54'
zhUrl: /hold-static-html-on-github
aliases:
  - /hold-static-html-on-github-en
layout: post
---

This is an entry-level technical article
teaching you how to host static HTML pages on GitHub.

<!--more-->


## GitHub Project Homepage

GitHub has a setting
where **the gh-pages branch of every project is accessible via `user-domain/project-name`**.

For example, I used to put some commonly-used js/css libraries in [my static project (LKI/static)][lki-static],
and the index.html on the `gh-pages` branch of that project could be directly accessed via [lki.github.io/static][html-static].

GitHub's original intent for this setting is [to let every project have its own homepage for display][pages],
but we can also borrow this setting to host static HTML pages.


## Hosting Static Pages

The rough steps to host pages are as follows:

1. Have your own GitHub account
2. Create a directory on GitHub [(Create new repository)][create-repo]
3. Use git to create a `gh-pages` branch under that project, and commit an index.html file

The command-line version of step 3 is roughly:

```
$ cd /Users/liriansu/new-repo
$ git init                        # initialize git directory
$ git checkout -b gh-pages        # create gh-pages branch and switch to it
# After running the previous command, put your index.html in the new-repo folder
$ git add index.html              # tell git index.html is going to be committed
$ git commit -m "add index.html"  # commit index.html
$ git remote add origin https://github.com/<username>/<repository>
$ git push -u origin gh-pages     # push to the GitHub server
```

Then we can see the just-committed index.html at `https://<username>.github.io/<repository>`.
Finally, if you want to build a personal blog on GitHub,
you can refer to [my setup approach][build-a-blog]


[build-a-blog]:   /how-this-blog-was-built-en
[lki-static]:     https://github.com/LKI/static
[html-static]:    /static/
[pages]:          https://pages.github.com/
[create-repo]:    https://github.com/new
