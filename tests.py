import unittest

from bash import bash

class TestBash(unittest.TestCase):

    def test_bash_concatonation_by_method(self):
        result = bash('ls .').bash('grep "tests.py$"').value()
        self.assertEquals(result, 'tests.py')

    def test_bash_concatonation_within_command(self):
        result = bash('ls . | grep "tests.py$"').value()
        self.assertEquals(result, 'tests.py')

    def test_bash_repr(self):
        result = bash('ls . | grep "tests.py$"')
        self.assertEquals(repr(result), 'tests.py')

    def test_bash_stdout(self):
        result = bash('ls . | grep "tests.py$"')
        self.assertEquals(result.stdout, b'tests.py\n')
        self.assertEquals(result.code, 0)

    def test_bash_stderr(self):
        result = bash('./missing_command')
        self.assertEquals(result.stdout, b'')
        self.assertTrue(result.stderr in [
            # Mac OSX
            b'/bin/sh: ./missing_command: No such file or directory\n',
            # Travis
            b'/bin/sh: 1: ./missing_command: not found\n'
        ])
        self.assertEquals(result.code, 127)

