---
title: "How I Implemented \"Playing GBA Games with Danmaku\""
date: "2018-01-06 18:58:33"
zhUrl: /play-gba-with-danmaku
aliases:
  - /play-gba-with-danmaku-en
---

Around my sophomore year of college,
I saw an extremely interesting Idea on TwitchTV.

<!--more-->

## Background

[TwitchTV][twitch] is a foreign website that mainly does game livestreaming.
Viewers can open the webpage and watch live game streams,
and everyone can send danmaku (bullet comments) at any time to express their thoughts.
[_What is danmaku?_][danmaku]

Based on this premise of "ten thousand people on one screen sending danmaku",
TwitchTV built a really fun feature:
"thousands of people control the same character, playing the same game."
[_For details, see the Twitch Plays Pokemon Wikipedia article_][tpp]

When I saw this news,
I went and played a bit,
and the experience was: super fun!!!

When thousands of people play on one screen,
the biggest feeling is **chaos**,
which is also the best experience.
Most players play with the goal of completing the game,
so overall the character's behavior is goal-directed.
But some players also play just to mess things up,
and at moments of fine operation (like catching a Pokemon)
it gets extra chaotic.

In the end the whole game (or social experiment) advanced in chaos,
and after 16 days and nights,
finally defeated the Elite Four,
completing the heroic feat of beating the game.

OK, that was all background introduction.
Seeing such a fun thing,
my heart was itching for a long time:
I want to implement something similar too!


## Implementation

Just like stuffing an elephant in a fridge requires breaking it down into steps,
to implement "play GBA games with danmaku on one screen",
the main things we need to do are:

1. Apply for a livestream room
2. Get the danmaku from the livestream room
3. Implement mapping from danmaku to key presses
4. Use a program to control a GBA emulator

Of course, this breakdown is very coarse,
and there will be many specific issues.
Let's look at them one by one.


### Apply for a livestream room

If I remember correctly (_too lazy to verify_),
TwitchTV's same-screen game function should have been officially implemented,
not by some streamer or third-party programmer like me.
When a platform implements it themselves, they have a lot of autonomy,
and can also promote the game itself,
so a campaign push would have better results no matter how you look at it.

But we ordinary humans are weak.
We have to start from scratch,
starting from applying for a livestream room.

