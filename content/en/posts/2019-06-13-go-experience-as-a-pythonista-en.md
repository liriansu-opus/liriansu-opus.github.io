---
title: "A Pythonista's Go Journey"
date: "2019-06-13 01:10:49"
zhUrl: /go-experience-as-a-pythonista
aliases:
  - /go-experience-as-a-pythonista-en
---

<!--more-->

# Background

Our team's backend main tech stack is Python,
specific software engineering practice is detailed in the previous article [django/python][se-django].
Since I normally write Python for company business,
and the projects I do are also Python tools,
I've actually been wanting to try Go.

Last week I happened to have time,
so I experienced Go's basic setup,
wrote a small service in Go (WeChat message push).

This article is about a Pythonista's Go newbie path.
Where there are misunderstandings or improper operations,
please instruct me, everyone.


# Syntax

Onboarding a language,
I always habitually open [learn x in y minutes][go-xy] first to go through the syntax.

![go keyword][go-keyword]

Go's special characteristic is it has very few keywords,
which makes Go's syntax easy to memorize.
Overall I think these syntaxes are fun.

## Loops

```go
// Just `for` directly can write infinite loops
for {
    fmt.Println("while true...")
}

// The keyword range is comfortable to use
data := map[string]string{
    "key": "value",
}
for key, value := range data {
    fmt.Println("while true...")
}
```

## Enums

```go
// iota actually made into a keyword
// The two iotas after this can be omitted
const {
    Unknown = iota  // 0
    Male    = iota  // 1
    Female  = iota  // 2
}

// Can also satisfy the preference of defining enums separated by 10
// `iota << 2` defining 1/2/4/8 with bit operations also works
const {
    Unknown = iota * 10  // 0
    Male    = iota * 10  // 10
    Female  = iota * 10  // 20
}
```

## Multi-expression checks

```go
// if statement takes the value of the last expression, so this kind of check is common
if f, err := file.Open(path); err != nil {
    return Response(400, err.Error())
}

// Checking boolean like this is also common
if data, ok := json.Unmarshal(body); !ok {
    return Response(400, "invalid json body")
}
```

## goroutine

```go
// Go's native concurrency is also a very elegant place
func sendTemplate() {
    // This is a time-consuming network request
}

func handleRequest(ctx Context) {
    validate()
    // sendTemplate()
    // ↑ Suppose for speed, we can't synchronously send the template, then with the keyword `go` we can one-click async ↓
    go sendTemplate()
}
```


# Projects

After the first chapter on syntax,
quickly reached the second chapter:
《How to start a project with go》

To write code, first you have to dig out the docs.
So the first stop is [the official site golang.org][golang-org]

Go's official site is actually very friendly,
from the most basic [teaching you how to configure environment, write initial project][golang-code],
to comprehensive long pieces like [Effective Go][golang-effective] — all clearly to the point.

After installing the language environment,
first played with the environment variable `GOPATH`.
But later discovered Go 1.12+ comes with go mod,
just need to briefly understand this concept.
Then let's put this aside,
directly hands-on feel Go's toolchain.

## Toolchain

After Python is installed, it mainly comes with REPL and the package manager pip.
After Go is installed, it comes with a series of tools including fmt/test/vet/mod.

- `go fmt`
  - This is the tool that made the biggest first impression on starting Go
  - It's a code formatting tool that doesn't support configuration, very strict
  - ~~prefer tab over space~~
- `go test`
  - Built-in coverage, very nice to use
- `go vet`
  - Seems to be a built-in linter

When playing with `go test` I discovered it tests against `package`,
and in Go,
the concept of `package` is also very prominent.
For example when calling package methods you have to include the package name,
so best practices also have the rule of "non-overlapping naming."
(For example, methods should be called `xml.Parser` rather than `xml.XMLParser`)

## Writing Business

Since what we wrote was a small service that provides RESTful-style interfaces to the intranet,
then calls WeChat to send message notifications to users,
by Python inertia I wanted to find a `django` + `wechatpy` combo to complete the business in a week.
After brief investigation, chose `gin` + `gorm` two big tools.

Go's third-party libraries feel very direct to me.
Because the way to introduce third-party libraries is `go get -u github.com/gin-gonic/gin`,
directly pulling from GitHub master branch's latest code,
so the whole third-party community feels based on distributed consensus,
only when everyone follows community norms,
will there not be mining code appearing... (although centralized also has mining code)

For documentation, what I actually read in the investigation phase was GitHub README,
GitHub is a frequently visited site,
each library's README is markdown style,
easy to read.
There aren't many places where I really need to look at godoc.
Because what's pulled is source code,
so basically you just read source code directly,
the experience is very similar to Python.

Specific business code I'll skip,
nothing special.


## Deploy

When starting to prepare deployment there were several fun topics.
Like Go's multi-environment configuration.

