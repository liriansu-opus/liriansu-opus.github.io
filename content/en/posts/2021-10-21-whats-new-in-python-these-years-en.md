---
title: "What's New in Python These Years"
date: 2021-10-21T20:26:58+08:00
zhUrl: /whats-new-in-python-these-years
aliases:
  - /whats-new-in-python-these-years-en
---

Recently we finally upgraded our whole stack to py39/go117.
While everyone was excited about Go's new features,
@ackerr raised a very sharp question:
"What's new in Python's new versions?"

<!--more-->

Yeah,
besides features like f-strings/dataclasses that everyone may already know,
what's actually new in the new versions?

I used to read Dota minor version changelogs with great enjoyment.
Today I decide to chew through the update logs from py36 to py310 ~~(HOHO~~

> All code snippets below can be executed in the latest Python 3.10.0 Repl.


# [What's new in Python 3.6][py36]

Python 3.6 was released on 2016-12-23, officially maintained until 2021-12-23.
Some of the more impactful changes include:

```python3
# In string concatenation, support for f-strings' inline concatenation method
# Finally we can concatenate strings as conveniently as JS
name = "ackerr"
precision = 2
height = 183.2
assert f"{name} is {height:0.{precision}f}cm tall." == "ackerr is 183.20cm tall."

# In constant definitions, you can use underscores to improve readability
number = 3_735_928_559
magic = 0xDEAD_BEEF
assert number == magic

# In variable definitions, type annotations are supported
# Worth noting that Python is still not strongly typed, just written in this __annotations__ variable
import typing
numbers: typing.List[int] = [1,1,4,5,1,4]
complex_data: typing.Dict[int, typing.Set[int]] = {}
assert "complex_data" in __annotations__

# Added enum.auto function, developers no longer have to bother with auto-increment
import enum
class Colors(enum.Enum):
    R = enum.auto()
    G = enum.auto()
    B = enum.auto()

assert Colors.B.value == 3
```

Other one-line updates include:

- Default encoding on Windows is now `utf-8`.
- Modified dict implementation, making its memory usage 25% lower than py35.
- Standard package `asyncio` got a bunch of updates, making it usable.


# [What's new in Python 3.7][py37]

Python 3.7 was released on 2018-06-27, officially maintained until 2023-06-27.
Some of the more impactful changes include:

```python3
# The type system supports lazy evaluation, no need to use a string to refer to yourself anymore
from __future__ import annotations
class QuerySet:
    def filter(self, **params) -> QuerySet:
        """some database filter"""


# Added the dataclass standard package
# Compared to dict argument passing, greatly improves readability
import dataclasses as dc
@dc.dataclass
class Person:
    name: str
    age: int
    gender: str = 'Unknown'

assert Person('me', '24').gender == 'Unknown'
```

Other one-line updates include:

- `async`/`await` are now reserved keywords.
- Added `breakpoint()` system function for debugging.
- You can control package variable access behavior by defining the package's `__getattr__()`.
- Standard package `time` supports nanosecond precision.
- Standard package `asyncio` got a bunch of updates, making it pleasant to use.


# [What's new in Python 3.8][py38]

Python 3.8 was released on 2019-10-14, officially maintained until 2024-10-14.
Some of the more impactful changes include:

```python3
# Added assignment-judgment syntax (also vividly called the walrus operator)
import re
if match := re.search(r"(\d+)%", "Total coverage: 80%"):
    print("Coverage is {match.group(1)}")

# Functions support using `/` to restrict non-keyword arguments
def calculate_data_length(data, /):
    pass

# Officially noted that in this case `calculate_data_length(data=data)` is clearly less readable, you can ban it when defining the function
# Plus this syntax avoids `**kwargs` argument-passing conflicts
def get_values(data, /, **kwargs):
    print(data, kwargs)

get_values({}, data='some_data')

# f-strings support self-explanatory syntax
name = "ackerr"
assert f"Debug: {name=}" == "Debug: name='ackerr'"

# Added `functools.cached_property` method, supports property caching
import functools
class DB:
    @functools.cached_property
    def connection(self):
        print(1)

db = DB()
assert db.connection == None
assert db.connection == None
```

Other one-line updates include:

- `continue` is no longer allowed in `finally` statements.
- Added `math.dist()` method for calculating Euclidean distance.
- Added `typing.TypedDict` supporting mixed types.
- Standard package `asyncio` got a bunch of updates, making it stable.
- In the official benchmark, overall performance improved 5%~20% compared to py37.


# [What's new in Python 3.9][py39]

Python 3.9 was released on 2020-10-05, officially maintained until 2025-10-05.
Some of the more impactful changes include:

```python3
# dict supports the union operator `|`
x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
assert x | y == {"a": 1, "b": 3, "c": 4}
assert y | x == {"a": 1, "b": 2, "c": 4}

# Support for native types like `list`/`dict`/`set` as type annotations
def occurance(names: list[str]) -> dict[str, int]:
    return {name: names.count(name) for name in names}
```

Other one-line updates include:

- Compiler changed from LL-based to PEG-based, to enable more powerful language features in the future.
- Added `str.removeprefix()`/`str.removesuffix()` methods.
- `hashlib` supports `SHA3`/`SHAKE` calculation.
- Non-Windows platforms no longer support building `bdist_wininst` (so many third-party libraries didn't update in time).
- In the official benchmark, overall performance shows no improvement compared to py37.


# [What's new in Python 3.10][py310]

Python 3.10 was released on 2021-10-04, officially maintained until 2026-10-04.
Some of the more impactful changes include:

```python3
# Added match+case syntax similar to switch+case
def check(status_code: int, message: str):
    match status_code:
        case 200 if message:
            return message
        case 200:
            return "ok"
        case 400:
            return "bad request"
        case 500 | 502 | 503:
            return "something wrong"
        case _:
            return "not implemented"

# `typing.Union` can be written more elegantly as `|`
def add_all(*numbers: int | float) -> int | float:
    return sum(numbers)

assert isinstance(42, int | float)

# `dataclass` supports keyword-only mode
import dataclasses as dc
@dc.dataclass(kw_only=True)
class Person:
    name: str
    age: int
    gender: str = 'Unknown'
```

Other one-line updates include:

- Optimized Python's various built-in error messages.
- Added `zip(*args, strict=True)` to force-check equal-length arguments.
- Optimized `str()`/`bytes()` performance, 40% faster in daily cases.


# Conclusion

You can see that Python, as a "stepping into adulthood" programming language,
hasn't had updates as exciting as Golang's generics or error handling in these years.
But overall the language iteration is also based on Python Zen's small-step-quick-run.

For developers, as long as third-party dependencies allow,
keeping the latest environment isn't very hard.

The features the author cares about are just a subset of the language standard.
Readers can also find more detailed and more practical changelogs on the official site.

Next time (if there is one) might bring the go115-go117 changelog.
See you then :)

(end)


[py36]: https://docs.python.org/3/whatsnew/3.6.html
[py37]: https://docs.python.org/3/whatsnew/3.7.html
[py38]: https://docs.python.org/3/whatsnew/3.8.html
[py39]: https://docs.python.org/3/whatsnew/3.9.html
[py310]: https://docs.python.org/3/whatsnew/3.10.html
