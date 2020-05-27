from factory import *
from state_machine import *
from observer import *
from command import *


def factory_example():
    task_1 = TaskFactory.get(TaskType.TASK1)
    task_2 = TaskFactory.get(TaskType.TASK2)

    task_1.run()
    task_2.run()


def state_machine_example():
    traffic_light = TrafficLight()
    print(traffic_light.state)
    traffic_light.execute()

    traffic_light.process_input(1)
    print(traffic_light.state)
    traffic_light.execute()

    traffic_light.process_input(1)
    print(traffic_light.state)
    traffic_light.execute()

    traffic_light.process_input(0)
    print(traffic_light.state)
    traffic_light.execute()

    traffic_light.process_input(0)
    print(traffic_light.state)
    traffic_light.execute()
    traffic_light.process_input(0)
    print(traffic_light.state)
    traffic_light.execute()


def observer_example():
    publisher = Publisher()
    subscriber_1 = Subscriber1()
    subscriber_2 = Subscriber2()
    subscriber_3 = Subscriber1()

    publisher.subscribe(subscriber_1)
    publisher.subscribe(subscriber_2)
    publisher.subscribe(subscriber_3)

    publisher.update_observers()


def command_example():
    invoker = Invoker(SimpleCommand(), ComplexCommand())
    invoker.run()


if __name__ == "__main__":
    factory_example()
    print("")
    print("")
    state_machine_example()
    print("")
    print("")
    observer_example()
    print("")
    print("")
    command_example()
