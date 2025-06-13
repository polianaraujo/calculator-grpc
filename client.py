import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    request = calculator_pb2.SumRequest(a=5, b=7)
    response = stub.Sum(request)

    print("Resultado da soma:", response.result)

if __name__ == '__main__':
    run()
