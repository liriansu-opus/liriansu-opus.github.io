---
title: "The Most Minimal Programming Language: Iota"
date: '2017-01-24 13:07:50'
zhUrl: /iota-language
aliases:
  - /iota-language-en
layout: post
---

This language has only two reserved words [(reserved keyword)][wiki-reserved-keyword]

<!--more-->


## Reserved keywords in various languages

While browsing SO today I found this question:
[Reserved keywords count by programming language?][so-reserved-keyword]

The number of reserved words in various languages, from largest to smallest, is roughly:

| ANSI COBOL 85 | 357   |
| JavaScript    | 180   |
| C#            | 102   |
| Java          | 50    |
| Python 3.x    | 33    |
| C             | 32    |
| Go            | 25    |
| Brainfuck     | 8     |
| iota          | **2** |

Yep, Python really does have few reserved words.
No wonder [there's a joke that Python is actually "executable pseudocode"][executable-pseudocode]

> python is executable pseudocode, while perl is executable line noise.

But wait, what is this iota language?
It can actually achieve Turing completeness with only two reserved words?


## Iota Programming Language

Although here we say Iota is a programming language,
actually writing executable script programs in Iota is not that simple.
The "programming language" here in a larger sense refers to the computer science concept of Turing-completeness for solving computable problems.
So first let's look at Iota's design concept:

[Iota on wikipedia][iota]

Uh, the page above is actually about the Greek letter Iota `ι`
The one below is the iota programming language:

[Iota and Jot][iota-jot]

The wiki introduces iota pretty well. Rough meaning (after I digested it):
Relative to the well-known [lambda calculus][lambda] and [SKI combinator calculus][ski],
Iota and Jot are very minimal [Formal Systems][formal-system].
Their design intent was to use as few operators as possible to achieve a Turing-complete language.
Simply put, iota has only two reserved words: one is `*`, and the other is `i`.
`*` combines the two following iota expressions, while `i` takes an expression `x` and returns `xSK`.

After reading the above paragraph you might be a bit dizzy.
So let's change perspective and imagine how iota was created.

A group of people gathered together.
Turing theory already existed,
lambda calculus already existed,
functional programming already existed.
Then someone asked a question:
What is the most minimal Turing-complete language?
So [Chris Barker][chris], standing on the shoulders of a series of existing theories,
invented the [iota][iota-jot] language.


## SKI Operators

[SKI][ski] is one important shoulder of a giant on iota's invention path.
SKI defines three operators in total: `S`, `K`, `I`
:) The names sound very simple and crude, I quite like them.
The rules are as follows:

* SKI appears in the form of parenthesized expressions. We can simply understand `xy = z` as `function x accepts argument y and returns value z`
* `I` accepts one argument and returns it, i.e. `Ix = x`
* `K` accepts two arguments and returns the first one, i.e. `Kxy = x`
* `S` accepts three arguments, returning the result of applying the first and third arguments to the second and third arguments, i.e. `Sxyz = xz(yz)`

Based on the above *mystical* definitions, magical things happen :)
**`SKI` actually only needs the `S` and `K` operators; `I` can be expressed as `SKK`** :

```
  SKKx
= Kx(Kx)      # by Sxyz = xz(yz)
= x           # by Kxy  = x
```

And through SKI, we can do many things:

* Recursion
* Negation
* Boolean logic

The examples above can be found in the [original wiki text: SKI combinator calculus][ski]


## Back to iota

After SKI, [Chris Barker][chris] proposed the iota operator,
with `ix = xSK`

So we can derive:

```
  ii
= iSK
= SSKK
= SK(KK)
= SKK <=> I

  i(iI)
= i(ISK)
= i(SK)
= SKSK
= KK(SK)
= K

  iK
= KSK
= S
```

:) Look, this is the charm of logic.
By defining a series of small cornerstones,
we can handle the whole edifice.

In summary, iota defined one key operator on top of SKI,
and added the `*` character to enable programmatic representation,
thereby achieving the goal of being the most minimal programming language.

[wiki-reserved-keyword]: https://en.wikipedia.org/wiki/Reserved_word
[so-reserved-keyword]: https://stackoverflow.com/questions/4980766/reserved-keywords-count-by-programming-language
[executable-pseudocode]: https://news.ycombinator.com/item?id=8241308
[iota]: https://en.wikipedia.org/wiki/Iota
[iota-jot]: https://en.wikipedia.org/wiki/Iota_and_Jot
[formal-system]: https://en.wikipedia.org/wiki/Formal_system
[lambda]: https://en.wikipedia.org/wiki/Lambda_calculus
[ski]: https://en.wikipedia.org/wiki/SKI_combinator_calculus
[chris]: https://en.wikipedia.org/wiki/Chris_Barker_(linguist)
