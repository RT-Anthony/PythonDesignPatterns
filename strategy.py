from __future__ import print_function


class Context(object):
    def __init__(self, strategy):
        self._strategy = strategy

    def run(self):
        self._strategy.run()


class Strategy(object):
    def run(self):
        print("Do default thing")


class StrategyA(Strategy):
    pass


class StrategyB(Strategy):
    def run(self):
        print ("Do different thing")
