---
layout: post
title: "How to Write Bugs"
date: '2017-09-20 19:49:38'
zhUrl: /how-to-write-bugs
aliases:
  - /how-to-write-bugs-en
---

By now,
yours truly has more than ten years of experience writing Bugs.
It's about time I share some Bug-writing insights
with those of you who want to write Bugs but haven't quite mastered the craft.

<!--more-->

## Overview

Honestly speaking,
writing Bugs is not itself a particularly glorious thing.
But writing a Bug that is well-hidden / has huge impact / looks like a Feature,
and then fixing it,
is a magnificent thing indeed.
Often, beneath your flowing-water bugfix code,
[you can also collect 666666 exclamations of awe from the onlookers][bumblebee].

In general,
the techniques of writing Bugs can be divided into the following dimensions:

* Developing features
  - Testing is for cowards
  - Don't let the outside world discover Bugs
  - Warning? Doesn't exist
  - Copy other people's code
  - Follow historical patterns, don't change easily
  - Use intermediate states to complete features
* Cultivating habits
  - Embrace change in all situations
  - Configure a personalized development environment
  - Do less useless automation work
  - Work on multiple things at the same time
  - Trust other people's implementations
  - Always be full of confidence
* Communicating with people
  - Always only implement the 90% solution
  - Always only implement the 100% solution
  - Don't explain your code even during Code Review
  - Defend the legitimacy of your Bugs
  - Properly blame others for writing badly
* Long-term maintenance
  - Be a person who keeps duties and responsibilities clear
  - Believe that ignorance equals innocence
  - Share duties and responsibilities with users and operations
  - Write more code, productivity = destructive power

Below I'll walk you through the specific Bug-writing techniques one by one.


## Developing features

### Testing is for cowards

One of the natural enemies of Bugs is thorough testing.
To write more Bugs,
we need to reduce the amount of testing.
But not writing tests doesn't quite fly morally,
so we need to use some appropriate phrasing to explain:

* This feature is very simple, no need to write tests.
* This feature is too complex, don't want to write tests.
* This feature is temporary, not writing tests.
* We can't write tests for this feature.
* Relax, the code I write is rock solid, guaranteed bug-free.

A more advanced approach is, when developing a feature yourself,
first manually test it to make sure it's complete.
But a few months later,
when someone else modifies the related code,
they'll quietly slip a few Bugs in there.


### Don't let the outside world discover Bugs

Bugs are extremely annoying.
Basically once discovered, they'll get fixed.
For this,
we have two operations we can do:

1. **Don't let the Bug be discovered**.
During coding,
use operations like `catch Exception { ignore(); }` more often,
or just log the Bug info into a log file no one reads.
That way, even if the previous operation went wrong,
the subsequent operations can still keep going,
maybe just like in elementary school math problems:
the process is wrong, but the result is right?

2. **Don't let the Bug be fixed**.
This is actually very simple.
We just need to write a Feature based on probabilistic assumptions.
For example, the classic `race condition`,
modifying the same variable under high concurrency,
or not locking npm package versions,
then deploying to multiple environments at different times…


### Warning? Doesn't exist

Having Warnings in the code is perfectly normal.
We just need to make sure the code compiles and runs.
Most of the gray/yellow/underlined things in the IDE are features built by some OCD programmers.
We should turn off these IDE warnings.

Then there's the Lint tools,
which are more for checking spelling.
Everyone has different coding habits.
We should respect individual differences.
Whenever there's a habit inconsistency,
we should turn off the corresponding Linter check.


### Copy other people's code more

There's a saying in the programmer industry that's been passed down for over two hundred years:
"Don't reinvent the wheel."

So we should copy existing code more.
That way one Bug becomes two Bugs.
And in future new versions, the Bug in that section of code gets fixed,
but no one will discover that we also copied a copy of the code,
which still has the Bug.

When we want to customize part of the code from a third-party dependency library,
use less inheritance and composition,
use more copy and paste,
then add customized changes where we need them.


