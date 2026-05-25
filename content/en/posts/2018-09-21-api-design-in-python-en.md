---
title: "Elegant Python API Design"
date: "2018-09-21 20:57:46"
zhUrl: /api-design-in-python
aliases:
  - /api-design-in-python-en
---

Today doing daily code bullshitting with [@hulucc][hulucc],
talking about principles for picking third-party libraries:
"I actually found I now don't really care how the source code is implemented when picking libraries,
but I really love libraries with super scientific api design."

<!--more-->


## Scientific APIs

What does scientific API design look like roughly?
For example a famous example is the [requests][requests] library.

> Requests is one of the most downloaded Python packages of all time,
> pulling in over 11,000,000 downloads every month.

The way this library's API is used looks roughly like this:

```
>>> response = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> response.status_code
200
>>> response.headers['content-type']
'application/json; charset=utf8'
>>> response.encoding
'utf-8'
>>> response.raise_for_status()
```

All the Python programming language designed here is meaningful human English language,
the `requests` in `requests.get` isn't just a package name,
it's also become part of the code's semantics.
The returned `response` is a typical HTTP protocol object,
any programmer with some understanding of the HTTP protocol,
can basically guess its main attributes and corresponding uses without looking at the docs.
Correspondingly there are also convenient commonly-used methods like `.raise_for_status()` and `.json()`.
This is the feeling scientific APIs give me.

Of course, the library's author (the handsome [Kenneth Reitz][kennethreitz]) is also aware of his code's elegant interface,
his personal signature says so too:

> I wrote @requests: HTTP for Humans.
> The only thing I really care about is interface design.
>   -- Kenneth Reitz


## Unscientific APIs

Most highly-starred open source projects' interfaces are relatively elegant,
so what do unscientific APIs look like roughly?
Uh, in my case, flipping through my code from two or three years ago,
it's full of unscientific API implementations.

When I first encountered `**kwargs`,
I really loved using this syntax,
for example I'd often write this kind of function:

```python
class Record:
    def create(**kwargs):
        now = kwargs.get('now', datetime.datetime.now())
        key = kwargs.get('key')
        value = kwargs.get('value')
        ...
```

The benefit of writing this way is it looks super flexible, satisfying to implement.
If you want to add a parameter later,
often you just need to add a new `kwargs.get` inside `record.create`.
However in most cases, this kind of implementation will just make the parameters implicit:
when you can't remember the params calling `record.create` you have to go into the function to see the implementation;
plus if you misspell `value` as `valeu`,
the function will run normally like in some languages!
Then will error somewhere later,
making it hard to conveniently find the root cause.

Later most of the time I'd write it like this:

```python
class Record:
    def create(now=None, key=None, value=None):
        if now is None:
            now = datetime.datetime.now()
        ...
```

This kind of explicit call mandates parameter correctness,
although the implementation requires writing more parameters,
calling and reading are clearer.

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Later whenever I see `Explicit is better than implicit` from `The Zen of Python` I think of this example.
(About Python interface parameter design, there's a Zhihu article I think speaks very well:
[《Some Design Insights on Python Function Interfaces - Lingjian》][method-signature])


## Examples

`The Zen of Python` has many more gems to mine.
For example one project I'm doing, [hutils][hutils],
the idea is to extract commonly-used functions in the company's various Python Web projects to make a base library,
turns out when writing it 80% of my time is spent thinking about how to make the API more scientific.

For example when writing backend,
often we encounter the situation of needing to convert framework error classes:

```python
def service_call(...):
    try:
        external_service.call()
    except ExternalServiceError as ex:
        log_error(ex)
        raise APIError('Error calling external service')
```

Correspondingly, we'd have a decorator like this to encapsulate error handling:

```python
@contextlib.contextmanager
def catches(*exceptions,
            raise_to: BaseException = None,
            raise_from: Callable[[Exception], BaseException] = None,
            log=False,
            ignore=False):
    try:
        yield
    except exceptions as ex:
        if log:
            log_error(ex)
        if not ignore:
            if raise_from:
                raise raise_from(ex)
            else:
                raise raise_to  # pylint: disable=raising-bad-type
```

With this encapsulated decorator,
simple error conversion can be separated from business code:

```python
@catches(ExternalServiceError, raise_to=APIError('Error calling external service'), log=True)
def service_call(...):
    external_service.call()
```

But this kind of decorator implementation will get hammered back at Code Review stage by iron-blooded teammates like [@hulucc][hulucc],
this API implementation has several unscientific places:
* `raise_to` and `raise_from` have overlap,
  and if the caller is careless it'll trigger `raise None`,
  even `pylint` noticed.
  Should use type checking to merge parameters.
* This kind of error conversion loses the original error class's stack trace info.
  Should use `raise ... from ...` syntax to preserve stack trace info.
* `transfer`/`ignore`/`retry` are actually relatively independent logic,
  mixed handling is of course possible,
  but the best case is splitting logic, handling independently.

After a round of discussion,
plus conveniently supporting the shortcut `catches(Exception, raises=raise_api_error)` syntax,
the decorator implementation changed to look like this.

```python
@contextlib.contextmanager
def catches(*exceptions, raises: Union[BaseException, Callable[[Exception], BaseException]], log=False):
    exceptions = exceptions or (Exception,)
    try:
        yield
    except exceptions as ex:
        if callable(raises):
            raises = raises(ex)
        if log:
            log_error(__name__, raises)
        raise raises from ex
```

Feels more elegant doesn't it.


## Closing

Because Python's syntax is extremely flexible,
interface design actually depends entirely on the programmer's design level.
But often the scientific and elegant implementation, like `There should be one-- and preferably only one --obvious way to do it` says,
is one in ten thousand.

Not only realize the functionality,
also be elegant, not dirty.
Looks like writing programs really requires thinking a lot,
no wonder programmers have less hair :)

(End)

[hulucc]: https://github.com/hulucc
[requests]: https://github.com/requests/requests
[kennethreitz]: https://github.com/kennethreitz
[method-signature]: https://zhuanlan.zhihu.com/p/25017419
[hutils]: https://github.com/zaihui/hutils
