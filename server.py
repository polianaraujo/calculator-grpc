import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Sum(self, request, context):
        # print(f"Recebido: {request.a} + {request.b}")
        return calculator_pb2.Result(result=request.a + request.b)
    
    def Sub(self, request, context):
        return calculator_pb2.Result(result=request.a - request.b)
    
    def Mul(self, request, context):
        return calculator_pb2.Result(result=request.a * request.b)
    
    def Div(self, request, context):
        if request.b == 0:
            context.set_details('Divisão por zero não é permitido')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return calculator_pb2.Result()
        return calculator_pb2.Result(result=request.a / request.b)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC rodando na porta 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