### Follow historical patterns, don't change easily

A lot of the time, the old code was written that way for a reason.
There's an old Chinese saying called "follow Xiao's plan as Cao did" (xiao gui cao sui),
which in programming means "the previous code was implemented this way, I should also write it this way."

This way, although we can only introduce new Bugs into new business,
we can inherit the Bugs of the old business.
And combining this technique with the previous one is even better:
"Copy historical code from before"
is a shortcut to greatly reducing the workload of writing Bugs.


### Use intermediate states to complete features

The code we write at work generally falls into two parts: technical code and business code.
Business code isn't very fun,
and it has clear deadlines.

At times like these we should silently meditate "I have to finish this quickly",
mutter "this is easy to implement",
while explaining "let me hack this together first, I'll clean it up later",
then with our programming literacy, solve the problem in a few quick strokes.

Although the Bugs written this way won't have a very long life cycle,
in case everyone gets busy later and forgets about the intermediate state here,
some Bugs will have a long life! Super!


## Cultivating habits

### Embrace change in all situations

There's a truth in the modern software development world,
called **"Requirements are always changing"**.
By the rules of logic:

* Because requirements are always changing,
* And because code is meant to implement requirements,
* Therefore code is also always changing.

The fact that we write new Bug after new Bug now has a solid theoretical foundation.

And here's a cool little trick:
the initial system design is generally simple,
the initial timeframe is also abundant,
but the time for changes is usually rather urgent.
So as long as we boldly embrace change and promise "I can implement this within this week",
there will be a small but ample window for us to perform in,
writing Bugs that others could never even design.


### Configure a personalized development environment

The development environment should NEVER, ever match the production environment:
because production environments are usually Linux, and Linux is too boring.
We should use some loose, case-insensitive systems like Windows/MacOS
as our development environment.

When developing on your own computer, to keep yourself happy,
you can globally install some nice fonts, very handy third-party libraries,
and then appropriately reference these customized awesome tools in your code.
Also, when testing, always use the latest version of the software,
like browsers, clients, code versions, etc.

When someone puzzledly reports a seeming Bug,
you can proudly reply: "Works on my machine."


### Do less useless automation work

If an automation program has a Bug,
once it's fixed, it's hard for it to be reintroduced.

But if every time we do some data operations,
we directly call code,
or write some one-off scripts to "automate" this operation,
then we have a chance to introduce brand new Bugs every time.

Although manual operations cost us more time,
they bring more potential for Bugs~


### Work on multiple things at the same time

Powerful people never leave their Bugs in only one project.

We should also be such people,
so just like "with great power comes great responsibility" says,
at any one moment we should dare to take on multiple tasks.
The tasks here can be big or small,
but each task should be in a different area.
It's even better if not only are the tasks urgent,
but stakeholders periodically chase you about them.

This way, while completing multiple tasks,
we can also fully experience the thrill of "context switching",
and leave our mark across multiple projects.


### Trust other people's implementations

Just as "The Pearl Bird" — which we had to study every few years through elementary, junior high, and high school — said:

> Trust often creates beautiful situations.

As pure and lovely programmers,
we should also trust others.
Trust that users are smart enough to definitely understand error messages,
trust that the requirements given by product managers are definitely simple,
trust that the designs given by designers are definitely easy to implement;
trust that the data passed in by the frontend is definitely valid,
trust that when valid data is passed in, the backend API definitely won't error;
trust that tested code definitely won't have problems in production,
trust that third-party libraries definitely won't break compatibility in minor versions,
trust that this expensive service is definitely better than MySQL.

And even when Bugs come out at times like these,
we can explain them away~
It's not our problem.
This Bug, see how exquisitely written it is.


### Always be full of confidence, no need to write comments

[20% of programmers in the world][pareto]
write 80% of the ~~programs~~ Bugs.
Generally speaking, programmers reading this article
should all belong to the top 20%.

