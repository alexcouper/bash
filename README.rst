bash for python
===============

A library that enables easy running and concatonation of bash commands in
python

For example::

    >>> from bash import bash
    >>> b = bash('ls .')
    >>> b
    README.md
    bash.py
    bash.pyc
    requirements.txt
    tests.py
    tests.pyc
    >>> b.bash('grep ".pyc"')
    bash.pyc
    tests.pyc

Motivation
----------

I found that I was often having to write the same lines of code to handle
running bash commands from python.

This provides a pip-installable, tested shortcut to writing::

    from subprocess import PIPE, Popen

    p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    output, err = p.communicate()


Support + Contributing
----------------------

Feel free to make pull requests, or report issues via the repo:

https://github.com/alexcouper/bash
