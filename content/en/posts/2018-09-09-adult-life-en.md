---
layout: post
title: "Three Years After Graduation Report"
date: '2018-09-09 19:46:37'
zhUrl: /adult-life
aliases:
  - /adult-life-en
---

The other day I saw a question on Zhihu,
called [《What are the differences between three years of grad school and three years of work》](https://www.zhihu.com/question/31907973).
My thoughts were suddenly awakened:
oh right, it's already been three years since I graduated.

<!--more-->

> Note, this article is 10,000 characters, might take half an hour to read?

My work habits and little Mia's are pretty similar,
the other day chatting we calculated:
normal nine-to-six with weekends off,
that's 40 hours a week;
but because the two of us basically still look at work-related stuff after getting off,
on average workdays add 2 hours of work,
and on weekends there's still a day spent on profession-related stuff,
so all told you could say we work 60 hours a week.
Heh. Meaning we work two years and have four years of experience.
Made bank.

Of course, this work experience buff is just for fun.
Seriously, if I'm calculating work experience,
I'd rather start from July 7, 2014,
that's the First Day (so many modifiers) of my first job as an intern.


## Internship

### Commute

![pic1][pic1]

Our university's setup is that senior year is for internship,
and because my hard study grades weren't great,
couldn't grind for grad school and also wanted to apply learning sooner,
so I went with the plan to find an internship,
then convert to a full-time job after graduation.

At that time [QAD (an American-funded multinational software company)](lazy-coding-thinking-en) came to our school for campus recruitment,
so I went and interviewed.
The process was written test + group interview + individual interview,
extremely similar to NIMO (Shanghai Jiao Tong University Network Management Department)'s interview process.

~~So I skillfully passed. (Not really)~~
I actually filled in my name and phone and froze,
because the third blank was called "target position,"
with SE, QA, and BA as checkbox options.
I raised my hand and asked the HR Sister Gloria in charge of distributing papers,
Gloria told me as a Software School student just fill in SE,
the other two don't need to fill in, so I obediently filled in SE.

Later I learned filling in position is because of the company's division of labor:

- QAD has R&D centers all over the world, China's R&D center is in Shanghai.
- Of course, Shanghai actually has not just R&D, but also Sales, After-sales, etc.
- The R&D department's formal name is Research and Development, written R&D, read R and D.
- R&D is split into many small teams by business team, my team is Release Foundation, which roughly means basic components team in Chinese, with about 20 people at peak.
- Each team in R&D has independent combat capability, from tech choice, frontend, backend to testing, all done within the team.
- So our team actually only had two positions: SE (developer) and QA (tester), BA is a position set up only by more frontline business-related dev teams.

After interning for a month I finally figured out the company's division of labor,
I was quite excited, because I thought this was the company's lifeblood.
A company can grow to multinational scale,
so the org structure must be scientific!
Learned it, one day when I open a multinational company,
I'll do it this way too!
I happily thought.

![pic2][pic2]

Later I learned there are also systems divided by job function.
But I always continued the routine when introducing the company to others of
first introducing the business scope,
then the company structure,
finally the team's relevant tech content.
Because I really go for this routine :)


### Commute

But one thing that bothered me during the internship was,
the company was at Lujiazui Software Park in Pudong,
school was in Minhang.
Counting walking, one way took two hours every day,
back and forth four hours gone.

Some classmates chose to rent a room near the company.
But I looked at my intern salary,
felt paying to come to work was a bit of a loss,
so I and Li Chao who interned at the same company agreed to get up at 06:45 every day,
leave at 06:50 to make it to the company before 09:00.

When the seniors at the company found out we'd chosen a 4-hour daily commute,
they joked with us: "You guys can't keep this up, you'll definitely rent a room within two months, or quit..."
Thanks to this reverse flag,
the whole year of internship, even when squashed against the doors of Line 5,
I persisted with 4 hours of subway round trip.
And I even finished anime I wanted to watch and books I wanted to read on the subway.

![pic3][pic3]

