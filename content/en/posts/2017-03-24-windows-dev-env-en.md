---
title: "Setting Up a Comfortable Windows Development Environment"
date: "2017-03-24 02:00:55"
zhUrl: /windows-dev-env
aliases:
  - /windows-dev-env-en
---

If you also don't mind sitting at the bottom of the [hierarchy of contempt][we-are-the-same],
then let's exchange notes on `how to set up a Windows development environment`.

<!--more-->


## The Bottom of the [Hierarchy of Contempt][we-are-the-same]: Windows

The [hierarchy of contempt][we-are-the-same] is a real part of a programmer's daily life.
For example, take classic programming languages.
There's a saying that goes:

> C engineers look down on C++ engineers,
> C++ engineers look down on Java and C# engineers,
> Java engineers and C# engineers look down on each other.
> Engineers writing static languages look down on engineers writing dynamic languages.
> Engineers using Python 3 look down on engineers still using Python 2,
> Engineers using Python 2 look down on engineers who hit UnicodeEncodeError.
>
> All engineers look down on PHP engineers.

And in terms of operating systems used,
the [hierarchy of contempt][we-are-the-same] basically goes:

> Engineers using Mac OS X look down on engineers using Linux,
> Engineers using Linux look down on engineers using Windows.

That said,
I still really like the Windows development environment.
The main reason is: **I can play games**...
Although nowadays I almost never play,
but this **can play games** unlimited possibility deeply attracts me...

o(〃'▽'〃)o
So we'll go through a series of steps
to set up the most comfortable Windows development environment! ~~and gaming environment~~


## Essential Software

There are a few pieces of software I consider essential in a Windows dev environment.

### [Chocolatey][chocolatey]

[Chocolatey][chocolatey] is a command-line package manager on Windows.
Not official,
but very easy to use.

Open `cmd.exe` as administrator and run one line of command to install successfully:

```
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

Once installed, one line of command installs commonly used software
and configures the Path environment variable:

```
choco install -y 7zip everything git jdk8 nodejs npm python2 putty vagrant virtualbox vim wox
```

The only downside is the installation is silent with default values,
so if some software needs to disable right-click menus
or be put in a specific folder, you'll have to set that up yourself.


### [Wox][wox]

That's the [wox][wox] that the previous `choco` command installs at the end,
a quick app launcher tool.

If you know `Spotlight` or `Alfred` on Mac OS,
[wox][wox] is their Windows version.

For example, on any interface,
after I press the `Alt + Space` shortcut,
a white input box pops up.
After I type the program name and hit enter,
the program automatically opens.
[wox][wox] supports wildcards,
supports search,
supports system operations (like lock screen, restart),
and with [everything][everything] added it supports file search.

![wox-sample][wox-sample]


### [Git Bash][git-scm]

What I'm talking about here isn't Git, but specifically [Git Bash][git-scm].
[Git Bash][git-scm] is a terminal software based on [mingw (MINimal Gnu for Windows)][mingw] that gets installed alongside Git.
It comes with Linux command-line tools like bash / ls / find / grep / wc,
supports .profile for custom environment variables,
supports git file status display.
With this I basically haven't used cmd or powershell anymore.


## My Preferences

The three pieces of software above I strongly recommend.
Below are some with a certain level of,
or strong, personal taste.

* `VirtualBox + Vagrant + Putty`: For normal development, I use `vagrant init ubuntu/trusty64 && vagrant up` to start an Ubuntu VM, then use Putty to connect, treating this VM as a complete Server. [VirtualBox][virtualbox] is the VM container, similar to VMware but with a more lenient license. [Vagrant][vagrant] is the VM management software, providing data communication between host and VM, and some automated tasks. [Putty][putty] is the classic remote terminal software.
* [`JetBrains full suite, including IntelliJ IDEA, PyCharm, Rider EAP, ReSharper`][jetbrains]: After all JetBrains is a commercial company that makes IDEs. They're still better than _some_ open source IDEs. For example, their IDEs basically don't have [Issues unresolved for 10 years][backslash-r]...
* `NetEase Cloud Music + Youdao Dictionary + Youdao Cloud Note`: Uh, not sure how to introduce these. It's pretty literally I just need these things. Coffee and music are programmers' good friends. I don't really drink coffee, I only have music.
* [`everything`][everything]: a super fast super easy-to-use global Windows search tool, efficiency comparable to the Linux `locate` command.
* [`Vim, on Windows it's GVim`: God of editors][editor-war].


## Other Tips

* [Left-ear Mouse's advice: be an eco-friendly programmer, starting with not using Baidu][no-baidu]
* Besides `Alt + F4`, Windows shortcuts `Win + E`, `Win + R`, `Win + D`, `Win + L`, `Win + Tab` are also very useful.
* You can use `left-click select in terminal` to copy, `Shift + Insert` to paste.
* The Windows equivalent of `ln` is `mklink <dest> <source>`. For directories add the parameter `mklink /d <dest> <source>`.
* If you use Vim, remap your `<Caps Lock>` key to `<Ctrl>`.
* Some configurations used in this article can also be found in [my config project on GitHub][myconf].

[backslash-r]: https://bugs.eclipse.org/bugs/show_bug.cgi?id=76936
[chocolatey]: https://chocolatey.org/
[editor-war]: https://en.wikipedia.org/wiki/Editor_war
[everything]: https://www.voidtools.com/
[git-scm]: https://git-scm.com/downloads
[jetbrains]: https://www.jetbrains.com/
[mingw]: https://www.mingw.org/
[myconf]: https://github.com/LKI/myconf
[no-baidu]: https://coolshell.cn/articles/9308.html
[putty]: https://www.putty.org/
[vagrant]: https://www.vagrantup.com/
[virtualbox]: https://www.virtualbox.org/wiki/VirtualBox
[we-are-the-same]: https://www.zhihu.com/question/24270600
[wox-sample]: /assets/windows_wox.jpg
[wox]: https://www.getwox.com/
