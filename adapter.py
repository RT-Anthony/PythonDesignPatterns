from __future__ import print_function


class Target(object):

    def request(self):
        return "Target's default behavior"


class Adaptee(Target):

    def get_request(self):
        return "get_request called"


class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return self._adaptee.get_request()
