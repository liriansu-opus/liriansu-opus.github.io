---
title: "Thoughts from Attending QCon 2018 Day One Morning"
date: "2018-10-18 18:54:24"
zhUrl: /qcon-2018-shanghai
aliases:
  - /qcon-2018-shanghai-en
---

Actually this QCon had three days total,
but I only went for half a day.

<!--more-->

A few months ago as QCon approached,
the boss heroically waved:
"This year we're buying tickets to listen to QCon!"
So we happily went to the website to look,
one ticket is several thousand RMB...
......
With our limited budget we could only buy some tickets within our means,
then split each ticket into several pieces,
letting as many comrades as possible experience the atmosphere of the "Global Software Development Conference."
(QCon's Chinese name really is this!)

This time I just went to the morning,
after Peng Lei/Zang Xiutao gave opening remarks at the main hall,
I listened to three speaker sessions.


# Java API Design Best Practices

The first session was originally a foreigner talking about Go,
but seems like traffic on the way prevented him from making it to the venue,
so they temporarily switched to a different foreigner talking about Java.

This dude is called Jonathan,
the companies he's been at all along are Sun/Oracle/Microsoft,
after introducing himself,
the PPT suddenly cut to <Effective Java (3rd)>,
then Jonathan hyped: 
"This is a book all Java programmers must read!"

Then the topic gradually got on track, Jonathan proposed several qualities good APIs have:

- Understandable
- Consistent
- Fit for purpose
- Well documented
- Restrained
- Evolvable

Then Jonathan used specific examples interspersed to explain his understanding of these qualities.

Listening through I felt removing the specific syntax examples,
outstanding APIs share common qualities,
just like in the previously written [《Elegant Python API Design》](/api-design-in-python-en).

Finally Jonathan hyped <Effective Java> again,
and forcefully promoted: "Those of you who've only read the second edition, remember to buy the third edition and read it..."
Made you wonder if he got commissions from this book (x


# Tencent Microservices Architecture: Past, Present, and Future

After a short break, it was Tencent speaker Liu Xin's turn.

Although the topic was microservice framework,
it felt like most of the time Liu Xin was promoting their framework [Tars (github.com/TarsCloud)](https://github.com/tarscloud)...

But the overall logic was still very clear:
- Earliest encountered problems of complex business logic, hard-to-control code quality, chaotic operations management, missing monitoring system.
- Later under the guiding ideology of "big systems small build," gradually started unifying frameworks.
- The framework first implemented basic functions of service calls + service governance.
- Then improved performance + ease of use.
- Now also introduced containerization + high extensibility (actually at this step it can be open-sourced and promoted)

There were two fun data points in Liu Xin's PPT.
One is 51% are all considering switching to Cloud Native architecture.
The topic this data leads to is a quite good topic,
makes heavy AWS users really want to say something,
I feel I could write a dedicated article next time.

Another is a four-quadrant chart loosely divided by service governance / multi-language:

![MS](/assets/pics/micro_services.jpg)

Very interesting.

Finally Liu Xin spent quite a bit of time talking about the many languages TARS supports.
After listening I really admired him (then chose service mesh...)


# The Past, Present, and Future of GO 2

After a short break, David Chaney who should have spoken first finally came.
(@hulucc asked: what's his relationship to Go?
@紫月酥 answered: probably like @jkzing to VueJS, a core Contributor.)

At first David talked a lot of history,
like the original purpose of Go's birth,
the path Go walked growing up,
the difference between software engineering and coding,
updates of multiple versions of Go,
companies/teams/projects currently using Go etc...
Listening I felt like he's another typical evangelist,
just treat it as Go popularization for pure newbies...

Then!
David suddenly introduced gopher, this cutie:

![gopher](/assets/pics/gopher.jpg)

(Felt like the whole audience instantly four-foreigner-excited.jpg)

After the long setup,
David finally talked about the three big problems Go faces and needs to solve:

* Dependency management
* Error handling
* Generics

Hearing this I slapped my thigh:
"Yes yes yes! That's exactly why I dropped it!"

Following that David unhurriedly used various small examples to give the current solutions:

* Go 1.11 can already use go modules to manage dependencies. (First-timer me had a familiar node_modules vibe)
* Go 2 will introduce check/handle and other syntactic sugar to handle errors, essentially still requiring programmers to handle errors at first opportunity
* Go 2 will have generics, currently may introduce contract. (But on specifics, I feel I didn't quite get it, need to dig deeper later)

![generic](/assets/pics/generic_dilemma.jpg)

Then David specially emphasized,
Go2 and Go1 are only big version differences,
"won't be like Python3 or Perl6..."


# Reflections

The first morning of the main hall completely ended here.
Overall, I felt the gain in horizons outweighed technical gains.
Knowing what direction colleagues are deep-diving in is also a great gain.

Last quarter of 2018 will definitely pick up Go again to seriously play with it...
(But not having default parameter values really makes writing uncomfortable.jpg)

![qcon](/assets/pics/qcon.jpg)

(End)
