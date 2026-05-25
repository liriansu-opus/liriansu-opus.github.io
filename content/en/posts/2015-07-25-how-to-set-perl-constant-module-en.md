---
title:     "How to Elegantly Use Perl's Constant Module"
date:      2015-07-25 20:56:06
zhUrl: /how-to-set-perl-constant-module
aliases:
  - /how-to-set-perl-constant-module-en
---

Recently while doing Perl coding I ran into a problem: I needed to validate a series of constants.

After Research&Develop-ing, I have some insights.

This article gives a _self-proclaimed_ elegant solution from the angle of Perl's constant definitions.

<!--more-->

## Common Constant Definitions in Perl

When writing projects, to avoid Magic Number situations, we often need to define constants.

Of course, according to [How to Write Unmaintainable Code][1], we shouldn't define constants — the more Magic the Number, the better.

Generally, constants in Perl look like this:

```perl
    use constant CONST_PI => 3.1416;
```

In modular coding, as constants increase, we'll want to put these constants into a constants module (Perl Module):

This approach also conforms to the DRY (Don't Repeat Yourself) principle. #DRYBestPractice?

For example, after some grinding, we have the following constants module.

```perl
    package Lirian::Constants;
    use strict;
    use warnings;

    #Math Const
    use constant CONST_PI => 3.1416;
    use constant CONST_E  => 2.718;

    #Default Config Parm Name
    use constant PARM_DB_NAME  => 'dbName';
    use constant PARM_DB_HOST  => 'dbHost';
    use constant PARM_GIT_USER => 'gitUser';

    require Exporter;
    our @ISA = qw(Exporter);

    our @EXPORT_OK = qw(
        CONST_PI
        CONST_E
        PARM_DB_NAME
        PARM_DB_HOST
        PARM_GIT_USER
    );

    our %EXPORT_TAGS = (
        all  => \@EXPORT_OK,
        math => [qw(
            CONST_PI
            CONST_E
        )],
        parm => [qw(
            PARM_DB_NAME
            PARM_DB_HOST
            PARM_GIT_USER
        )],
    );
```

The code above bluntly demonstrates a Perl constants module.

The `our @ISA = qw(Exporter);` indicates this module inherits from the [Exporter][2] module.

With this definition, we have a "central repository" for constants.

As for how to use it, let's see the next section.


## Using the Constants Module

In the previous section, by inheriting from Exporter, we got a Lirian::Constants module.

Generally, we use it like this:

```perl
    package Lirian::Math;

    use Lirian::Constants qw(:all);
    use strict;
    use warnings;

    sub get_circum {
        my ($r) = @_;

        return 2 * CONST_PI * $r;
    }

    1;
```

In normal cases, using constants is fairly straightforward, but suppose the requirement is a bit twisty:

At the start of the program, we need to validate the user's config file, making sure every entry is valid.

For example, the config file looks like this:

```config
    dbName=github
    dbHost=localhost
    gitUser=LKI
```

Obviously, a simple but somewhat dumb method is to do this:

```perl
    sub validate_config_dumb {
        my ($conf) = @_;

        validate_parm($conf, PARM_DB_NAME);
        validate_parm($conf, PARM_DB_HOST);
        validate_parm($conf, PARM_GIT_USER);
    }
```

This approach has a few problems:

1. With lots of config parameters, the code gets very long, ugly
2. When adding config constants, you not only need to modify the constants module, you also need to add it here — tiring
3. Submitting code like this feels embarrassing, dumb
4. None of the above three points are problems in [Lucky Programming][3]

So what counts as an elegant approach?


## Leveraging Perl's Export Mechanism

In Exporter, the contents defined in %EXPORT_TAGS can be referenced directly:

```perl
    my $tags      = \$Lirian::Constants::EXPORT_TAGS;
    my $math_tags = $tags->{math}; # ['CONST_PI', 'CONST_E'];
    my $parm_tags = $tags->{parm}; # ['PARM_DB_NAME', 'PARM_DB_HOST', 'PARM_GIT_USER'];
```

This way we can get the constants' names. Now we need to [get a variable's value from its name in Perl][4]

```perl
    my $name  = 'CONST_PI';
    my $value = Lirian::Constants->$name; # 3.1416
```

So for the problem in the previous section, we can come up with a more elegant solution~

```perl
    sub validate_config {
        my ($conf) = @_;

        my $tags      = \$Lirian::Constants::EXPORT_TAGS;
        my $parm_tags = $tags->{parm};
        foreach my $parm_name (@$parm_tags) {
            my $parm_value = Lirian::Constants->$parm_name;
            validate_parm($conf, $parm_value);
        }
    }
```

Done! From now on, when adding constants, validate_config will automatically validate the newly added config options~

Now you can use [a cool Git Commit Message][5] to commit your work!

[1]:https://coolshell.cn/articles/4758.html
[2]:https://perldoc.perl.org/Exporter.html
[3]:https://coolshell.cn/articles/2058.html
[4]:https://stackoverflow.com/questions/2187682/how-do-i-access-a-constant-in-perl-whose-name-is-contained-in-a-variable
[5]:https://whatthecommit.com/
