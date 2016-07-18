# gRPC tutorials in Python & GoLang

> gRPC, a language-neutral, platform-neutral, open source, remote procedure call (RPC) system initially developed at Google.

## What is gRPC?
In gRPC a client application can directly call methods on a server application on a different machine as if it was a local object, making it easier for you to create distributed applications and services. As in many RPC systems, gRPC is based around the idea of defining a service, specifying the methods that can be called remotely with their parameters and return types. On the server side, the server implements this interface and runs a gRPC server to handle client calls. On the client side, the client has a stub (referred to as just client in some languages) that provides the same methods as the server.
![](https://grpc.github.io/img/grpc_concept_diagram_00.png)

## gRPC & protobuf
> By default gRPC uses protocol buffers, Google’s mature open source mechanism for serializing structured data (although it can be used with other data formats such as JSON).

简而言之，protobuf负责数据的序列化/反序列化，gRPC负责接口代码的生成(server/stub)；

protobuf当前有2和3两个版本，IDL语法差别比较大，gRPC官方建议使用proto3

## install
1. install the gRPC runtime
```language
(for python) pip install grpcio
(for go) go get google.golang.org/grpc
```
2. install protocol buffers support
```language
(for python) pip install grpcio-tools
(for go) go get -a github.com/golang/protobuf/protoc-gen-go
```

## 运行示例代码
### python
```language
python greeter_server.py &  python greeter_client.py
```
如果修改了interfaces/interfaces.proto，需要重新生成接口代码
```language
$ ./run_codegen.sh
```

### GoLang
```language
go run server/main.go & go run client/main.go
```
如果修改了interfaces/interfaces.proto，需要重新生成接口代码
```language
$ protoc --go_out=plugins=grpc:. interfaces.proto
```

## Advance Topics
### RPC life cycle
*除了示例中使用的 **Unary** 接口类型*:
```language
rpc SayHello (HelloRequest) returns (HelloReply) {}
```
gRPC 还支持其他三种接口类型：
Server streaming RPC, 如：
```
rpc SayHelloServerStream (HelloRequest) returns (stream HelloReply) {}
```
Client streaming RPC, 如：
```
rpc SayHelloClientStream (stream HelloRequest) returns (HelloReply) {}
```
Bidirectional streaming RPC,如：
```
rpc SayHelloBiStream (stream HelloRequest) returns (stream HelloReply) {}
```

### Synchronous vs. asynchronous / Timeout &. cancel
python支持同步和异步调用rpc，同时支持超时和取消；
```
response = stub.SayHello.future(interfaces_pb2.HelloRequest(name="you"), _TIMEOUT_SECONDS)
在返回结果或者timeout之前可以主动取消: response.cancel()；取消的作用仅限于client（如果请求已经发给server，server端依然会处理改请求）
  print(response.result())
```