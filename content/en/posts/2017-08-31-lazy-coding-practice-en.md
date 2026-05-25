---
title: "How to Be Lazy When Writing Code? Practice More"
date: "2017-08-31 20:25:12"
zhUrl: /lazy-coding-practice
aliases:
  - /lazy-coding-practice-en
---

Compared to "a language",
"a programming language" is more often "a convention".
(Of course, "language" itself is "convention".)

<!--more-->

![standards][xkcd-standards]

[Last time we talked about wanting to be lazy when writing code][thinking],
**figuring things out, thinking clearly before writing** is one way to address the root.
But mortals' (no typo) requirements are never the main point,
to be lazy when writing programs,
ultimately you still slack on the code itself.

## Best Practice

Foreign programmers love muttering a term,
called `Best Practice`.
For example how `JSON` should be handled in `Java`,
you can search `Java JSON Best Practice`;
for example I know nothing about databases,
but I want to learn,
I can search `Database Best Practice`;
for example I'm the client,
I don't know what I want myself,
I can also search `Requirements Best Practice`.

This kind of English term generally has a direct Chinese translation,
called `最佳实践`,
which sounds super stupid.
But it's very useful for giving examples.

When I joined [Zaihui][zaihui],
I'd only written a bit of `Python`,
my coding habits were not adding `encoding`,
not knowing `from __future__`,
writing `print` without parentheses,
all third-party libraries I needed installed in the global `site-packages`.
After coming here [I learned about `virtualenv`][virtualenv].
Later when Boss Zhang was playing with `Lucene` I set up `Gradle` for him,
and explained: "This thing is simple, similar concept to `virtualenv`."
Boss Zhang sighed:
"Actually learning a language starts from these tools,
this way I have a feeling of having gotten started!"

There's also things like [`Go` language's `gofmt` command][gofmt],
this command forces a unified code style adjustment,
can't be configured, can't be customized, indentation uniformly uses Tab.
I was extremely tortured,
but I also recognized the thinking here:
"Language style is just ~~Lin Daiyu~~ Hamlet, a thousand people a thousand faces.
Compared to perfect style, unified style is more scientific."

`Best Practice` is the guide during actual operation,
understanding, mastering, practicing `Best Practice` can ~~write much less code~~ avoid many detours,
solve real problems with elegant methods.


## Elegant Methods

Following the routine, next I should talk about an elegant method.
But your humble brother has no elegant method,
so I can only use myself as a counter-example.

When writing `API`,
you often handle `URL`,
handling `URL` is actually string concatenation.
For example in `Python` converting a `dict` to `query string` format,
I used to write it like this:

``` python3
params = {'name': 'afu', 'action': 'take a plane'}
query_string = '&'.join(['{}={}'.format(k, v) for k, v in params.items()])  # 'name=afu&action=take a plane'
```

At the time I felt good about myself,
thinking `Python` is `Python` after all,
`List Comprehension` is so elegant, so pretty.
However this code not only has a bug,
actually `Python` has a dedicated library `urllib` to handle this kind of problem,
`urllib` has also considered various edge cases (like with illegal characters etc.):

``` python3
# Using Python 3 as example
import urllib

params = {'name': 'afu', 'action': 'take a plane'}
query_string = urllib.parse.urlencode(params)  # 'name=afu&action=take+a+plane'
```

Later I also learned that `urlencode` function's location is different in `Python2` and `Python3`,
typically use [`six`][six] this library to handle compatibility.
The following code doesn't need extra explanation _Using Python 3 as example_:

``` python
import six

params = {'name': 'afu', 'action': 'take a plane'}
query_string = six.moves.urllib.parse.urlencode(params)  # 'name=afu&action=take+a+plane'
```

Even though there are many methods that achieve the same effect,
in software engineering,
people often pin down a `Best Practice` and follow it.
This way not only saves the effort of writing programs,
but also saves the effort of communicating and arguing.
Just as [`Zen of Python`][zen] says:
`There should be one-- and preferably only one --obvious way to do it.`

I used to be very curious why most people use `import datetime`+`datetime.datetime(), datetime.date()` when writing `Python` `datetime` types,
I was perplexed,
isn't `from datetime import datetime, date`+`datetime(), date()` better?
And the subsequent code is shorter.

Later when I read [`Kenneth Reitz`'s `Hitchhiker's Guide to Python`][python-guide] I understood,
`Explicit is better than implicit` is reflected by explicitly specifying the package name,
this way the code's expressiveness is stronger, and more readable.

```
## Very bad

[...]
from modu import *
[...]
x = sqrt(4)  # Is sqrt part of modu? A builtin? Defined above?


## Better

from modu import sqrt
[...]
x = sqrt(4)  # sqrt may be part of modu, if not redefined in between


## Best

import modu
[...]
x = modu.sqrt(4)  # sqrt is visibly part of modu's namespace
```

Since learning this,
I've made up my mind never to use `from datetime import datetime` again.


## Summary

This thing called `Best Practice`,
looks beautiful,
used well can hugely ~~slack off~~ reduce workload.
But it has one important characteristic:
`Best Practice` is never tried out,
but **pondered, learned, selected** to be obtained.
Adding one more `if`, one more machine, hiring one more person, working a bit more overtime,
can probably only solve the immediate problem.
Learning one more bit each day,
that's how, when problems need solving,
facing the multiple pressures of tech, business, deadlines,
you can elegantly use `Best Practice` to solve the problem.

In summary,
to ~~slack~~ ~~do less~~ improve efficiency,
we set down these small goals:

* Learn one more `Best Practice`
* Use it once you learn it, use the elegant method over the stupid one
* Learn through thinking, not entirely through trial-and-error feedback

After all, programming style can't be [shotgun programming][random-programming].


[xkcd-standards]: https://imgs.xkcd.com/comics/standards.png
[thinking]: /lazy-coding-thinking-en
[zaihui]: /my-work-en
[virtualenv]: https://docs.python-guide.org/en/latest/dev/virtualenvs/
[gofmt]: https://blog.golang.org/go-fmt-your-code
[six]: https://pythonhosted.org/six/
[zen]: https://www.python.org/dev/peps/pep-0020/
[python-guide]: docs.python-guide.org/en/latest/
[random-programming]: https://coolshell.cn/articles/2058.html
