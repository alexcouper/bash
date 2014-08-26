from subprocess import PIPE, Popen


class bash(object):
    "This is lower class because it is intended to be used as a method."

    def __init__(self, *args, **kwargs):
        self.p = None
        self.stdout = None
        self.bash(*args, **kwargs)

    def bash(self, cmd, env=None, stdout=PIPE):
        self.p = Popen(
            cmd, shell=True, stdout=stdout, stdin=PIPE, stderr=PIPE, env=env
        )
        self.stdout, self.stderr = self.p.communicate(input=self.stdout)
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
