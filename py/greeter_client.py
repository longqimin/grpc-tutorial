from __future__ import print_function

from grpc.beta import implementations

import time
import interfaces_pb2

_TIMEOUT_SECONDS = 20


def run():
  channel = implementations.insecure_channel('localhost', 50051)
  stub = interfaces_pb2.beta_create_Greeter_stub(channel)
  response = stub.SayHello.future(interfaces_pb2.HelloRequest(name="you"), _TIMEOUT_SECONDS)
  time.sleep(0.1)
  response.cancel()
  print(response.result())


if __name__ == '__main__':
  run()
