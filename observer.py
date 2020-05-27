from __future__ import print_function
import abc


class Observer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, data):
        return


class Observable(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update_observers(self):
        pass

    @abc.abstractmethod
    def subscribe(self, observer):
        pass


class Subscriber1(Observer):
    def update(self, data=None):
        print("Hello")


class Subscriber2(Observer):
    def update(self, data=None):
        print("world")


class Publisher(Observable):
    def __init__(self):
        self.observers = []

    def update_observers(self):
        for observer in self.observers:
            observer.update()

    def subscribe(self, observer):
        self.observers.append(observer)

