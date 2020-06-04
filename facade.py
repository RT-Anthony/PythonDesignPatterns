from __future__ import print_function


class Facade(object):
    def __init__(self, subsystem1, subsystem2):
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def execute(self):
        self._subsystem1.run()
        self._subsystem2.run()


class Subsystem1(object):
    def run(self):
        print("SubSys 1")


class Subsystem1(object):
    def run(self):
        print("SubSys 1")
