#!/bin/bash

# Runs the protoc with gRPC plugin to generate protocol messages and gRPC stubs.
python -m grpc.tools.protoc -I../interfaces --python_out=. --grpc_python_out=. ../interfaces/interfaces.proto
