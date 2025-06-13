import grpc
import calculator_pb2
import calculator_pb2_grpc

def get_numbers():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    return a, b

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    a, b = get_numbers()

    print("Resultados:")
    print("Soma:", stub.Sum(calculator_pb2.TwoNumbers(a=a, b=b)).value)
    print("Subtração:", stub.Subtract(calculator_pb2.TwoNumbers(a=a, b=b)).value)
    print("Multiplicação:", stub.Multiply(calculator_pb2.TwoNumbers(a=a, b=b)).value)

    try:
        result = stub.Divide(calculator_pb2.TwoNumbers(a=a, b=b)).value
        print("Divisão:", result)
    except grpc.RpcError as e:
        print(f"Erro na divisão: {e.details()}")

if __name__ == "__main__":
    main()
