from flask import Flask
import simpy


class World:

    def __init__(self):
        self.__env = simpy.Environment()
        self.__env.process(self.car())
        self.__message("not started")

    def __message(self, msg: str) -> None:
        print(f"world message: {msg}")
        self.__world_message = msg

    def __message_with_time(self, msg: str) -> None:
        self.__world_message = f"{msg} at {self.__env.now}"

    def car(self):
        while True:
            self.__message_with_time("Start parking")
            parking_duration = 5
            yield self.__env.timeout(parking_duration)
            self.__message_with_time("Start driving")
            trip_duration = 2
            yield self.__env.timeout(trip_duration)

    def run(self):
        self.__env.run(until=15)

    @property
    def world_message(self):
        print(f"http request for world message received, sending {self.__world_message}")
        return self.__world_message


app = Flask(__name__)
world = World()


@app.route('/')
def world_state():
    return world.world_message


if __name__ == '__main__':
    world.run()
    app.run()

