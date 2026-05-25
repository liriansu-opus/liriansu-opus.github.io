---
layout: post
title: How This Blog Was Built
date: 2015-09-24T20:26:17.000Z
zhUrl: /how-this-blog-was-built
aliases:
  - /how-this-blog-was-built-en
---

At the very beginning, I actually used [LAMP][wiki-LAMP] to set up a personal blog on the school's IP. Setting up a blog this way had a few dumb problems:

<!--more-->

* The internet cuts off at 11pm and only comes back at 6am, so this "personal blog" would go offline
* The school blocked outbound port 80, and domain access defaults to port 80, so accessing the blog from off-campus required this weird format like `https://cloudisdream:8080`
* Since my own computer was the server, I had to keep it on the whole time, which wasn't great

## JAVA / Servlet / Structs + Spring + Hibernate

> After collecting a generous tip, the innkeeper whispered to you: every university's software engineering major teaches JAVA+SSH

Actually before LAMP, I had tried writing a microblog-like (personal?) website using Java+Servlet from coursework

It looked like this:
![First site][thats-moon]

While writing I kept marveling at how hard web design really is, and actually this homepage was modeled after NetEase Weibo of that era


## LAMP + WordPress

After writing once through from frontend HTML CSS JS to backend JAVA SQL, I started realizing that although full-stack engineer sounds great, actually writing it is exhausting

At that time chatting with ED, just talking about how [his blog][edward-mj.com] was built with WordPress, so I set up a server on my own computer

Although I mentioned the drawbacks of setting up a server this way at the start of the article, the school actually did give us a convenience: **fixed IP**

So I went to Wanwang and bought a domain name, CNAME-d it to the school IP.

But because I really couldn't bear keeping the computer on all the time, and also the network cutting off, eventually I abandoned this approach.


## Github Pages + Jekyll

The current blog is the simplest [GitHub Pages][github-pages] + [Jekyll][jekyll]

Putting webpages on GitHub gives you the natural advantage of version control. Jekyll uses Ruby, simple and easy to use.

Building a blog from scratch is basically just these steps:

1. Register a GitHub account and create the directory account.github.com
2. Run `gem install jekyll`, then `gem new my-site`
3. Modify `_config.yml` to your own settings, then add blogs in the `_post` folder


## Comments

A blog without comments always feels like something's off. Since it's a static page on GitHub, the basic solutions are: use [Duoshuo Comments][duoshuo], [Disqus][disqus], or customize comments using GitHub issues
(at first I even thought disqus == disquz)

Considering all aspects, I went with Disqus, following [the official documentation][disqus-jekyll]

Just insert a Comment Code snippet in the Page and you're done.


## Enhancement

At this point, the basic blog theme has been fully set up

But there are still a few areas of dissatisfaction:

1. The Twitter icon at the bottom of the page should be changed to Weibo (but I haven't figured out how to draw it)
2. Need to complete the About page
3. The Kramdown GFM render style still doesn't feel quite right, especially the interface — [GitHub Issue's Render style][github-render] looks more comfortable

Looks like in the future, while writing the blog I also need to continuously optimize the website!

[wiki-LAMP]:     https://en.wikipedia.org/wiki/LAMP_(software_bundle)
[thats-moon]:    /assets/thatsMoonPage.jpg
[edward-mj.com]: https://edward-mj.com/
[github-pages]:  https://pages.github.com/
[jekyll]:        https://jekyllrb.com/
[duoshuo]:       https://duoshuo.com/
[disqus]:        https://disqus.com/
[disqus-jekyll]: https://help.disqus.com/customer/portal/articles/472138-jekyll-installation-instructions
[github-render]: https://github.com/LKI/blogs/issues/3
