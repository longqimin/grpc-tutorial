import time

import interfaces_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(interfaces_pb2.BetaGreeterServicer):

  def SayHello(self, request, context):
    print "SayHello"
    return interfaces_pb2.HelloReply(message = "hello")


def serve():
  server = interfaces_pb2.beta_create_Greeter_server(Greeter())
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except:
    server.stop(0)

if __name__ == '__main__':
  serve()
