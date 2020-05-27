import abc
from enum import Enum


class StateMachine(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def state(self):
        return

    @state.setter
    def state(self, new_val):
        return

    def process_input(self, _input):
        return


class Light(Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2


class TrafficLight(StateMachine):

    _state = Light.RED

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_val):
        self._state = new_val

    def process_input(self, _input):
        if self._state == Light.RED and _input == 1:
            self._state = Light.GREEN
            return self._state
        elif self._state == Light.GREEN and _input == 1:
            return self._state
        elif self._state == Light.GREEN and _input == 0:
            self._state = Light.YELLOW
            return self._state
        else:
            self._state = Light.RED
            return self._state

    def execute(self):
        if self._state == Light.RED:
            print("Please Wait")
        elif self._state == Light.YELLOW:
            print("Prepare to stop")
        elif self._state == Light.GREEN:
            print("Proceed")
