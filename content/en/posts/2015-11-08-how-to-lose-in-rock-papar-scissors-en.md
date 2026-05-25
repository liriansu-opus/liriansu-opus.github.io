---
layout: post
title: "Losing Strategies in Rock Paper Scissors"
date: 2015-11-08T21:01:28.000Z
zhUrl: /how-to-lose-in-rock-paper-scissors
aliases:
  - /how-to-lose-in-rock-paper-scissors-en
---

When I was seven or eight, I was still reading "Reader's Digest".
There was an article in there that talked about winning strategies in rock paper scissors.

<!--more-->

## Rock Paper Scissors

Let me first say some useful nonsense.
In typical game theory situations, problems are simplified into an easy-to-judge model.
That is to say, even though a quick-reacting person can use `playing after the opponent` as a winning strategy,
mathematical models generally rule out this possibility.

(So it seems mathematicians don't quite like sociologists?)

In the rock paper scissors model, the rules are basically three points:

* Both sides play at the same time, picking one of rock, scissors, or paper.
* Rock beats scissors, scissors beat paper, paper beats rock.
* If it's a tie, play another round.

This kind of three-choice mutually-countering game also exists abroad—it's called [Rock-Paper-Scissors][RPS].


## Winning Strategy

Mathematical models often assume both players are smart people.
Obviously, in rock paper scissors a smart person's strategy is to play randomly,
that way both sides have a 50% chance of winning.

But in real situations, both sides are ordinary people.
*(Didn't I just say we'd simplify the model =_=)*
So we need to make an assumption:

**An ordinary person won't make the same choice twice in a row**

That is, if they played scissors this time, they probably won't play scissors next time.
So as long as you play paper next round, you won't lose.
Similarly, if the opponent plays rock, next round play scissors; if the opponent plays paper, next round play rock.

To generalize, under this assumption:
**Whatever your opponent plays, next round play the one that counters it**

Of course, the premise itself is the weakness of this strategy.
If your opponent is stubborn and never changes their move,
then this strategy will fail miserably.


## Real Combat Example

When walking down the stairs with my girlfriend, we played the game `whoever wins rock-paper-scissors takes a step`,
and before playing I quickly thought:

1. My girlfriend isn't happy when she loses, only happy when she wins, and if she's unhappy I can't be happy either.
2. My girlfriend won't logically nitpick with me, so she probably won't stubbornly play mind games with me.
3. My girlfriend likes to play paper the first round.

Yep, so I adopted `play rock first, then play the option that counters her`,
and successfully lost five or six rounds in a row.

Yep, after all, things like winning strategies can also be **used in reverse**.

[RPS]: https://en.wikipedia.org/wiki/Rock-paper-scissors
