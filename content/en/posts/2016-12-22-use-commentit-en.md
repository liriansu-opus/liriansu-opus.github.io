---
title: "Disqus is unstable, so I started using commentit"
date: '2016-12-22 20:20:07'
zhUrl: /use-commentit
aliases:
  - /use-commentit-en
layout: post
---

Comments on a static blog hosted on GitHub Pages have always been a pain in the butt.
I used to always use [disqus][disqus],
but it's always teetering on the edge of being blocked by the GFW...

<!--more-->


[Because ~~I felt there was no need to set up a blog server from scratch~~ I was lazy, I directly went with GitHub Pages.][built-blog]
But since GitHub Pages is static, comments became a problem.
So after some research I used [disqus][disqus]'s third-party comments.

The convenient thing about disqus is that it's simple to set up.
I just had to register and add a [comments.template][disqus-template], and it would automatically expand into a comments section.
But for various reasons [disqus][disqus] doesn't support users behind the GFW well.

And I didn't want to use [Duoshuo][duoshuo] either — that one looks incredibly dumb...

Until I recently discovered a piece of black tech: [Comm(ent|it)][commentit].
A one-sentence summary of its static comment principle is: `all comments become Git Commits and get pushed to your Repository`.

Holy crap!
Feels great!

And [its template configuration is actually as simple as disqus's][commentit-template].
Addition: we also need to configure direct commits to master on [commentit's config page][commentit-config] :)

:) So it's time to comment below this page
to become a [Contributor to this blog's GitHub project~][contributors]

[disqus]:               https://disqus.com/
[built-blog]:           /how-this-blog-was-built-en
[disqus-template]:      https://github.com/LKI/lki.github.io/blob/b1c59b15a83fe0e0c9c2af55b15e1d3fa107c551/_includes/comments.html
[duoshuo]:              https://duoshuo.com/
[commentit]:            https://commentit.io/getting-started
[commentit-template]:   https://github.com/LKI/lki.github.io/blob/eb8e55e54fafc4effeeed8ed24ddae142829372b/_includes/comments.html
[commentit-config]:     https://commentit.io/settings?master=true&group=true
[contributors]:         https://github.com/LKI/lki.github.io/graphs/contributors
