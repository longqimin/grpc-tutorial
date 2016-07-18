package main

import (
	"log"
	"net"

	"golang.org/x/net/context"
	"google.golang.org/grpc"

	pb "../../interfaces"
)

const (
	port = ":50051"
)

// server is used to implement interfaces.GreeterServer.
type server struct{}

// SayHello implements interfaces.GreeterServer
func (s *server) SayHello(ctx context.Context, in *pb.HelloRequest) (*pb.HelloReply, error) {
	println("SayHello")
	return &pb.HelloReply{Message: "hello"}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterGreeterServer(s, &server{})

	s.Serve(lis)
}
