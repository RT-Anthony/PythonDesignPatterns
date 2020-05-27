from __future__ import print_function
from enum import Enum
import abc


class TaskType(Enum):
    TASK1 = 1
    TASK2 = 2


class Task(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self):
        return


class Task1(Task):
    def run(self):
        print("Hello")
        return


class Task2(Task):
    def run(self):
        print("World!")
        return


class TaskFactory(object):
    @staticmethod
    def get(enum):
        if enum == TaskType.TASK1:
            return Task1()
        elif enum == TaskType.TASK2:
            return Task2()
