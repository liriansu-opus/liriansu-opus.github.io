---
layout: post
title: "Why I Like Engineer Culture"
date: '2018-07-26 22:38:44'
zhUrl: /engineer-culture
aliases:
  - /engineer-culture-en
---

<!--more-->

Mia's company's parent company is 3G Capital.
The other day she suddenly got curious about what the company culture was like,
and went and read some materials about it.

Then Mia surprisedly told me:
"I found 3G Capital's requirements for talent really magical.
The three keywords are smart, poor, desire to be rich..."
The air was instantly filled with happy laughter.

Later I thought,
what's the corporate culture at my company?
If I had to say, it'd probably be `engineer culture`.


# Engineer Culture

When watching American TV shows,
we find that Americans always have a garage on the first floor,
the garage's toolbox holds all kinds of heirloom practical tools,
Mickey/Rick/Baymax all came out of the garage.

The engineer culture of software engineers is very similar to this scene:
- Learn through practice
- Solve problems with tools
- Autonomous decision-making

I really like this kind of engineer culture.
Specifically,
let's take a Series B company's R&D department as an example,
which is the company I'm currently at:
Zaihui (Shanghai) Network Technology Co., Ltd.


## Learn Through Practice

We have a document called
`the Hitchhiker's Guide to ZaiHui Dev`,
commonly known as "Newbie Village Quest,"
the document roughly looks like this:

![guide][guide]

The document chapters include setting up the dev environment,
familiarizing with basic business, participating in collaboration workflows, getting to know the basic architecture,
plus appendices called DLC including permissions, teammates, little scripts, etc.

In addition to this complete set of documentation,
each person is also assigned a buddy,
just like an old assassin with a new assassin,
new comrades on the path of "nothing is true, everything is permitted" can grab their buddy and ask anything thoroughly when they have questions.

For example, the backend's Newbie Village Quest looks roughly like this (excerpt):

- Play with the API
  - Run a server locally, try using the interface to get info for merchant id=1
  - Try using the test environment's login interface, get your own key
  - Figure out a way to add a permissioned account for yourself in all test environments
  - Modify your own username in the library by calling the api
- Play with the DB
  - Join a meeting in the test environment
  - Find the "Avada Kedavra" related function in the code, deactivate your own account
  - Study the code that sends verification codes (pin.py) and set yourself a permanent verification code in the test environment
- Write Bugs
  - Try to break the <Hui Ba Grilled Fish> public account, get WeChat to show "this public account cannot provide service" (remember to fix it! Otherwise the test daddy will yell!)
  - Try to write a unit test that has a chance of failing without using the random library
  - Write a circular import, make all uts fail
  - Try changing some code in the test environment, then break the deployment of that environment (expected result is an error when running pull_new_code)

Generally,
a teammate with Python experience can finish the Newbie Village Quest in about a week,
getting familiar with our main business and the general framework of the backend.
A teammate just out of school can also learn the workflow of RESTful/MySQL/Git/Jenkins through this full process.

Correspondingly, we also practice the DevOps principle,
which is `Eat your own dog food`.
This includes not only integrated development + architecture design + environment setup,
but also playing around with others' test environments,
if I break an environment I have to fix it,
and if I don't fix it I get a knife at my back to make me fix it (not really)...

## Solving Problems with Tools

As of now (July 2018),
our company's tech department (all engineering + QA) is fewer than 60 people total,
corresponding to our thousands of annual-fee merchants,
on average each person supports 100 merchants.

> Thinking about it like this, Minjun (the handsome 96er fresh grad) also supports 100 merchants,
> thinking about it makes me a bit excited for him...

This is where the large number of tools we use act as leverage,
amplifying each engineer's productivity.

When I was being interviewed,
a line from Boss Xie made a deep impression on me:
"Problems that can be solved with tools,
we won't have engineers do."

Specifically,
let's look at some steps in a typical development workflow.


### Iteration

