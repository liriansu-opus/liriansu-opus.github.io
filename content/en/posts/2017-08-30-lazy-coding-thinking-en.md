---
title: "How to Be Lazy When Writing Code? Let Me Think"
date: "2017-08-30 23:10:52"
zhUrl: /lazy-coding-thinking
aliases:
  - /lazy-coding-thinking-en
---

I'm really not bashing `Perl` just because I wrote `Python`.

<!--more-->

## Setup

After installing [wakatime][wakatime] this plugin recently,
I couldn't resist the curiosity to check exactly how much time I spend writing code on a normal day.
After rigorous data statistics:
I only spend 25% of my time writing code.
(At 40 hours a week,
I only write 10 hours of code a week=\_,=)

![old-waka][old-waka]

This is not good.
So I decided to buckle down,
and after thinking I was deeply immersed in writing code for a week,
25% became 33%.
So rigorous data statistics still indicated:
most of my time was spent slacking.

![new-waka][new-waka]

So I gave up the struggle,
just like Su Shi's friend Monk Foyin said:
`Since you've come, settle down` _he didn't actually say that_

I happily thought:
"Ahh.
I only spend this tiny bit of time working,
doesn't that mean I'm super efficient?"

"No, it just means you're lazy."
The little justice-man inside my heart popped out.

I very happily talked back:
"Right right, I'm just lazy.
And like I said before,
laziness has the kind that's not constructive,
and the kind that's once-and-done."

Hmm, today I want to try to convince the little justice-man in my heart,
**I'm not slacking, I'm thinking about problems!**

By the old routine,
I'll tell a story to explain the principle.
Pardon my poor performance!


## Development

From my senior year to graduation,
I was in [QAD][QAD] as R&D (i.e., R&D engineer)
Generally, "R&D engineer" is what it's called from a division-of-labor angle,
in foreign-language it's `SE, Software Engineer`,
corresponding to QA engineer `QA, Quality Assurance`.
In internet companies if it's web programming,
they'll split from another dimension into frontend engineer `FE, Front End`,
backend engineer `BE, Back End`.
Some also split by department into architecture, tech (business), algorithms, data different groups.

[QAD][QAD] mainly splits R&D departments by business,
we were the Foundation group (basic infrastructure group) at the time.
The company makes SaaS-form ERP systems. (SAP, Oracle are both our competitors)
SaaS here can simply be understood as annual subscription membership,
when Volkswagen company buys QAD's ERP system it's not a one-time deal,
once the contract is signed,
we're also responsible for the entire system's installation, training, maintenance, upgrades.
(Of course Volkswagen also pays corresponding "property fees")
The company's department divisions are roughly as follows:

