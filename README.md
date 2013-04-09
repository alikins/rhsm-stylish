rhsm-stylish
============

pep8/flake8 extentions for rhsm python tools

Dependencies
===========

flake8 (recent, master from git/hg basically)
    https://bitbucket.org/tarek/flake8/wiki/Home

pep8 (recent, master from git basically)
    https://github.com/jcrocholl/pep8

Suggestions
==========

pep8-naming (https://github.com/flintwork/pep8-naming)


Install
=======

(Install recent versions of flake8 and pep8 first)

python setup.py install

Then ```flake8 --version``` should show 'rhsm-stylish' as a plugin.

Usage
====

Invoke flake8 as normal, it should pick up the new checks

ie,

```flake8 /path/to/foo.py```


Tests
=====
Some basic testing can be dome with:

    ```flake8 test/*.py```

At the moment, nothing is asserted or varified, but it should
at least be some sample good/bad code.

But basically, *_pass.py should not show any errors, while
_fail.py should show some errors.

Checks
======
R201  no 'except:' at least use 'except Exception:'
R202  assertRaises Exception too broad
R306  imports not in alphabetical order
R701  Empty localization string
R702  Formatting operation should be outside of localization method call
R702  Use bare string concatenation instead of +


License
======

This is based heavily on hacking.py from various OpenStack
projects, nova in particular. So:

Apache License 2.0
