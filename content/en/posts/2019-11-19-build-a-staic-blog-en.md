---
title: "Building a Pure Static Blog Without Hosting Your Own Server"
date: 2019-11-19T01:00:07+08:00
zhUrl: /build-a-staic-blog
aliases:
  - /build-a-staic-blog-en
---

Also known as: how I switched from jekyll to hugo.

<!--more-->

This article will cover:

- Background
- Building the blog
- Usage feelings
- Open holes


## Background

A few months ago a friend emailed me:
"commentit is dead, remember to swap it out!"
That's when I realized this static comment system had reached the end of its project life.
Even [the GitHub Repo][commentit] is archived now.
Then I also realized:
*It's been a while since I last refurbished my homepage.*

That won't do.
**Life is in the tinkering.**

So taking advantage of recently switching to a new coding environment,
I redid my blog.
As the saying goes, a picture is worth a thousand words,
let me first show a picture of the renovated blog:

![blog-preview][blog-preview]



## Building the blog

> This chapter is about boring steps,
> the next chapter has my opinionated personal feelings XD

If you don't want to maintain your own server,
hosting on GitHub Pages is a great choice.
Four years ago when I built a blog with jekyll, I wrote a piece:
[《How this blog was built》][lki-build-jekyll].
Roughly speaking, building a feature-complete static blog has these steps:

1. Find a static content framework
2. Install a static comment system
3. Configure the rest: theme, domain, etc.

### Setting up the framework

[hugo][hugo] is very easy to install,
just use command line or [download from the official site][hugo-install]:

```
brew install hugo
```

Then [following the official tutorial][hugo-quickstart],
one-shot create directory + start with default theme:

```
hugo new site quickstart
cd quickstart
git init
git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
echo 'theme = "ananke"' >> config.toml
hugo server -D
```

For advanced stuff, just read the docs.
And with that, step one of finding a framework is done.

### Setting up comments

[utterances][utterances] is another tool that uses GitHub Issues for comments,
and it uses [Primer][primer] to achieve very high GitHub-style fidelity.

Installation is also very simple,
just find a template page and add its config:

```
<script src="https://utteranc.es/client.js"
        repo="[ENTER REPO HERE]"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
```

The result looks like this:

![utterances-preview][utterances-preview]

### Other accessories

The theme I'm using is [joway/hugo-theme-yinyang][yinyang],
its overall minimalist style I really like.

For fonts, since this is a personal blog, I didn't use rigorous fonts like FiraCode.
For English fonts I'm using [ipython/xkcd-font][xkcd-font].
For Chinese fonts I'm still looking for a cute handwritten one.

![xkcd-303][xkcd-303]

For the domain, by default it gives you a lki.github.io domain.
For custom domains, see the official docs: [github-custom-domain][github-custom-domain]
Remember to enable HTTPS in settings:

![github-pages][github-pages]

To count visitors, you can use the [static counter Busuanzi][busuanzi]:

![blog-header][blog-header]



## Usage feelings

My previous blog system also used GitHub Pages,
with jekyll + commentit as the toolchain.
Overall feelings are:

- Using GitHub Pages compared to self-hosted blog:
  - Pleasant: **no maintenance needed**
    The backend I do at work is already enough, I don't want to spend time investigating my own blog's 502 (x
  - Pleasant: cheap
    Uh, embrace open source, embrace open source.
  - Annoying: access speed isn't fast enough
    But this is because of GitHub, complaining is useless.
  - Annoying: **limited**
    For example, the comment function would be very easy to implement if self-hosted.
- Using hugo compared to jekyll:
  - Pleasant: freshness
    I have to say, indeed.
  - Pleasant: **hugo is written in go**
    Before, just for jekyll, I had to keep a redundant ruby environment on my computer, while go's environment is naturally there.
  - Pleasant: well-chosen defaults, no need for excessive customization
    Whether configuration or archetypes, hugo feels better to me, and [hardLineBreak][blackfriday-hlb] is really useful.
  - Annoying: GitHub only supports auto-building jekyll
    Adding a git pre-push hook actually solves this, not a huge problem.
- Using utterances compared to commentit:
  - Pleasant: **default style is better**
    The commentit style I previously hand-wrote, as a css-handicapped person I fell countless times on `inline-block`...
  - Pleasant: **syncing comments via issues is the right way**
    commentit's philosophy is to attach comments via git push, but after practice, using GitHub Issues is the way.

Also worth mentioning,
when considering migrating from jekyll,
I also seriously considered hexo.
But in the end because hugo looked more charming,
and also to stick to the unnecessary stubbornness from back then of giving up hexo
and choosing jekyll (x

![star-history][star-history]

> Attached: star growth trend comparison

There's also one happy little point,
which is that this theme's support for WeChat public account formatting is much better than before :)



### Open holes

The current blog overhaul is wrapped up for now,
next I'll definitely go back to the rhythm of seriously working and seriously recording life.

But for the blog itself,
there are still plenty of holes to fill:

- Use [Primer][primer] to unify the body and comment styles.
- Find a fun Chinese handwritten font. (Actually this conflicts with the above.)
- Provide font-switching options like TravisCI. (Aside from being cooooool, it's not useful.)
- Add a friend-links function, properly introduce the strength of my friends.
- Find a way to gracefully display the old commentit comments.

If I list them out,
the holes to fill come one after another.
After all, as Lu Xun often said:
"Personal blogs are worth seriously working on,
because after all, **life is in the tinkering**."


(End)


[commentit]: https://github.com/jillro/commentit
[lki-build-jekyll]: /how-this-blog-was-built-en
[hugo]: https://gohugo.io/
[hugo-install]: https://gohugo.io/getting-started/installing
[hugo-quickstart]: https://gohugo.io/getting-started/quick-start/
[utterances]: https://utteranc.es/
[primer]: https://primer.style/
[utterances-preview]: /assets/blog-hugo/utterances.png
[yinyang]: https://github.com/joway/hugo-theme-yinyang
[blog-preview]: /assets/blog-hugo/preview.png
[xkcd-font]: https://github.com/ipython/xkcd-font
[xkcd-303]: https://imgs.xkcd.com/comics/compiling.png
[github-custom-domain]: https://help.github.com/en/github/working-with-github-pages/about-custom-domains-and-github-pages
[github-pages]: /assets/blog-hugo/github-pages.png
[busuanzi]: https://busuanzi.ibruce.info/
[blog-header]: /assets/blog-hugo/header.png
[blackfriday-hlb]: https://gohugo.io/getting-started/configuration/#blackfriday-extensions
[star-history]: /assets/blog-hugo/star_history.png