《Code Complete》both Chinese and English versions I finished reading on the subway,
even today I clearly remember,
surrounded by working corporate slaves, I could only hold up my phone and lift my head to read books,
deeply shocked by a piece of code malpractice described in the book.


### Newbie

During the interview, I asked Joe what the dev environment was like for the team?
Joe said: "Our dev languages are Perl and PHP, normally we develop on Linux with Vim. Have you used these?"
I awkwardly scratched my head: "Perl/PHP I've only heard of, Linux and Vim I've only touched in class, don't really know."
Joe consoled: "It's fine, you'll get used to it by writing. Each of us has a Mentor."

Oh 0w0, there's a Mentor, then I'm at ease, I thought.
At Network Management we also had this Mentor master-apprentice system,
a clear go-to person for help is huge psychological comfort to a newbie,
of course in the end the practice still depends on yourself.

On day one I arrived an hour early, came at 8.
Turned out the front desk MM wasn't at work yet,
I stood outside waiting ten minutes until the cleaning auntie came to open the door for me...
After thanking her I found the desk with my badge,
then discovered behind me was already sitting an engineer who looked nearly 30.
Looked at his badge, it said Justin Zhang,
I curiously asked him: "Justin hello, I'm Lirian, Chinese name Su Ziyue. Are you my Mentor?"
Justin thoughtfully answered: "Kind of... I guess?"
(Actually yes)

After finishing the company's online courses for new hires on anti-corruption, anti-harassment, etc. (yes...)
I rubbed my fists eagerly and asked Justin if there was anything I could do,
Justin said: "Go learn about Vim."
Emmmmmm, before I could understand this task,
Justin opened up a Vim page:
"Let me show you how we normally read and write code."
Then Justin showed me various features like Nerdtree/CTags,
and helped me install his config [(schnell18/dotvim)](https://github.com/schnell18/dotvim)...

So for the next few days, besides the company's Newbie Village Quest,
I also happily looked at Vim-related materials everywhere (yeah, I hadn't even run vimtutor.)
The more I looked the more I felt about this Vim thing,
just like Justin said:
"Vim is a very powerful tool, you might take a month to learn Vim, but you can use it for a lifetime."
At first when I wasn't proficient,
I'd often do jjjjjjjjj or i→→→→→→→→→ kind of operations,
but since Justin would stand behind me from time to time to Review code,
under pressure and self-respect, I switched to }} or f2$ kind of operations...

