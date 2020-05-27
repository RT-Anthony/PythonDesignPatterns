from __future__ import print_function
import abc


class Command(object):
    __metaclass__ = abc.ABCMeta

    def execute(self):
        pass


class SimpleCommand(Command):
    def execute(self):
        print("Executing simple command...")


class ComplexCommand(Command):
    def execute(self):
        Receiver.func1()
        Receiver.func2()


class Receiver(object):
    @staticmethod
    def func1():
        print("Doing part 1")

    @staticmethod
    def func2():
        print("Doing part 2")


class Invoker(object):
    def __init__(self, on_start=None, on_finish=None):
        self._on_start = on_start
        self._on_finish = on_finish

    def set_on_start(self, command):
        self._on_start = command

    def set_on_finish(self, command):
        self._on_finish = command

    def run(self):
        print("Running start command")
        self._on_start.execute()

        print("Invoker logic ... ")

        print("Running finish command")
        self._on_finish.execute()
