import sys
from subprocess import PIPE, Popen
SUBPROCESS_HAS_TIMEOUT = True
if sys.version_info < (3, 0):
    try:
        from subprocess32 import PIPE, Popen  #NOQA
    except ImportError:
        # You haven't got subprocess32 installed. If you're running 2.X this
        # will mean you don't have access to things like timeout
        SUBPROCESS_HAS_TIMEOUT = False


class bash(object):
    "This is lower class because it is intended to be used as a method."

    def __init__(self, *args, **kwargs):
        self.p = None
        self.stdout = None
        self.bash(*args, **kwargs)

    def bash(self, cmd, env=None, stdout=PIPE, stderr=PIPE, timeout=None, sync=True):
        self.p = Popen(
            cmd, shell=True, stdout=stdout, stdin=PIPE, stderr=stderr, env=env
        )
        if sync:
            self.sync(timeout)
        return self

    def sync(self, timeout=None):
        kwargs = {'input': self.stdout}
        if timeout:
            kwargs['timeout'] = timeout
            if not SUBPROCESS_HAS_TIMEOUT:
                raise ValueError(
                    "Timeout given but subprocess doesn't support it. "
                    "Install subprocess32 and try again."
                )
        self.stdout, self.stderr = self.p.communicate(**kwargs)
        self.code = self.p.returncode
        return self

    def __repr__(self):
        return self.value()

    def __unicode__(self):
        return self.value()

    def __str__(self):
        return self.value()

    def __nonzero__(self):
        return self.__bool__()

    def __bool__(self):
        return bool(self.value())

    def value(self):
        if self.stdout:
            return self.stdout.strip().decode(encoding='UTF-8')
        return ''
