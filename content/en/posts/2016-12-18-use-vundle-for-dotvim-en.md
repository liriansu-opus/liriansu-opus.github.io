---
title: "Using Vundle to Manage Vim Plugins"
date: "2016-12-18 02:22:16"
zhUrl: /use-vundle-for-dotvim
aliases:
  - /use-vundle-for-dotvim-en
---

Today I switched my vim plugin manager to [Vundle][vundle].
I used to use [pathogen][pathogen].

<!--more-->


## Vim Configuration

Actually I only started using Vim after my internship.
At that time Justin directly let me clone a copy of [his vim configuration][dotvim-justin].
Using a ready-made configuration greatly flattened Vim's learning curve,
and I could get started using it pretty quickly.
Even now, I still think the correct posture for picking up Vim is to find some big shot's configuration.

Later when I'd been using Vim a bit more,
I started trying to manually modify vimrc to change settings.
The foundation of modifying code is reading code / learning code,
so I learned about [pathogen][pathogen],
a Vim plugin for quickly adding plugins...


## pathogen

The advantage of pathogen is that it's tiny and straightforward:

You just need to add an autoload folder,
configure pathogen's loading,
and then you can freely add or remove plugins under the preset plugin directory.

However, there are a few annoying things in actual use:

* For convenience, I generally use git submodule to add plugins.
git submodule not only has a crappy usage,
its commit is also pinned,
so I often have to manually update plugin versions.
* Because I used git submodule, deleting plugins also became cumbersome.
* [pathogen][pathogen] is mainly written by [Tim Pope][tpope],
and that project only has three updates in a year...
not active at all.

Considering flexibility/portability/activity,
I decided to switch package managers.


## Vundle

So I thought of [Vundle][vundle],
a Vim plugin manager that looks pretty proper.
Its configuration is actually relatively simple:

Clone the [Vundle][vundle] package locally (can use git submodule),
configure vimrc, then write plugin names in vimrc.

But the first time loading plugins with the command `vim +PluginInstall +qall` can be pretty slow.


## Current Configuration

So after fiddling around a bit,
I successfully switched from pathogen to vundle.
My dotvim is on [github][dotvim].

Side note:
The first time I learned about [Vundle][vundle],
I always felt it had a strong knockoff-Emacs-package-manager vibe,
so back then I didn't consider [Vundle][vundle] at all...
So **technical taste can't be the only criterion for evaluating technology~**

[vundle]:          https://github.com/VundleVim/Vundle.vim
[pathogen]:        https://github.com/tpope/vim-pathogen
[dotvim-justin]:   https://github.com/LKI/dotvim
[tpope]:           https://github.com/tpope
[dotvim]:          https://github.com/LKI/dotvim
