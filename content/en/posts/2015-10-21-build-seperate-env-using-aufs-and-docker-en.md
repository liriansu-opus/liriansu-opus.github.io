---
title: "Building Multiple Private Dev Environments with AUFS and Docker"
date: 2015-10-21 14:55:24
zhUrl: /build-seperate-env-using-aufs-and-docker
aliases:
  - /build-seperate-env-using-aufs-and-docker-en
---

Let me start this article with a question:
In our usual work, how do we generally give everyone an independent dev environment?

<!--more-->

## Eight Immortals Crossing the Sea

For example, the most common approach: everyone has their own computer, do whatever they want, sync code with something like Git.
But the initialization process is very slow this way—you have to install all kinds of software and configurations.

So some folks set up a central server, where everyone SSHes in via something like Putty, each with their own account.
But this way the environments aren't independent, and permission control is a pain (after all, everyone wants to sudo).

Later people just distributed VM images directly—each person gets a 10G image file,
just Load it and the environment is up.
But every time you modify the environment you have to update nearly 10G...

Anyway, it's eight immortals crossing the sea, each with their own tricks.
You can also use [AUFS][aufs] and [Docker][docker-intro] to give everyone an independent dev environment.


## AUFS

According to Google:

> AuFS stands for Another Union File System. AuFS started as an implementation of UnionFS Union File System. An union filesystem takes an existing filesystem and transparently overlays it on a newer filesystem. It allows files and directories of separate filesystem to co-exist under a single roof.May 8, 2013

Suppose we have a directory like this:

```
$ tree
.
└── public
    ├── database
    │   ├── dbfile1
    │   └── dbfile2
    └── src
        ├── helloworld.lisp
        └── sudoku.lisp
```

We want to use the public directory as a base and create a private environment for each person,
so we run a few commands:

```
$ mkdir change private
$ mount -t aufs -o dirs=./change:./public none ./private
$ tree
.
├── change
├── private
│   ├── database
│   │   ├── dbfile1
│   │   └── dbfile2
│   └── src
│       ├── helloworld.lisp
│       └── sudoku.lisp
└── public
    ├── database
    │   ├── dbfile1
    │   └── dbfile2
    └── src
        ├── helloworld.lisp
        └── sudoku.lisp
```

In the mount command, -t specifies the type as aufs, and -o is the option.
We mounted the change directory with read-write permission and the public directory with read-only permission into private.

Suppose we add and modify a file inside private:

```
$ cd private/
$ touch newfile
$ echo "Changes" > src/sudoku.lisp
$ cd ..
$ tree
.
├── change
│   ├── newfile
│   └── src
│       └── sudoku.lisp
├── private
│   ├── database
│   │   ├── dbfile1
│   │   └── dbfile2
│   ├── newfile
│   └── src
│       ├── helloworld.lisp
│       └── sudoku.lisp
└── public
    ├── database
    │   ├── dbfile1
    │   └── dbfile2
    └── src
        ├── helloworld.lisp
        └── sudoku.lisp
```

You can see that all the changes we made in the private environment happened inside change!

This is equivalent to stacking Layers—we stacked a writable change layer on top of a read-only public layer.
*Though for file deletions you need extra detection*


## Stacking with Docker

With the mount from the example above, stacking with Docker becomes easy.
Using [Docker's Volume][docker-volume]:

```
docker run -ti -v /tmp/docker/private:/work ubuntu /bin/bash
```

This way we can map the private directory as a volume into the /work directory inside the docker container.
The rest is just [Get good use of docker images][docker-images]~

[aufs]:            https://coolshell.cn/articles/17061.html
[docker-images]:   https://docs.docker.com/userguide/dockerimages/
[docker-intro]:    /virtual-machine-vs-vagrant-vs-docker-en
[docker-volume]:   https://docs.docker.com/userguide/dockervolumes/
