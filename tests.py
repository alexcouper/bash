from datetime import datetime
import unittest

try:
    from subprocess import TimeoutExpired
except ImportError:
    try:
        from subprocess32 import TimeoutExpired
    except ImportError:
        pass

import bash as bash_module
from bash import bash


class TestBash(unittest.TestCase):

    def test_bash_concatenation_by_method(self):
        result = bash('ls .').bash('grep "tests.py$"').value()
        self.assertEqual(result, 'tests.py')

    def test_bash_concatenation_within_command(self):
        result = bash('ls . | grep "tests.py$"').value()
        self.assertEqual(result, 'tests.py')

    def test_bash_repr(self):
        result = bash('ls . | grep "tests.py$"')
        self.assertEqual(repr(result), 'tests.py')

    def test_bash_stdout(self):
        result = bash('ls . | grep "tests.py$"')
        self.assertEqual(result.stdout, b'tests.py\n')
        self.assertEqual(result.code, 0)

    def test_bash_stderr(self):
        result = bash('./missing_command')
        self.assertEqual(result.stdout, b'')
        self.assertTrue(result.stderr in [
            # Mac OSX
            b'/bin/sh: ./missing_command: No such file or directory\n',
            # Travis
            b'/bin/sh: 1: ./missing_command: not found\n'
        ])
        self.assertEqual(result.code, 127)

    def test_passing_env(self):
        result = bash('echo $NAME', env={'NAME': 'Fred'})
        self.assertEqual(result.stdout, b'Fred\n')

    def test_output_to_stdout(self):
        b = bash('ls .', stdout=None)
        self.assertEqual(str(b), '')
        # Shouldn't find anything because we haven't piped it.
        self.assertEqual(str(b.bash('grep setup')), '')

    def test_timeout_works(self):
        if not bash_module.SUBPROCESS_HAS_TIMEOUT:
            raise unittest.SkipTest()
        self.assertRaises(TimeoutExpired, bash, 'sleep 2; echo 1', timeout=1)

    def test_sync_false_does_not_wait(self):
        t1 = datetime.now()
        b = bash('sleep 0.5; echo 1', sync=False)
        t2 = datetime.now()

        self.assertTrue((t2-t1).total_seconds() < 0.5)
        b.sync()
        self.assertEqual(b.stdout, b'1\n')
