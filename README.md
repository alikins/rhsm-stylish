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

License
======

This is based heavily on hacking.py from various OpenStack
projects, nova in particular. So:

Apache License 2.0
