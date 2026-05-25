---
title: "How to Count File Lines in Windows Command Line"
date: "2016-04-15 22:13:15"
zhUrl: /how-to-calculate-file-lines-in-windows
aliases:
  - /how-to-calculate-file-lines-in-windows-en
---

Today I needed to count file lines, but I happened to not have a Linux environment on hand.

<!--more-->

## Counting Code Lines on Linux

On Linux this is a very simple thing:

```bash
    find . -name "*.py" | wc -l
```

This line can easily count the lines of all py-suffixed files in the current directory.


## Counting Code Lines on Windows

This time we shouldn't use cmd but PowerShell instead.

[Powershell][powershell] is an automation configuration framework developed by Windows based on .NET.
(Basically it's the new command line.)

Then we can type:

```powershell
    dir .\ -Recurse *.py | Get-Content | Measure-Object
```

We can see the output:

```
Count : 1253
```

This means py-suffixed files in the current directory have a total of 1253 lines.

[powershell]: https://en.wikipedia.org/wiki/Windows_PowerShell