My Mentor Justin was an engineer with extremely strong code OCD.
At that time our project management used git + gitolite,
every time we submitted code,
Justin would use git diff + vimdiff to line-by-line review our code.
Sometimes when typing commands on the command line,
Justin would also stand behind me explaining the commands I should type.
And from this I learned from Justin the English ways to say various symbols,
like dash, quote, etc...
(Though at first every time Justin said "git rev dash list" I'd freeze and take half a day to react)

![pic4][pic4]


### Worries

Gradually, I got used to using Putty + Vagrant to set up dev environment,
using Vim + Git to edit and submit code,
using Perl to solve business problems.
But as I learned more,
I started worrying I couldn't become outstanding.

Around then on the commute I read quite a few tech articles/books,
two thoughts particularly struck me,
one came from 《Code Complete》:

> About programmer experience:
>
> People put absurd emphasis on how many years of experience a programmer has.
> "We need programmers with 5+ years of C programming experience" is a stupid thing to say.
> If a programmer hasn't learned C well after the first year or two, three more years are meaningless.
> This kind of "experience" has little to do with work efficiency.

When I saw this line at the time,
I thought back on my own two weeks of work,
and discovered I was actually just purely emitting my existing knowledge!
I didn't want after three years of work,
to become the kind of person with effectively one year of work experience repeated twice.

There's another one I figured out on the way to work.

I get very tired playing competitive games, because I really want to win.
I want to win not because I enjoy the feeling of victory,
but because I fear the frustration of unrewarded effort, of unequal pay-off.
So a lot of the time I don't go all out doing things,
because that way even if my team loses,
I have a reason to think: "not my fault, I only put in 80% effort."

But I, not yet graduated, also thought,
if I really chose a life path where I don't go all out and enjoy myself,
then when I look back, how could I not regret wasting my youth, or feel ashamed of accomplishing nothing?

So in my own psychological hint segment,
I added the chicken soup line "people smarter than you are also harder-working than you."

![pic5][pic5]


## Going Full-time

### Real-world Problems

![pic6][pic6]

After interning for a year,
I smoothly converted to full-time.
I ran into a small puzzle: salary.
Of course, here "puzzle" doesn't mean the company gave me trouble or I was unsatisfied or anything.
First I actually don't care much about fresh-grad salary, because I always feel one day the value I create will exceed my one year of post-graduation salary;
secondly the company also doesn't lowball any employee's salary, all offers are at a unified level.

The salary puzzle was that I vaguely felt it wasn't enough.
In university my monthly living expenses were about 1000 RMB or so,
very sufficient.
After graduation if I wanted to rent a one-bedroom with kitchen near the company,
it'd cost about 3500 a month, after deducting this much rent and other miscellaneous I'd have just over 2000 left a month.

Of course, a normal social adult definitely wouldn't spend such a portion on rent.
But I thought I don't smoke don't drink, don't buy clothes don't eat fancy meals don't socialize,
home time is either reading tech blogs or playing games,
and my girlfriend isn't materialistic,
can't give expensive gifts so give thoughtful ones...
By the principle of being thrifty it's about enough?
So I resolutely spent half of my monthly disposable income on rent...

Later about a year after graduation,
my dad asked me: "
Your mom after graduation lived at your grandfather's place,
that year of post-grad work, basically saved all the money,
later when we got married your grandfather even gave your mom all the saved salary.
You've been interning plus working for two years, you've saved a bit of money, right?"
Me: "...saved saved... oh I need to do laundry, gotta go, 886"

That year my younger brother finished college entrance exam to go to Wuhan for university,
I planned to give him the newest iPhone.
When I went to university,
my uncle gave me a laptop (Lenovo Y470),
after getting the gift, my heart was filled with the disposable freedom of joy,
I posted on QQ Zone "I have my own computer! So happy I'm about to cry!"
After my mom saw, she fiercely criticized me: "Getting a computer makes you this unpromising? Delete that status quickly."
Me: "..."
So when my brother went to university,
I decided to also let him experience this disposable freedom of joy :)

After seriously calculating the price of the newest iPhone,
and my financial situation over several months,
I shamelessly dragged my girlfriend to eat at the canteen for the public for two consecutive months,
and ordered only one meat dish, then mooched off girlfriend's vegetables.
After eating at the public canteen for two months,
I successfully fell in love with the dish of cartilage.
For real, cartilage is genuinely delicious.


### Last Day

From internship to going full-time there's another thing that left a deep impression on me,
which was Justin's resignation to go to Ping An Good Doctor.

Foreign companies have a ceremonial Last Day,
on this day you might walk through a Checklist one by one,
then chat with normally-collaborating coworkers about work or life stuff,
then send an email with your personal contact info to everyone in Shanghai and cc'd to various foreign coworkers you regularly contact,
finally after the whole Checklist is done you leave work early,
ending your several-year employee career at this company, starting the next phase of work and life.

When I read literary works,
I can't stand two kinds of plots:
one is the late years of a beauty or hero;
the other is hard-to-say goodbyes.

Even today I can still recall Justin's Last Day,
he arrived nearly an hour early as usual in the morning,
also handled things normally,
at noon the team coworkers normally went downstairs for a farewell meal,
during which everyone chatted about the past and the future.
Around 4pm,
Justin put on his backpack,
not very loudly said: "I'm off."
Then everyone stood up to say goodbye to Justin,
Justin paused in the aisle,
the smile staying on his face the whole time,
until he turned and left.
I melancholically sighed: "If Justin had stood for two more minutes I think I would've cried..."
Suddenly everyone couldn't help laughing,
scattering that gloomy parting atmosphere.

![pic7][pic7]