Although I may not remember the code I wrote three years ago,
I should be able to understand the code I wrote a year ago.
So as long as I know I'm maintaining it myself,
there's no need to write much commentary.

And for people like us with great English,
of course we'd write comments in English.
But worried that the people reading the code might not have good English,
so let's just not write comments after all.

Based on this foundation of confidence,
we can also feel that all the Bugs we write are fixable,
so some temporary Bugs don't need to be taken too seriously.
As the saying goes, `When there's a bug, there's a fix.`


## Communicating with people

### Always only implement the 90% solution

Veteran programmers pass down by word of mouth a saying like this:
"Compared to a complex design that covers 100%, I prefer a simple design that covers 90%."

Although this way we can't write 100% of the Bugs,
actually according to this principle,
we can think of the abandoned 10% of users as one giant Bug.

Looked at this way,
with less work,
we've completed a bigger Bug.
It's actually more efficient.


### Always implement the 100% solution

Wise old Chinese elders speak an Eastern proverb that goes:
"He who travels a hundred li, ninety is half the journey."

When we do system design / business implementation,
if we can't do it the best,
if we don't consider all the cases,
then it's basically equivalent to not having implemented the feature at all.

The reasonable flow for software should be: design the whole system first,
then develop, deploy all at once,
then organize the Bugs from last time,
together with all the designs and features from next time, and deploy again.
This way the old Bugs can live longer,
and new Bugs can keep being deployed.

In a 100% solution,
although Bugs are reduced in part,
we can disperse the duties and responsibilities of writing Bugs.
In the end, the designers, implementers, testers, and deployers across the whole flow are all parents of the Bugs.


### Don't explain your code even during Code Review

With the popularization of modern software development workflows,
most programmers now use version control tools like Git.
But these are just tools for uploading code.
Even when version control is combined with project workflow tools,
we should still believe in the power of the individual.

When sending a Code Review, make good use of the auto-email function.
Explain less of the code logic, and chase others more: "approve my code quickly".
Because small Code Reviews are easier to read,
the Bugs you write will be seen through at a glance.
So an even better approach is to send a big PR with changes spanning hundreds or thousands of lines.
This not only shows our workload,
but also makes others daunted at the thought of Reviewing our code.

Over time,
others can only Review our coding style,
and then the Bugs can hide in the code logic,
traveling between dev, test, and production environments.


### Properly blame others for writing badly

If you've mastered all of the above techniques,
then congratulations, you've become an intermediate Bug-writing engineer.
At this point you've not only acquired the right to write Bugs,
you've also acquired the right to blame others.

Of course, we can't escalate to personal attacks,
so we should mainly attack other people's code:
"You shouldn't write it this way"
"I don't think writing it this way works"
"Writing it this way will have Bugs later"

To maintain an aura of mystery, also explain to others less about why / what is good code and what is bad code.
People with good mindsets, when blamed, may go google it and write fewer Bugs;
people with bad mindsets, when blamed, may doubt whether they're suited for this line of work.

Overall, people competing with us in writing Bugs will diminish.
This way next time we write Bugs openly,
we can also retort "You also wrote a Bug."


### Defend the legitimacy of your Bugs

Bugs also come in many varieties.
Different scenarios give rise to different Bugs,
varying in severity, urgency, and consequences.
Writing Bugs is truly the most normal everyday thing.

According to the saying "if it exists, it's reasonable",
we should bravely defend our Bugs.
The main phrases can converge with the techniques above,
and the essence is summarized as follows:

* How did you reproduce it? Works on my machine, are you sure you operated it correctly?
* This is an edge case, just don't operate this way, can be ignored.
* This was implemented this way before, it's not a Bug, it's a Feature.
* It was fine originally, it broke because the requirements changed, if requirements hadn't changed it wouldn't have broken.
* The script ran wrong, just fix it and re-run. A data problem, how can that be called a Bug?
* This feature wasn't written by me.
* When this was Code Reviewed, A-jun didn't catch it.
* When this was tested, B-jun didn't test it out.