For Python (Django)'s multi-environment I've always used environment variables + multiple config files,
for Go I looked at the community,
basically similar principle.
Can use environment variables,
or use multiple config files (like yaml),
also one is using command parameters (flag library).
Go community actually highly recommends using flag,
because this way config and code (executable file) merge as one,
more conducive to maintenance.
But ultimately I still chose environment variables + multiple config files...

For project compilation and deployment we use GitLab CI/Docker.
Also the five-step routine of ci-build/test/compile/docker-build/deploy.
What's special in Go is heavily referencing GitHub and Google official code,
domestic pulling speed is relatively slow,
so to speed up builds,
we also set up corresponding acceleration channels to improve speed.
Currently, from code entering main branch,
to auto-deployment takes no more than 3min.


## Performance

Self-written small service deployed,
first thing to do is wrk to test QPS.

Python(Django)'s default is actually sync mode,
basic supported QPS is very low,
we use gevent + uwsgi coroutine mode specially tuned,
a simple interface to get server current time,
on a small broken 1CPU+4G Memory machine,
Python(gevent) QPS can reach about 1000,
while untuned Go(gin) QPS reaches 10000.
Really impressive, Go.


## Community

In the week of playing with Go,
my actual effective coding time wasn't long,
most time was wandering in Go's various community best practice documents.

In my eyes,
besides Go language's many shining points,
Go's whole language community operation is also worth other languages learning from.
For example the official-pushed toolchain mentioned above,
this can effectively raise the floor of all projects.
Python also just released [a formatting tool black][black] last year,
self-claimed to be **the uncompromising code formatter**.
(Python: Don't rush, learning, learning)


# Feelings

Talked so much seemingly neutrally,
actually all are feeling expressions,
let me concentrate and summarize my feelings.

## I'm Inadequate

When writing Go I can directly feel my own inadequacy.
One part is many places I can perceive the possibility of syntax simplification,
but my language expression ability hasn't reached the level of optimization.
Like the [check keyword in Go 2 Draft][go-draft],
I vaguely feel like a similar mechanism could also be implemented based on `panic + recover`,
but when I actually try to write it I can't.
And Python I feel I can totally write as Lisp.

Another part is library usage, or "language ecology."
Whether the standard library normally used,
or various third-party libraries for backend business,
or libraries for engineering use like unit testing, quality control,
I can only do on-site investigation when I encounter them.

Anyway because of lacking basic knowledge,
plus insufficient proficiency,
the process of writing Go always has this magical feeling "I'm so inadequate, I don't even know this."

## I Like Go

Inadequacy didn't stop me from expressing liking :)

Go reveals a very old-school KISS principle,
sometimes it gives me a feeling of being even more simplified than Python.
Like best practices will tell you:
"Don't prematurely split files,
problems solvable with ten files in one directory don't need layering."

Compared with Python,
Go's execution speed reveals an unreasonable kind of fast.
After Python deeply understanding concurrency models,
tuning CPU and language parameters,
result is still an order of magnitude behind Go...
(But on development speed Python is still super fast...)

And,
Go also has cute [Gopher][gopher]~

![gopher-emoji][gopher-emoji]

## Practicing Go

Currently my company backend's main tech stack is Java and Python,
what I mainly write is Python.

From my brief experience,
Go will have great performance on key high-performance services,
but on new business prototypes, Web layer multi-business,
Python's magic-like development speed is still unmatched (hands on hips)

Currently various popular backend frameworks are basically language-independent,
we can choose suitable tech stacks based on different business application scenarios.

Enterprises in choosing tech stacks,
also actually consider other more realistic factors,
like difficulty of recruiting developers,
unification of code base and tech stack,
decoupled management of large teams.
These are also very deep, worth discussing topics.

After writing Go for a week,
I more firmly believe my philosophy:
"Engineers are people who solve problems,
technology is the tool to solve problems.
If software engineering isn't done well, saying tools are hard to use,
is no different from:
stabbing a person to death and saying, it wasn't me, it was the weapon?"


# Follow-up

A week's experience card is a bit too short,
quite unfinished.

If I have time later,
about these Go topics I'll continue researching:

- Production environment service deployment posture.
- Go's service visualization (monitoring, logs, tracing)
- Foundational libraries using black magic to raise language expressiveness
- Cross-language inter-service interaction practice

Welcome exchange,
and please point out and criticize improper places in the article.

(End)


[black]: https://github.com/python/black
[go-draft]: https://go.googlesource.com/proposal/+/master/design/go2draft-error-handling-overview.md
[go-keyword]: /slides/golang-experience/reserved_words.png
[go-xy]: https://learnxinyminutes.com/docs/go/
[golang-code]: https://golang.org/doc/code.html
[golang-effective]: https://golang.org/doc/effective_go.html
[golang-org]: https://golang.org/
[gopher-emoji]: https://github.com/egonelbre/gophers/raw/master/.thumb/icon/emoji-3x.png
[gopher]: https://github.com/egonelbre/gophers
[se-django]: /software-engineering-django-en
