---
layout: post
title: "Python Project Deployment Automation Part One: A Chestnut Example"
date: '2017-11-23 16:49:57'
zhUrl: /python-deployment-automation-one-sample
aliases:
  - /python-deployment-automation-one-sample-en
---

This article mainly describes the tools used in the code release workflow at my company
([a growing startup][zaihui-intro]).


<!--more-->


## Release tool: [Jenkins][jenkins]

The release tool we use is [Jenkins][jenkins], which [many companies are using][jenkins-stackshare].
To give a ~~chestnut~~ picture as an example,
on the Jenkins Server we can release backend server code with one click:

![jenkins-demo][jenkins-demo]

After pressing the Build button,
the following happens:

* On the Jenkins server, a pre-configured Bash script is triggered
  * git commands fetch the latest code version, switch to the appropriate branch
  * ~~Run code style checks and unit tests~~ since we started using the paid version of GitLab, this function has been switched to GitLab CI
  * After security checks pass, use the fab command to deploy the code


## Release command: [Fabric][fabric]

The fab command here uses [Python's Fabric library][fabric].
This library is similar to [ansible][ansible],
and mainly contains two sets of functions:

* **Local command integration**.
This has a similar function to Java's [`ant`][ant], [`gradle`][gradle],
or JS's [`npm run`][npm].
They can all integrate several operations into a simple workflow command.

* **Remote ssh tool**.
[Fabric][fabric] is based on [ssh][ssh],
and implements a convenient set of remote command interfaces.
For example, this piece of code can upload configurations to a remote server:

```
from fabric.api import *  # NOQA

# Don't bother trying, both domains here are fake. Just plug in your ssh host/user.
env.hosts = ['www.kezaihui.com', 'zaihuiwebserver-814613977.cn-north-1.elb.amazonaws.com.cn']
env.user = 'saber'

def update_supervisor_config():
    put('./supervisor/*.conf', '/etc/supervisor/conf.d/', use_sudo=True)
    run('supervisorctl update', use_sudo=True)
```

But [Fabric][fabric] has a rather annoying issue: it only supports [Python2][which-python].
If you want to use [Python3][which-python],
you can use [Fabric][fabric]'s fork branch [Fabric3][fabric3].
[Fabric3][fabric3] is mostly functionally equivalent to [Fabric][fabric].

If you only want the local command integration part of the functionality,
there's another library called [Invoke][invoke] that provides similar functionality.
This library is mainly impressive in its name —
[Dota 2's Karl is also called Invoker][invoker].


## Process management: [Supervisor][supervisor]

In production environments,
to ensure the robustness of server processes,
we use [supervisor][supervisor] to monitor process status.

A simple nginx supervisor config will look like this:

```
[program:nginx]
command=/usr/sbin/nginx
autostart=true
autorestart=true
stdout_logfile=/var/log/supervisor/nginx.log
stderr_logfile=/var/log/supervisor/nginx_error.log
```

After putting the config file at `/etc/supervisor/conf.d/nginx.conf`,
you can use a series of commands to bring the service up:

```
$ supervisorctl update  # supervisorctl is supervisor's CLI tool, refresh the config
nginx    STARTING    pid 1000, uptime 0:00:00

$ supervisorctl status  # check process status
nginx    RUNNING     pid 1000, uptime 0:12:34

$ kill -9 1000  # simulate various disturbances by killing the nginx process

$ supervisorctl status  # check process status again, you can see supervisor auto-restarted it
nginx    STARTING    pid 1020, uptime 0:00:00
```

## Summary

The engineer responsible for releasing,
may have only clicked one `Build` button on the page.
But the actual flow is like this:

* Jenkins triggered the configured Bash script.
* Inside the Bash script, the fab command was run.
* The fab command executed the code upload work, essentially executing commands over ssh.
* Finally supervisor started/restarted the process service.
* Release complete.

The above is roughly my company's current crude introduction to deployment automation.
The upgrade road is long,
there's still a lot to learn / practice / master.

> [Original link][self], [author @Lirian Su][about-me]
>
> Copyright belongs to the Zaihui R&D team. Reprinting is welcome, please retain the source.

[zaihui-intro]: https://www.zhihu.com/question/19596230/answer/152193862
[jenkins-stackshare]: https://stackshare.io/jenkins
[jenkins]: https://jenkins.io/
[jenkins-demo]: /assets/pics/zaihui_jenkins.jpg
[fabric]: https://github.com/fabric/fabric
[ansible]: https://github.com/ansible/ansible
[ant]: https://ant.apache.org/
[gradle]: https://gradle.org/
[npm]: https://www.npmjs.com/
[ssh]: https://en.wikipedia.org/wiki/Secure_Shell
[which-python]: https://docs.python-guide.org/en/latest/starting/which-python/
[fabric3]: https://github.com/mathiasertl/fabric/
[invoke]: https://www.pyinvoke.org/
[invoker]: https://dota2.gamepedia.com/Invoker
[supervisor]: https://supervisord.org/
[self]: /python-deployment-automation-one-sample-en
[about-me]: /about/
