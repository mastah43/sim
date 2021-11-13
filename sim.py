from flask import Flask, Response
import boto3
import simpy
import json


class World:

    def __init__(self):
        self.__env = simpy.Environment()
        self.__env.process(self.car())
        self.__message("not started")
        self.__messageCount = 0

    def __message(self, msg: str) -> None:
        # TODO self.__messageCount = self.__messageCount + 1
        print(f"world message: {msg}")
        kinesis = boto3.client("kinesis")
        kinesis_put_response = kinesis.put_record(
            StreamName='sim-1-events',
            Data=bytes(msg, "UTF-8"),
            PartitionKey="partition1", # TODO partition e.g. by agent
            SequenceNumberForOrdering="0" # TODO f"{self.__messageCount}"
        )
        print("kinesis put response: " + json.dumps(kinesis_put_response))
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
world.run()


@app.route('/')
def world_state():
    return Response(world.world_message, mimetype="text/plain")


if __name__ == '__main__':
    print("starting web server for development only, docker mode will use gunicorn wsgi server")
    app.run(port=5000, debug=True, host='0.0.0.0')

