---
title:     "Differences Between Virtual Machine, Vagrant, and Docker"
date:      2015-10-12 12:49:55
zhUrl: /virtual-machine-vs-vagrant-vs-docker
aliases:
  - /virtual-machine-vs-vagrant-vs-docker-en
---

Virtualization technology has always been a very important thing in the computer world.
The first thing most programmers think of when they hear this word is VMware running Linux under Windows.
And this "VMware running Linux" is what we call a Virtual Machine.

<!--more-->

The main benefit of a virtual machine is that you can create a development environment different from the host OS
(for example, most offices use Windows computers)

But this convenience for development also leads to it being kind of a hassle to initialize this kind of environment
And when a project gets to a certain stage and depends on certain changes in the environment itself
creating a virtual machine dev environment from scratch becomes very tedious
Vagrant is a tool meant to solve this kind of tedium


## Vagrant
According to [the official statement][why-vagrant]

> Vagrant provides easy to configure, reproducible, and portable work environments built on top of industry-standard technology and controlled by a single consistent workflow to help maximize the productivity and flexibility of you and your team

Vagrant itself doesn't do the virtual machine work, but allows users to use VMware|VirtualBox|AWS to launch VM images. They call these Providers.
Of course, images in Vagrant are called Boxes, and many companies have already prepared initialized Boxes [here][hashicorp-box] that you can use directly
Vagrant also provides initialization scripts (Provisioning) for Boxes — these init scripts can use more scripting tools to complete the configuration of the Box.

So compared to traditional virtual machines, Vagrant stands on the shoulders of giants and accomplishes automation.


## Docker
The Docker project's goal is to achieve a lightweight virtualization solution. The biggest difference between it and Virtual Machine is that Docker containers share the OS kernel
![vm][virtual-machine]
![docker][docker-engine]

So the comparison between Docker and traditional virtual machines is obvious:

| Feature           | Docker        | Virtual Machine     |
|-------------------|---------------|---------------------|
| Startup           | Seconds       | Minutes             |
| Size              | Usually MB    | Usually GB          |
| Performance       | Near native   | Weaker than native  |
| Single host count | Thousands     | Usually dozens      |
| Kernel            | Shared        | Independent         |


## Vagrant vs Docker
Honestly, these two shouldn't be put together for comparison — their virtualization levels aren't on the same scale.
And these two aren't contradictory: if you need to run several specific Linux distributions on a Windows system, you can totally use Vagrant + Virtual Machine first and then embed several Dockers inside.

If you must compare them, if you need to run cross-platform virtualization, use Vagrant; *otherwise*, use Docker

Lastly let me throw in a comparison table:

| Feature        | Virtual Machine     | Vagrant             | Docker                |
|----------------|---------------------|---------------------|-----------------------|
| Virtualization | Full virtualization | None                | System virtualization |
| Image mgmt     | None                | Yes, usually GB     | Yes, usually MB       |
| Performance    | Weaker than native  | Weaker than native  | Near native           |
| Kernel         | Independent         | Independent         | Shared                |


## References
1. [《Docker — From Beginner to Practice》][docker-the-book]
2. [Why Vagrant][why-vagrant]
3. [Docker is Not a Virtual Machine][docker-by-shell909090]
4. [Should I use vagrant or docker][so-vagrant-or-docker]

[why-vagrant]:             https://docs.vagrantup.com/v2/why-vagrant/index.html
[hashicorp-box]:           https://atlas.hashicorp.com/boxes/search
[virtual-machine]:         https://dockerpool.com/static/books/docker_practice/_images/virtualization.png
[docker-engine]:           https://dockerpool.com/static/books/docker_practice/_images/docker.png
[docker-the-book]:         https://dockerpool.com/static/books/docker_practice/index.html
[docker-by-shell909090]:   https://github.com/shell909090/slides/blob/master/md/docker.md
[so-vagrant-or-docker]:    https://stackoverflow.com/questions/16647069/should-i-use-vagrant-or-docker-io-for-creating-an-isolated-environment
