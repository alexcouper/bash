import unittest

from bash import bash

class TestBash(unittest.TestCase):

    def test_bash_concatonation_by_method(self):
        result = bash('ls .').bash('grep "tests.py$"').value()
        self.assertEquals(result, 'tests.py')

    def test_bash_concatonation_within_command(self):
        result = bash('ls . | grep "tests.py$"').value()
        self.assertEquals(result, 'tests.py')