Applying for a livestream room mainly involves choosing the livestream platform.
Because I've always been an A/B Station user,
the livestream platform is basically a choice between Douyu ([A Station's Shengfangsong][shengfangsong]) and Bilibili Live.

In the end I registered a Douyu room two years ago.
(An ad: the livestream room that I never stream on: [douyu.com/lisp][lisp])

Step one is done.


### Get the danmaku from the livestream room

This is a very interesting problem.
First, it's affected by the previous question,
which leads to the real-world issue: **the difficulty of getting danmaku is different for each livestream platform**.

Comparing Douyu and Bilibili Live,
Douyu definitely has more viewers,
but due to the atmosphere and audience demographic,
[there are more programmers who write plugins for Bilibili][vim-bilibili] _CITATION NEEDED_.

But since we chose Douyu in the previous step,
we have to see it through.
So two years ago I followed [the question "How do you get danmaku info from Douyu livestream rooms?"][zhihu-douyu-danmu] on Zhihu,
and by the way learned some socket knowledge (yes, this sentence reflects my actual skill level...)

At the time there wasn't a good library to use,
and I was too lazy to research it myself,
so I got stuck here.

Later [while wandering around GitHub][play-github],
I found that the itchat author had written a package
supporting getting danmaku from various livestream platforms,
which felt like the wheel I needed!
[So I starred it first as a bookmark][danmu].

Today is January 2018.
This library's most recent update was May 2017,
so the code hasn't been updated for over half a year.
Before formally adopting it I tested it.
Douyu danmaku was fine,
but Bilibili danmaku, because it [parses the webpage source directly to get ROOMID][roomid],
had already broken.
And because this library (or littlecoder this person) isn't very Pythonic,
I secretly planted another flag in my heart,
forked this project,
thinking: whenever I've slacked off enough, I'll go improve it.

So in the end I adopted the danmu library,
and successfully got Douyu danmaku in a few lines of code.
The (pseudo)code looks roughly like this:

```
import danmu

client = danmu.DanMuClient('https://www.douyu.com/lisp')

@client.danmu
def receive(message):
    print('[{}] {}'.format(message['NickName'], message['Content']))

client.start()
```

### Implement mapping from danmaku to key presses

Nothing much to say about this one.
It's just business logic / grunt work.
Easy. Skip.


### Use a program to control a GBA emulator

OK, there's a pitfall here first.
Let's recall:
the original goal was to "implement playing GBA games with danmaku",
and now this small step got regressed to "using a program to control a GBA **emulator**".
Where did this emulator requirement come from?

Ah, this has its reasons.

First, my memories of GBA, aside from the physical console,
half of them are given by [`VisualBoyAdvance.exe`][vba] this emulator.
Also, in theory we could implement a Web version,
or roll our own GBA emulator,
but that would be extra work.
So based on the principles "break a goal I can't achieve down into smaller steps I can"
and "Lu Xun said, don't reinvent the wheel",
I split "use a program to play GBA games" into "use a program to control a GBA emulator" + "use a GBA emulator to play GBA games" (already exists) — two tasks.

OK, let's realistically look at the first point:
"How to use a program to control a GBA emulator."

In my mind,
if implemented in Python,
basically it would be Python calling Windows libraries + Windows libraries sending signals to the program + program receives signals to achieve effect.
This kind of combo should work.

Although my usual dev environment is Windows,
I actually know nothing about Windows APIs (exposing skill level x2).
But if you don't know, you can ask!
So a few days ago I asked hulucc, a Windows expert next to me,
and he said [Windows has an API called sendkey][sendkeys] that can do this,
but it can only control the active window.
Later he looked it up,
and told me Python has a library called `pywin32` that can call Windows APIs,
and sent me an article: [How to Build a Python Bot That Can Play Web Games][py-bot]
for reference.

After all this studying,
I was very moved,
and then went and found another library [keyboard][keyboard] (foggy).

The fact is I came back and researched it later.
Using the Windows API can definitely achieve my goal,
but the problem is [pywin32 or the similar pypiwin32, both packages don't have proper pip releases and need manual installation][pywin32-install],
which made me uncomfortable.
And while googling,
I found another Python library [`keyboard`][keyboard].
Its homepage looks pretty nice,
and it can meet my needs.
Not bad, this one.

So the implementation of receiving danmaku + sending key presses (pseudo)code looks roughly like this:

```
import danmu
import keyboard
import constants

client = danmu.DanMuClient('https://www.douyu.com/lisp')

@client.danmu
def receive(message):
    print('[{}] {}'.format(message['NickName'], message['Content']))
    content = message['Content']  # mainly added this line and the if below
    if content in constants.valid_keystrokes:
        keyboard.send(content)

client.start()
```

### A small pitfall

There's a small pitfall here.
Simply put, the GBA emulator VisualBoyAdvance (VBA below)
seems to translate key presses by monitoring keyboard events.
(This description isn't professional enough)

Translated into code language, the line `keyboard.send(content)` has no effect on VBA.
After some thinking plus trying,
in the end I used the combo of `keyboard.press(content)` + `time.sleep(0.02)` + `keyboard.release(content)` to achieve the effect.

In the end I can't help but exclaim:
the **thinking plus trying** part in the description above,
is the most painful and most beautiful thing about writing programs.


## Summary

The above was rather fragmented.
To summarize:

To make "playing GBA games with danmaku" happen,
the broken-down and completed tasks were:

* Register a livestream room, chose Douyu.
* Get livestream room danmaku, paid attention to info around me, finally used the danmu library.
* Implement business logic.
* Use a program to control a GBA emulator to play GBA games, used the keyboard library to send key info.

The final product is on my GitHub: [LKI/danmaboy][danmaboy] project,
with effective code being only about 100 lines, all in the [danmaboy/\_\_init\_\_.py][init.py] file.

Wrote it in one afternoon,
but the time spent slacking off and thinking in between was a few years (embarrassed).

In the afternoon while writing code I also did one experiment:
streaming while writing code.
But because no one was watching (the real reason),
the overall feeling was similar to rubber duck programming.
Wrote for a while, then nervously thought about the approach.
The effect was surprisingly good.

After the final product came out,
I tried running it in the livestream room,
~~startup failed~~ and ran into a fundamental flaw:

**Because it's a game, normal danmaku delay gets amplified to the point of extremely affecting the game experience in this project**

Basically you send a danmaku,
and 15 seconds later the corresponding game change happens.
Forget the TwitchTV effect,
even basic solo play wouldn't really work…

Sigh.

Still, it's one of many ideas in my heart.
This article serves as a period to put on this project.

I still have many unfinished endeavors in my heart.
If you're interested,
welcome to chat with me~

See you next time.

![screen][screen]
_Screenshot during the livestream_

[twitch]: https://www.twitch.tv/
[danmaku]: https://zh.moegirl.org/zh-hans/%E5%BC%B9%E5%B9%95
[tpp]: https://en.wikipedia.org/wiki/Twitch_Plays_Pok%C3%A9mon
[shengfangsong]: https://www.zhihu.com/question/27088840
[lisp]: https://www.douyu.com/lisp
[vim-bilibili]: https://github.com/feisuzhu/vim-bilibili-live
[play-github]: /how-i-use-github-en
[danmu]: https://github.com/littlecodersh/danmu
[roomid]: https://github.com/littlecodersh/danmu/blob/master/danmu/Bilibili.py
[zhihu-douyu-danmu]: https://www.zhihu.com/question/29027665
[vba]: https://en.wikipedia.org/wiki/VisualBoyAdvance
[sendkeys]: https://msdn.microsoft.com/en-us/library/system.windows.forms.sendkeys(v=vs.110).aspx
[py-bot]: https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117
[keyboard]: https://github.com/boppreh/keyboard
[pywin32-install]: https://stackoverflow.com/questions/4863056/how-to-install-pywin32-module-in-windows-7
[danmaboy]: https://github.com/LKI/danmaboy
[init.py]: https://github.com/LKI/danmaboy/blob/master/danmaboy/__init__.py
[screen]: /assets/pics/screen.png
