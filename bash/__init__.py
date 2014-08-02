from subprocess import PIPE, Popen


class bash(object):
    "This is lower class because it is intended to be used as a method."

    def __init__(self, cmd):
        self.p = None
        self.stdout = None
        self.bash(cmd)

    def bash(self, cmd):
        self.p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
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
        return self.stdout.strip().decode(encoding='UTF-8')