Actually most people don't do one job their whole life,
same in 21st-century Shanghai.
So actually everyone in the workplace,
also clearly knows one day, the coworker next to them,
might choose to leave for all sorts of reasons.
Everyone holds blessings for resigning coworkers,
after all the world is big, life is bigger,
there's always chance to meet again.

Later in yellow peach season after Justin left,
we still successfully got delicious yellow peaches as usual through Justin's channel :)


### Main Job

After Justin left,
I gradually took over the entire project.
With new campus recruitment in the new year,
new interns came to the company,
I became a diligent older brother (@Ray)'s Mentor,
and like Justin taught me back then I taught him Vim, reviewed his code.

In the process of communicating with him,
I hazily saw the shadow of myself a year ago,
indirectly my self-understanding deepened.
I seemed to vaguely grasp concepts like "how to ask others for help to learn faster,"
"how to exercise autonomy at work appropriately."

In specific business development,
because team staffing was always quite scientific,
and everyone was quite efficient,
we finished developing the Perl version two months earlier than expected.
And here I happily found something I could write on my resume.

I sensed early on that the project would finish early,
so a thought always wavered in my heart:
"Could we rewrite this Perl command-line tool in Java?"

We used Perl at the time because the first version of this command-line tool used Perl,
plus Perl itself is very suitable for command-line text processing,
and the developers in our team were very skilled in Perl.
But Perl's drawbacks were also obvious:
it's not a mainstream language, hard to recruit experienced people,
newbies easily increase resignation risk because they can't see a future in learning this,
and Perl's deployment is heavily related to the system,
we even stepped on a pit where prelink conflicted with Perl.
In comparison, Java might be weaker in text processing,
but is much easier for recruiting and deployment.

But doing engineering projects, a big issue you encounter is cost-effectiveness.
Our Perl version of the project took nearly a year to write,
including unit tests the code volume was something like 50k lines,
launch time was still two months away,
looks unfeasible.
But we made it happen anyway.

The whole thing was mainly because of my Manager: Joe's determination.
(Same person who interviewed me during the internship!)
I'd talked with Joe about the Perl vs Java topic,
he first strongly agreed with my view,
and told me about engineering project issues he could figure out solutions to.

So I decided to first try in my own spare time to rewrite the whole project in Java,
even if it ended up unused at least it'd be my Java practice.
Back then evenings after eating at the public canteen plus walking girlfriend to the subway,
I'd walk home, take a shower then rush back to the company to code.
Because I was familiar with the logic and it was just pure refactoring, plus could abstract classes and streamline code,
in just over a month I'd implemented the skeleton of the entire project plus basic unit tests.

![pic8][pic8]

Later one day Joe saw the skeleton was done,
so he excitedly pulled me into a serious meeting,
calculated the input-output ratio,
and summarized 8 English reasons "why should refactor from Perl to Java."
Finally Joe, after coordinating and communicating with all parties,
not only got the plan to rewrite in Java approved,
we also got two more months of development time! (negotiated extension)
Then Joe pulled several teammates from other projects in the team to develop together to the final launch :)


### Foreign Teammates

Because our command-line tool was ultimately deployed for use by various foreign programmers,
my organizational task before launch was to liaise with foreign teammates.
At the peak of liaising I had voice meetings online from 09:00 to 11:00 every morning for two consecutive weeks with foreign coworker (@Mythily),
she'd share her screen,
and I'd watch her Terminal as I explained various commands or docs to her.

At this point I suddenly understood why Justin would say to me "git rev dash list" all in English command-line pronunciation,
because I could only also say it this way to Mythily,
I couldn't very well tell a foreigner "ls space -l enter"...

Unfortunately due to insufficient skill,
much of the time I could only say:
"emmm, let me send you the command line in chat"
"yeah yeah yeah, space"
"no no no, dash, yeah git dash"

But fortunately Mythily was an Indian coworker,
both of us had super strong understanding of accented English,
communication was very smooth.

Sometimes after finishing the day's tasks we'd chat a bit,
once she happily told me about an Indian traditional holiday called Diwali,
and invited me to come visit India during Diwali sometime.
I also politely invited her to visit China during Spring Festival,
showing certain great-nation manner.


