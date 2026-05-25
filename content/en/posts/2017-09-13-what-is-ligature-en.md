---
title: "What is a Ligature"
date: "2017-09-13 22:45:39"
zhUrl: /what-is-ligature
aliases:
  - /what-is-ligature-en
---

Or "why do some characters disappear when copied from PDFs",
"why can fi be joined together in some fonts",
"how does Fira Code do those joined-up symbols"

<!--more-->

## ligature

ligature, the Wikipedia Chinese page calls it "合字" (compound character), but conceptually it's closer to "连字" (joined character).
As the literal meaning suggests, a ligature is a character joined together. For example, a Chinese ligature looks like this:

> As the saying goes, knowing the writing is like meeting the person.
>
> Some experts, based on Trump's signature,
> said his wild abandon is just like his single horizontal stroke, unrestrained...

![trump-chinese-ligature][trump-chinese-ligature]

In the Latin language family, ligatures as a feature are used a lot.
[For example the German letter `ß` was originally `ss`][wiki],
[the Latin letter `W` was originally `VV`, two `V`s...][wiki],
very magical.
And the `æ` letter we know from phonetics,
looks a lot like a ligature, but actually isn't a ligature,
`æ` is a letter actually used in Old English and a series of language families.


## fi and Printing

In the heyday of movable type printing,
people used type molds to print articles.
For one article,
if you wanted to use different fonts,
you had to pick correspondingly different type molds.

![fi][fi]

In some fonts when letter `f` and letter `i` are joined together,
the horizontal stroke of `f` would collide with the dot of `i`, making typesetting awkward.
So for convenience and aesthetics, some fonts directly have a `fi` ligature type mold.
Here whether it's printed-font ligatures, or handwritten-font ligatures above,
they're all the same concept, all called `ligature`.


## Ligature in Computer Fonts

Although computer fonts don't have all the physical limitations printed fonts do,
some fonts' `fi` still retain the `ligature` feature.
If you look around your computer font config page,
you can find the related properties.

Based on computers also being able to support ligatures,
clever people thought they could use it to do things!
For example there's a font called [Fira Code][fira-code].

[Fira Code][fira-code] claims itself to be the most suitable programming language for programmers,
because it's extremely friendly to various math symbols (details, please click the image below)

![fira-code-demo][fira-code-demo]

Of course the premise is the editor must also support ligature,
for example JetBrains-family IDEs:

![jetbrains-ligature][jetbrains-ligature]


Just as ancient wisdom says:

> Renew daily, renew every day, renew again

Got to keep learning.


[trump-chinese-ligature]: /assets/pics/trump_chinese_ligature.jpg
[wiki]: https://en.wikipedia.org/wiki/Typographic_ligature
[fi]: /assets/pics/fi.png
[fira-code]: https://github.com/tonsky/FiraCode
[fira-code-demo]: https://raw.githubusercontent.com/tonsky/FiraCode/master/showcases/all_ligatures.png
[jetbrains-ligature]: /assets/pics/jetbrains_ligature.png