* R&D responsible for developing software. R&D is the research and development department, Research and Development, I'm here...
* Sales responsible for selling products. (Sometimes R&D isn't done yet, the product is already sold, so it reverse-pressures R&D... very magical...)
* Service responsible for product installation, going live, training. Sometimes clients have customized requirements, Service also writes code. For example a Chinese pharmaceutical company needs to develop a set of FDA review processes, this is obviously not the standard flow, this requires **customized development**.
* Support responsible for daily support. For example when products have Bugs normally, Bugs at night, Bugs on weekends, all need to solve them for clients...
* Finance, Law, HR, CEO and other teammates provide internal support, maintaining orderly organizational operation.

The project I was on was called `CVC, Customer Version Control`.
The problem to solve was **version control of code in customized development.**
For example Volkswagen company,
they installed the QAD2008 version in 2008,
then based on the 2008 version did a lot of customized development around vehicle testing, vehicle safety performance, etc.
So when QAD wanted to upgrade the main program version,
Volkswagen exclaimed: ["1079 Merge Conflicts Found!!!"][xkcd-git]
This kind of conflict between customization and the main branch
was just one of the problems we were solving at the time,
others also included over 10G local code environment build,
dev-test-sup-prod multi-environment code management,
soft/hard lock, etc.


## Turn

Little justice-man: "ok, so you talked all this,
not one sentence related to actually writing the program..."

Indeed, not one sentence related to actually writing the program.
Well since I've rambled this much,
let me ramble even more...

For tech selection, at first we used `Git` + `Perl`.
Because we were doing code version control,
the core wheel used `Git`,
the team's tech stack at the time was mainly `Git vs SVN`,
plus because we needed to do multi-environment management,
so `git rebase`, `git cherry-pick`, `git filter-branch` and a string of commands that can modify history had obvious advantages.
Plus because the whole project was ultimately a command-line tool,
and the team's previous main tech stack was `Perl`,
[the project language adopted `Perl`][pl].
This language `Perl`'s strongest point is its command-line interaction and text processing,
many `shell` commands are natively shared,
like `echo, test -f, $@` etc.;
on text processing, regex and some `heredoc` are also very beautiful.
But `Perl`'s biggest problem isn't actually [the language itself's notorious ghost-script appearance][jokes],
the biggest problem is: `Perl` is declining day by day.
For example if we say we're hiring `Java` engineers,
we can actually hire many talents,
but similarly hiring `Perl` engineers,
the probability of hiring equally talented people may not be much higher,
but the cost paid would be much higher.

So later I did one thing,
used `Java` to rewrite `CVC` in my off-hours.
March-April Shanghai is especially cool,
I lived close to the company,
after dinner at six-something, walked home for a shower,
put on slippers and bounced back to the company.
Daytime writing `Perl`, nighttime writing `Java`, super happy.
The boss at the time was also very good at going with the flow,
seeing me refactoring the project on my own,
he gave me fewer tasks too,
so later in work hours I was also "slacking" writing `Java`.
Because the requirements were clear, the feature points were clear,
just like this two months passed,
twenty thousand lines of `Perl` code plus the same scale of unit tests,
(for a moment I really couldn't find a more appropriate metric than lines of code...)
half of it got refactored by me to `Java`...
Later everyone together filled in the various Edge Cases,
the whole product officially switched to `Java`,
which counts as a tiny contribution.


## Close

My time at QAD (July 2014 to October 2016)
was basically all contributed to the CVC project.
Same features,
the `Perl` version took more than a year to implement,
the `Java` version took a few months to implement.
The deciding factor had nothing to do with language expressiveness,
but with `business requirements` and `business understanding`.

As mentioned in the project flow above,
the project was doing **customized development**,
requirements came from **Service** department colleagues.
At first they didn't know what kind of software was easy to use,
the product mode we defined (e.g., free checkout files),
but they felt another mode was better (developers change frequently, need soft lock on files),
or felt the product could be better (e.g., the flow needs to be deeply integrated with Jira).
So actually we kept progressing on this `Design - Refine` cycle
(in Chinese the saying is "took quite a few detours")

Also during refactoring,
because we knew the overall shape of the requirements,
we could better abstract the logic.
Just like an architect designing a house,
because they know the overall structure,
they can determine the load-bearing of the beams,
the materials of the components.


Little justice-man thought, said:
"Oh, I see. You're saying,
slacking off and not writing the program is actually just putting the pen down,
to think about what kind of program to write?
Requirements more accurate, understanding more clear, things will go better?"

"Right right! Full marks understanding!"

Little justice-man again with a face of disdain:
"But in real life, this won't be the situation."

Yeah, so I can only say "learned, learned" on one side,
while thinking "who am I, where am I, what program should I write?"


[wakatime]: https://wakatime.com/dashboard
[old-waka]: /assets/pics/wakatime_dashboard.jpg
[new-waka]: /assets/pics/wakatime.png
[QAD]: https://www.qad.com/about
[xkcd-git]: https://xkcd.com/1597/
[pl]: https://www.tiobe.com/tiobe-index/
[jokes]: https://coolshell.cn/articles/1903.html