### Spare-time Tech

I talked a lot about work stuff,
on one hand because I really was at work working,
off-work thinking,
even before sleeping I was thinking how to write code more elegantly;
on the other hand was being really poor,
my normal pastime was watching YYF or browsing tech blogs.

For tech blogs there's a site I really like, called [coolshell](https://coolshell.cn/haoel).
The blog owner Chen Hao's state is the state I idealize:
working on the tech frontline for over a decade straight,
with original and outstanding understandings of language, tools, architecture, culture,
having uncommon influence over ordinary programmers, guiding them to become excellent,
and still struggling on the frontline today.

Inspired by blogs like this,
I also decided to [start my own blog](/why-im-blogging-en).
But at first I didn't have much to write,
so I [listed some bug-solving workflows](/vagrant-up-but-mount-no-device-en)...

In the process of writing blogs, I discovered this is a great path to progress:
writing blogs not only urges me to "make new daily, daily make new, again make new,"
but also constantly reminds me to look at how others find problems, understand problems, solve problems.
At least this won't make me too disconnected from the industry,
might also avoid the issue of one year experience repeated N years.


## Change

### Setback

One day jogging by the Huangpu River,
I suddenly got a call from Justin.
After catching up on recent state,
Justin invited me to interview at his current company Ping An Good Doctor.
I thought about it,
felt that trying out an internet company wasn't bad,
and Justin had already gone there as scout,
the company should be good,
so I happily went to interview.

Then I bombed...