Keep the above phrases firmly in mind,
throw them out at appropriate times,
and your inner confidence when writing Bugs will be all the more solid.


## Long-term maintenance

### Be a person who keeps duties and responsibilities clear

A civilization of over five thousand years of history passes down this saying:
"If you're not in the position, don't manage its affairs."

It means "code written by others, we don't need to care about. Bugs written by others, we don't need to fix."
Modern tools provide very convenient history features.
For example, Git has `git blame`.
Such features let us quickly pinpoint who wrote a certain Bug.

In normal conversations about code with others,
use more pronoun adverbs like "your code", "my code", "his code" to strengthen the sense of code ownership.
This way, when Bugs come out, others can't pass the buck.
Although the downside of this is that the Bugs we write ourselves
we have to fix ourselves.
But following the operations from the previous sections,
we can definitely pass the buck.

In short, in one sentence:
Bugs are all written by people.
If it's not written by you, it's written by me.

Be a person who keeps duties and responsibilities clear.
That way no one will be interested in our code,
and in our own code,
we can write as many Bugs as we want.


### Believe that ignorance equals innocence

Whether the ignorant are innocent or guilty is a topic that onlookers love to debate.
But in our Bug-writing programmer industry,
it's very clear: the ignorant are innocent.

For example, when we want to use a third-party library, how do we use it?
Just Baidu it, find the first piece of code, and copy-paste it.
We don't necessarily need to understand the principles of all the code,
because the demand to implement the feature is more urgent.
What if a Bug comes out?
The ignorant are innocent.
I didn't know there'd be a Bug.

Not too clear on what to do here,
ask A-jun to write a piece of code and send it to me.
Although I'm still not too clear on the specific operation,
this code was written by A-jun.
So when there's a Bug, the guilty one is also him.
And later when my call has problems,
I can also write quite a few Bugs to blame on him.

Ignorance equals innocence, that is:
when we write programs,
we don't need to understand the principle of every line.
As long as it works,
when the program has problems,
it can't be blamed on me.
After all, who hasn't had their newbie days?


### Share duties and responsibilities with users and operations

Technology surely can't solve every problem.
And technology surely can't solve people problems.

So many times, when there's a Bug,
it's not that we implemented it wrong,
it's that the user operated it wrong.

This tool is written for programmers.
They're all very smart.
No need to make it that polished.
Throw a `NullPointerException` once in a while,
they can surely read the trace.
Throw a `segmentation fault`,
they'll surely use `gdb` to step-debug it, right?

This tool is ultimately used by ops.
The `end user` can be trained,
so no need to make it too easy to use.
Just have the feature implemented.
Throw a 400 once in a while,
just teach the user to use the console.
Not every 500 in every case is an unusable bug.
Some cases can be resolved with a specific operation.

Why doesn't the user understand?
This, is also a Bug in another sense.


### Write more code, productivity = destructive power

Alright, you've finished the thirty-six stratagems of Sun Tzu's Art of War.
The last step, of course, is improving productivity.

As long as you've thoroughly studied this article,
mastered the art of Bug production,
then by working diligent overtime,
writing more code,
you can surely master the art of mass Bug production.

As a person named "Yu Gong" in Chinese mythology said,
writing Bugs is the same:

> Though I die, my son will live;
> But out of 100 lines of code there are 51 Bugs,
> Fix 1, and 78 Bugs remain;
> Though the code does not increase, the Bugs are inexhaustible.


Still need to keep training.

[_This article's ideas mimic "How To Write Unmaintainable Code"_][bad-code]

[pareto]: /pareto-rule-of-programmers-en
[bumblebee]: https://github.com/MrMEEE/bumblebee-Old-and-abbandoned/commit/a047be85247755cdbe0acce6#diff-1
[bad-code]: https://coolshell.cn/articles/4758.html