Our company has always run agile development,
in the early days we used Trello.
At that time products were few,
and product managers were also few.

Later as teammates gradually increased,
we tried Jira.
Jira's benefit is its powerful configurability,
and its complementary Confluence etc. are complete.
But because configuring is tedious,
and we didn't have time to repeatedly tune it ourselves,
most teammates weren't very used to Jira.

Later up to now we've been using Teambition.
Currently each product line has its own agile board,
one iteration every two weeks, planning meeting on Monday, retrospective meeting next Friday.
Every morning at standup, besides going through yesterday's progress and today's plan,
we mainly bring up some small questions/difficulties in the standup,
a 10-person standup ends in about 10 minutes, super efficient.

When interviewing the other day,
a young lady from VIPshop curiously asked me:
"Are your iterations on a fixed two-week schedule?"
I realized that different teams have different iteration execution details,
so I explained to her our understanding of iteration:
"Iteration is actually like a subway train,
we set it as one train every two weeks,
whatever this iteration can finish, we finish.
The train doesn't wait for people, what doesn't get done can be done in the next iteration."


### VCS

The version control tool we use is privately deployed GitLab EE.
Besides Repository,
we also use its Merge Request/CI/CD/Docker Registry/Wiki features.

For example take our bot KevinBot,
if you want to add a new feature to Kevin the process roughly looks like:

- Fork the project to develop locally
- Push to your own repo, submit a merge request
- Triggers CI checks
  - flake8 checks for syntax issues, like using double quotes, forgetting commas
  - django checks for migration issues
  - Runs all uts to see if unit tests pass
- Beg the code owner to review your code
  - There will be online comments, hard-to-explain things will be explained offline
  - If there are problems they get sent back to be modified, re-push
- approve + merge
- Auto-triggers docker auto-build
- After build completes, auto-triggers deployment, kevin bot deployment complete

![review][review]

In the whole process the contributor needs to fork + coding + merge request,
the code owner needs to review + approve + merge,
the remaining unit tests, image build, version update are all done by a single pipeline~

> So the little bot updated one impractical fun feature after another

![alias][alias]


### Monitoring

Our monitoring system is divided into several parts.
For all monitoring alerts we use email + WeChat bots.
For machine state monitoring we use AWS CloudWatch built into the cloud platform,
for business state and log monitoring we use the entire ELK system,
and for the most direct and practical error monitoring we use Sentry.

For example a year ago there were several deployment nights each week,
everyone would watch Jenkins console log on one side,
and watch Sentry on the other to see if any error logs would pop up.
If there were of course it was fire-line programming!
(So at that time there was this meme of nine cores rubbernecking:

![fire][fire]

Later we finally welcomed real QA teammates,
Sentry is still a very effective debugging tool we use in the test environment,
whether it's an error or warning,
every error on Sentry has a chance of being caught and hung up for hammering.

Once Sentry got a bit slow,
even keenly noticed by Boss Xu as not simple,
which led to a case: [《Case Solved · The Mystery of Sentry》][sentry]


## Autonomous Decision-Making

The various aspects of engineer culture mentioned above,
every excellent team definitely has the same kind of engineer team.
But on one point,
I feel only my company is special.

To quote something Boss La who used to work at AutoNavi said:
"Back at AutoNavi, what I did was assigned to me by my leader.
My leader, what he did was assigned by his leader.
What everyone did and the technology they used was relatively fixed.
But at Zaihui, it's basically however is best.
And honestly, I never imagined work could be this happy!"

Boss La is always so wise (read with sarcasm).

The politics teacher said,
when we answer questions we should use the general-detail-general format for high marks.

It seems one reason engineer culture is so likable,
is that engineers themselves are also very likable.


(End)


[guide]: /assets/pics/engineer/guide.png
[review]: /assets/pics/engineer/review.png
[alias]: /assets/pics/engineer/alias.png
[fire]: /assets/pics/engineer/fire.jpg
[sentry]: /solve-a-sentry-case-en