I interviewed for Java backend,
the interviewer asked me some pretty normal Spring framework / Java thread pool / GC / process analysis stuff,
and I couldn't answer any of it.
The interviewer was also helpless,
he asked me: "Then what do you feel you're good at?"
I weakly answered: "Vim?"
The interviewer thought, asked me: "What's the shortcut to move the cursor to the middle of the screen?"
I froze, then answered: "I don't know..."
(Later I looked it up and learned it's `M`, I really had never used it...)

Later when I came back I seriously reviewed,
felt the main issues in my interview were:
one is I really was inadequate, lots of things I didn't know, hadn't learned hadn't practiced;
two is overconfident without preparation, some routine questions can be studied beforehand;
three is not realizing the Java tech stack for writing command-line is different from writing backend.
Plus the interview didn't ask algorithm questions,
so I couldn't get bonus points through hard knowledge...

But in the end they still gave me an offer,
just that the salary was awkward,
it was an offer with no raise from my current job.
Asked HR, they said it's because I'm not yet a year out of school,
so I'm counted as a fresh grad.
I was reluctant, but very understanding.
Although I'd never interviewed others, if I were to interview someone who couldn't answer a single question,
being able to give an offer is already giving the referrer huge face.

Facing this offer, I started agonizing.
In theory level-pay job-hopping isn't scientific,
but this is an internet company, hot industry;
and there's the known leg-hugger Justin,
following him to learn should be fine, right?
But leaving QAD like this still wasn't quite right,
the project at the time wasn't fully done,
and not counting internship I hadn't even worked a year,
the teammates in the team were actually all very nice...
emmm agonizing.

Generally in hero movies, when down a senior steps out to give guidance.
So I tried private messaging Hairy Ear Mouse on Weibo,
and got his reply.

![pic9][pic9]

Then that evening I had a nearly two-hour phone call with Brother Hao.
On the phone, he talked about his three different experiences at Amazon, Alibaba, and his own startup,
as well as similar worries he had when young,
and even talked about his method of thinking when writing code to solve problems and his corresponding life view.
Brother Hao's advice was concrete,
but what I heard that night was a very idealistic two characters: vision.

In the human lifespan of nearly a century,
as an engineer you'll solve countless problems,
so sometimes the problem in front of you, viewed more long-term, will have a better solution.
After hanging up the phone,
a folk saying came to my heart: "Don't look down on a poor young man."
So in the end after pre-communicating with Justin,
I politely declined the offer with HR Sister.

(Then every day I gave myself two liters of chicken blood!)

![pic10][pic10]

![pic11][pic11]

![pic12][pic12]


### An Ordinary Day

Later one day, Baixing.com's HR (@PP) found my email from my GitHub,
sent an email asking for my WeChat,
then scheduled a morning interview.
Pinduoduo bro FM also asked if I wanted to interview there,
so I also conveniently scheduled an interview for the afternoon of the same day.

In the morning I went to Haoran to interview at Baixing,
at noon I found ldsink to eat noodles at the school entrance,
after eating ldsink also took me along to tour his company.
Just walking up to Kaili Building, a coworker greeted ldsink,
I curiously asked: "Who's this?"
ldsink said it was a sales coworker.
I felt very surprised: "You guys are this warm? Devs and sales are this close?"

After touring the company,
felt this small company really was quite obviously small,
not many people and decor was kind of bare,
but I met Eason Jiang's former roommate,
a thin guy from Tongji University,
the world is so small.

In the evening after finishing interviewing at Pinduoduo,
ate a bowl of noodles with FM and FHN at a noodle shop near the company,
after eating it was past 7pm preparing to head home.
Suddenly on WeChat ldsink asked if I'd eaten,
he said the coworkers at the company hadn't gotten off yet,
and saved me a boxed meal, inviting me to go eat together...
I thought, how could a company box meal compare to the noodle shop's noodles outside,
but still ran over.

Turns out I went to interview!
The resume I'd sent to Zhou Cheng two weeks ago was all printed out...
The first interviewer looked like a successful backend,
did two algorithm questions and chatted a bit then done;
the second interviewer was the Tongji thin guy from above,
didn't ask anything, pure bullshitting, I showed him my frontend toy projects from spare time,
he introduced product-related stuff to me then done...
Then I sat and waited a bit,
the company's CEO actually specially came back from outside to see me,
then he asked about my tech ideals,
I told him a bit then we started licking each other (with body language too...)

After getting home I called my girlfriend to tell her about the day's interviews,
and conjecturally told her: "If they all give me offers, I'd probably go to Zaihui, this company gives me a really comfortable feeling."

Later I really did go to Zaihui,
and worked with a bunch of really strong teammates.

![pic13][pic13]

> When you grow old and look back on life,
> you'll find,
> when you went abroad to study,
> when you decided on your first profession,
> when you chose a partner and fell in love,
> when you got married, were actually all huge changes of fate.
>
> But at the time standing at life's three-way fork, seeing winds and clouds and a thousand sails,
> the day you made your choice, on the diary, was rather dull and ordinary,
> at the time you thought it was the most ordinary day of life.


## A New Beginning

![pic14][pic14]

### Freedom

At the end of November 2016, I came from a foreign company to a Series A internet company.
After gradually getting familiar with the business and tech,
I suddenly realized many things I'd taken for granted were actually different at every company.
What touched me most was company systems.

For example work scope.

At foreign companies it was actually fixed quantity and timing.
What I did was assigned by the team, faster or slower it was the same amount,
team stuff was distributed by department to each Manager,
basically also reasonably and relatively fixedly distributed.
But at internet companies work is entirely based on initiative.
Not only if you do it fast you have more to do (of course doing slow means bad performance review),
but many things can be cut!
Very likely everyone discusses and discovers a more scientific way to achieve it, the whole thing doesn't need to be done.

The most direct feeling is that coworkers around have super high ownership.
Because what they do they participated in thinking and discussing,
so everyone's enthusiasm is very high,
first time I discovered so many people work even at home... and they're actually all at my company???

There's also new-hire training.

QAD has over a month of new-hire training,
during which besides business training, there are also English email, work etiquette etc. training.
Zaihui tech department's new-hire training was just one day,
initially there wasn't even a Mentor system,
just relied on hired big shots being able to save themselves and figure things out to support it.
But later gradually there's a Buddy (Mentor) system,
and a complete series of Newbie Village Quests to familiarize with the business.

And there's recruiting.

At QAD when recruiting I wasn't involved,
not clear on specifics,
but basically the Manager decided.
And in my second week at Zaihui I was already being taken to interviews.
I quickly discovered compared to the "picking subordinate" feel of interviews,
Zaihui's interviews actually had us "picking teammates."
The CEO/CTO's final interview is quality control,
the earlier coworker interviews are actually crucial,
interviewing candidates from different angles is the only way to guarantee always hiring Class A people.

Of course, our offer rate is only 4% which has been criticized many times by HR MMs,
but conversely, our resignation rate is also only 0%.

![pic15][pic15]


### Tech-related

Although I lightly described the tech earlier,
actually before coming to Zaihui I'd never touched proper Python Web backend development.
How inadequate was I, roughly?
Well, if Jinming (the seemingly successful backend mentioned above) had asked me these questions at interview:
What does each HTTP request method mean? / What is virtualenv for? / What is uwsgi for?
I couldn't have answered a single one...

Inadequate, gotta admit.
So back then every day I'd come home and tell my girlfriend:
"I'm so inadequate, my teammates are so strong,
but I'm really happy, feel like I can learn anything,
and they write code after work too,
feel like I've found my own kind, but feel like I can never catch up to them"

But I quickly discovered the binding immortal rope was no longer there:
once I joined I immediately had permissions for all sorts of test environments.
Don't understand uwsgi config? Then go play around in the test environment.
Broke something because you didn't understand? It's fine, the frontend daddy will quickly come pound on you and force-make you understand.
Hazily it felt like first playing dota, picking Sniper and quickly learning all heroes' skills.

That period I basically also wrote company-related code on weekends.
Because on weekends there's no problem of test environments getting broken or conflicting,
I could try things wildly, then learn all sorts of lessons.

After this experience,
I'm very certain of one fact:
empower programmers as much as possible,
excellent people will take off like Rock Lee unbuckled his weights.


### Life-related

Work content at Zaihui I actually wrote many other articles to talk about, like:
[《My Work》](/my-work-en)
[《Why I Like Engineer Culture》](/engineer-culture-en)
won't elaborate too much.

The job-change node has another meaning for me,
which is I rented an apartment with my girlfriend.

My parents are both teachers,
as a child after school at home I'd hear them chatting about various students, lesson prep, subject groups, exams,
they were not only warm and loving spouses in life,
but also listened to each other and gave advice in work,
which I really longed for.
So what makes me happiest about renting with my girlfriend,
is actually being able to collapse after getting home from work,
either listen to girlfriend talk about HR's career and various crap,
or talk to girlfriend about engineer's development planning and various crap.

But thinking about it,
about girlfriend I've also specially written [《My Girlfriend Little Mia》](/my-little-mia-en),
not much special to say.

Sigh, the troubles of high output.


## Closing Words

Sitting in front of the computer,
seriously thinking about all the various things done in three years since graduation,
what touched me most isn't anything substantive,
but the progress of my thinking.

Being kind to people,
using control-variable method to study problems,
considering things from others' perspectives — these universal things learned since childhood are actually very correct and useful methodologies.

Hope this world, under your and my effort,
becomes more and more beautiful :)

![pic16][pic16]


[pic1]: /assets/pics/adult/2014-07-07.png
[pic2]: /assets/pics/adult/2014-07-07-2.png
[pic3]: /assets/pics/adult/2014-07-29.png
[pic4]: /assets/pics/adult/2014-08-27.png
[pic5]: /assets/pics/adult/2015-01-27.png
[pic6]: /assets/pics/adult/2015-07-05.png
[pic7]: /assets/pics/adult/2015-04-30.png
[pic8]: /assets/pics/adult/2015-11-12.png
[pic9]: /assets/pics/adult/2016-03-14.png
[pic10]: /assets/pics/adult/2016-06-26.png
[pic11]: /assets/pics/adult/2016-07-04.png
[pic12]: /assets/pics/adult/2016-07-11.png
[pic13]: /assets/pics/adult/2016-12-13.png
[pic14]: /assets/pics/adult/2016-11-25.png
[pic15]: /assets/pics/adult/2017-03-21.png
[pic16]: /assets/pics/adult/2018-01-01.jpg
