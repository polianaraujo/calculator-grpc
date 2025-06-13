#!/bin/bash

# Gera os arquivos *_pb2.py e *_pb2_grpc.py a partir do .proto
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

echo "Arquivos .proto gerados com sucesso!"