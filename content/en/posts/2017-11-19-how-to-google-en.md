---
title: "How to Use Search Engines"
date: "2017-11-19 21:52:07"
zhUrl: /how-to-google
aliases:
  - /how-to-google-en
---

This is how I do it.

<!--more-->

In daily learning / work,
I often ask and get asked questions.
Sometimes I'm surprised to find that
I seem to be very good at answering other people's questions.

So I proudly introspected,
and discovered the reason for being "apparently good at answering questions":
I'm very good at using search engines.

So I sheepishly introspected again,
and discovered the reason for being "good at using search engines":
I've mastered some little tricks.

I've decided to write down these little tricks.
After you become familiar with them, understand them, apply them, master them,
I believe you too can become a quality Google UI.


## Don't use Baidu, use Google when possible

Among humans on the mainland,
the most widely used search engine should be Baidu.

But I don't like using Baidu.
Some subjective reasons are mainly the following:

* Bad reputation, replaceable.
For various reasons (fake medicine / promoted listings / leaked user info),
Baidu's search reputation is bad;
and competitor Sogou (sogou.com) can also replace the search function.
So I'd rather choose products with good reputations.

* Content updates are not timely.
For a chestnut, the latest content in GitHub Issues
is rarely indexed by Baidu [CITATION NEEDED].
And many obscure errors in code,
get indexed even less.

Personally, I recommend that friends who can access Google search
should all use Google search.
Although Google's China localization isn't necessarily great,
queries like "how to detect gas leaks",
"what's the meaning of bro drinks ice quokka cola meme",
"which YiDianDian flavor tastes better" can all be searched with appropriate answers.

For mainland humans who can't access Google,
they can also use Bing, Sogou, etc. as substitutes.
I personally usually use Sogou.

For programmer friends,
if you want to know more about "don't use Baidu search",
you can read [Coolshell's call: "Be an environmentally-conscious programmer, starting by not using Baidu"][anti-baidu]


## Find the X problem

I always thought the XYZ problem was a widely used saying,
turns out I might have been the first to use this phrasing.

The XYZ problem is described as ["sometimes what we want to solve is the X problem, but we get tangled up in the Y problem, and finally fall into the Z problem trap."][xyz]
To summarize: **find the root of the problem**.

For example, [the typewriter effect mentioned in that article][xyz]
is a good example of searching for the X problem.

Another example is a third-party library error you encounter when writing code.
Errors reported by programs are usually quite raw:
like `channel 0: open failed: administratively prohibited`.
Sometimes when we see the error,
we'll involuntarily think a few steps ahead.
We think maybe SSH channel ran into a permission issue,
so we search `linux ssh channel permission`,
and the answers go all over the place.
The best practice here is to use the raw error message directly to search,
because the raw error message is the most accurate description of the root problem.


## Use orthogonal search terms

Actually, when we searched `linux ssh channel permission` in the previous section,
we'd already used the orthogonal search terms trick.
Here I'm borrowing the math term orthogonal,
which means several search terms should be as **mutually distinctive and unrelated** as possible.

For example, if uncultured me
forgets the name of Zhu Ziqing's famous essay,
I can search "father oranges don't move"
and find the article "Silhouette" (Bei Ying).
~~(Actually you'll find memes / jokes / sticker packs)~~

For example, I know the speedster in DC comics is the Flash,
and I forget who the speedster is on the Marvel side,
then obviously searching with closely related words like "fast 1000 miles a day been to many places" won't surface Quicksilver.
We have to use "Marvel fast counterpart of Flash" as keywords to search,
and we'll get the appropriate result.


## Understand the result

Most of the time search engines won't give you the exact answer,
they'll give you a webpage.
If you searched for an error,
many times you'll get a Q&A forum page,
or a discussion thread.

This requires us to be able to extract useful key information from the whole page,
and sometimes also distinguish erroneous information.
This is where experience plays its role.
You just need to try downloading a pirated Chinese software,
and you'll grasp the trick of "extracting useful info".

If it's programming-related searching,
you need to know some basic methods for Stack Overflow / GitHub Issue:
for instance, high-voted answers on Stack Overflow are often from many years ago,
so watch out for language / library versions;
and on GitHub Issue, the answer with the most emoji is generally useful — empirical rules like these.

Many times you might be a search engine UI,
responsible for explaining the result to other people a second time.
Then on the premise that you're solving the [**X problem**][xyz],
the most useful thing is **putting yourself in their shoes**.
Determine the other person's stance / comprehension level / needs,
then tell it to them in language they can accept.


## Summary

* Don't use Baidu, use Google when possible.
* Find the X problem.
* Use orthogonal search terms.
* Understand the result.

As long as you do these few things,
you're a qualified search engine UI.

Top it off with a gentle attitude,
good camouflage,
and an unfathomable depth that no one can see through.

Congratulations, you've become a master in others' eyes!
(confetti)

[anti-baidu]: https://coolshell.cn/articles/9308.html
[xyz]: /x-y-z-question-en
