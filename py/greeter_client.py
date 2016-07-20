from __future__ import print_function

from grpc.beta import implementations

import time
import interfaces_pb2

_TIMEOUT_SECONDS = 10


def run():
  channel = implementations.insecure_channel('localhost', 50051)
  stub = interfaces_pb2.beta_create_Greeter_stub(channel)
  response = stub.SayHello(interfaces_pb2.HelloRequest(name="you"), _TIMEOUT_SECONDS)
  print(response.message)


if __name__ == '__main__':
  run()
