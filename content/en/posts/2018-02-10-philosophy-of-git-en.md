---
layout: post
title: "The Philosophy of Git"
date: '2018-02-10 16:01:31'
zhUrl: /philosophy-of-git
aliases:
  - /philosophy-of-git-en
---

This article attempts to introduce what makes Git remarkable.
Intended for readers who want to learn about Git,
or who are interested in software design.

<!--more-->

As an extremely flexible tool,
Git is handy to use for everything from version managing single-player game data files,
to multi-person collaborative crap-piling development.

So what's the secret behind Git's flexibility?
Probably because Git's design is orthogonal, and its implementation is solid.


## Overview

There are many terms / commands in Git,
but they can be grouped into a few major categories.
The concepts within each category are orthogonal,
meaning there's very little overlap between concepts,
no fuzzy concept definitions.
Based on this design,
Git correspondingly implemented a solid command system.

> Some concepts in Git are hard to translate accurately,
> this article uses the original English terms where concept words are involved.

Frequently used concepts include:

* Line Diff
* Commit
* Branch
* Repository
* Remote


## Line Diff

The way Git implements version control is by using Line Diffs
to deduce what each Commit specifically changed,
then using multiple Commits (essentially multiple Line Diffs) to construct the entire history.

This Line-Diff-based fundamental design determines some characteristics of Git:

1. Can store all history.
   We often hear "Git is a distributed version control system".
   This means Git doesn't need a centralized server.
   You can do all operations.
   Because all Line Diffs are stored locally,
   an operation like "view the list of filenames modified yesterday" can be completed entirely offline.

2. Not friendly to binary files.
   Binary files can't be forced into a Line Diff comparison.
   So if you use Git to manage binary files,
   Git will only display `Binary File Differ`.
   Combined with the "store all history" point above,
   a 200M file committed today,
   then modified-and-overwritten tomorrow and the day after,
   ends up making the whole directory 600M…
   (That is, generally don't use Git to manage large binary files)

3. Can detect file renames.
   If in a Commit,
   from the Line Diff perspective,
   the deleted file and the added file have high similarity,
   Git will judge it as a rename operation.


## Commit

Line Diffs make up a Commit.
A Commit is the minimum unit for most Git operations.
The word is both verb and noun.

A Commit contains multiple pieces of information:

- SHA hash: a unique identifier generated based on line diff + second-precision timestamp
- Author: the person who wrote the Line Diff
- Committer: a hidden attribute, representing the person who made the Commit
- Date: includes AuthorDate and CommitDate
- Message: the Commit's text description. Git takes the first line of the Message as the Subject, so [a certain convention][message] is usually followed
- Line Diffs: what content was changed

Concepts that could be mentioned here also include RootCommit and MergeCommit,
but their specialness doesn't affect practical use,
so we'll skip them and continue.


## Branch

Multiple Commits form a Branch.
The initial Branch is by default called master (the main branch).

In many commands, Branch and Commit can be used as equivalent operation targets.
For example:

Xiao Cheng wrote code for a day.
He committed many times on the wechat branch.
About to clock out, Xiao Cheng wants to review today's changes.
Suppose his log looks like this:

```
> git log --oneline --graph
* f01c8d1 (HEAD -> wechat) refactor: improve project layout
* 2f9c867 feat: add rest api to create card
* 5d5242b feat: custom wechat card background
* 873e6ca fix: wechat card slow query
* 0dd06a9 fix: 500 when user unsubscribe
* fb91f98 (origin/master, master) feat: implement wechat card
* 176b4f0 feat: implement membership level
* 2727226 migration: add Settings.enable_level
...
```

Then the following commands are completely equivalent:

```
# view diff from master to wechat
> git diff master..wechat

# view diff from master to current (HEAD means current position, i.e. wechat branch)
> git diff master..HEAD

# view diff from master to current (HEAD is the default, can be omitted)
> git diff master

# view diff from master's commit to current
> git diff fb91f98

# view diff from five Commits ago to current (master branch is five Commits ago)
> git diff HEAD~5
```

So we could also say "Branch is a special Commit".
Once you understand this,
when you look at most Git commands again,
you'll find they're all in the form `git <operation> <range> -- <files>...`.

For example, to view what's being released today is `git diff master..release`,
to roll back a file to 200 Commits ago is `git checkout HEAD~200 -- some/path/some/file.txt`,
to view the change history of a single file is `git log -- some/path/some/file.txt`


## Repository

A Repository contains all the operation history.
The `git init` command can initialize a Repository.

A Git Repository structure might look like this:

```
- .git/
  - hooks/
  - objects/
  - refs/
  - HEAD
  - config
- ForgiveDB/
- README.md
- requirements.txt
```

The `.git` directory here stores all the history of Line Diff, Commit, Branch mentioned above.
Just like the example with large binary files,
this might store several hundred MB of file history.


## Remote

A Remote is just a Repository that lives somewhere else.
The same Repository can have multiple Remotes added.

Aside from basic operations like `push/pull/fetch`,
there's also a rather slick design about Remote:
Git supports local Remotes.

For example, sample commands are as follows:

```
# Suppose there's a Repository at /home/lirian/chinese-calendar on the server
> cd /home/lirian

# Clone it to somewhere
> git clone chinese-calendar /opt/git/repo/chinese-calendar --bare

# Another user on the same server can clone this Repository
> cd /home/ldsink && git clone file:///opt/git/repo/chinese-calendar && git remote -v
origin       file:///opt/git/repo/chinese-calendar (fetch)
origin       file:///opt/git/repo/chinese-calendar (push)
```

With this kind of design,
Remote/Repository are completely separate.
History can still be modified even when offline.
We can even treat Remote as a special kind of Branch.
For instance, `fork - pull request` is an application of this pattern.


## Epilogue

Some examples in this article are just a taste.
Interested readers can try thinking about implementations for these extension questions:

* Regarding Line Diff: how similar do two modified files have to be for Git to recognize a rename?
* Regarding Commit: how to modify a Commit's Author? Can you see the Committer on GitHub?
* Regarding Branch: how to delete a remote branch? Can the Commit produced by `git stash` be operated on like a Branch?
* Regarding Repository: after deleting a branch, does the Git directory get smaller?
* Regarding Remote: what does the `--bare` flag used in the article mean?

In Git's design philosophy, another very powerful part is its History management,
which is another topic worth detailing.

Overall, in my eyes Git is a scientific and powerful tool.
The reasons Git is excellent are:

* Orthogonal design: clear term definitions, few overlapping concepts, strong expressive power.
* Solid implementation: rich secondary terminology, complete command parameters, fits real application scenarios.

(End)

[message]: https://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html
