# Simulando um serviço de calculadora com uma operação simples: soma de dois números

## Exemplo básico de comunicação gRPC em Python

1. Definir o serviço no arquivo `.proto`.
2. Gerar o código Python com o `grpcio-tools`.
3. Implementar o **servidor**.
4. Implementar o **cliente**.

## Etapas para execução do projeto

1. Clonar ou criar o projeto.
2. Crie o ambiente (`pip` ou `conda`). Instalação dos pacotes necessários.
```
pip install -r requirements.txt
```
3. Gere os arquivos `.proto` com o script:
```
./generate_proto.sh
```
4. Iniciar o servidor (em um 1º terminal):
```
python3 server.py
```
5. Executar o cliente (em um 2º terminal):
```
python3 client.py
```

#### Estrutura do projeto
```
calculator-grpc
├── calculator.proto
├── client.py
├── server.py
├── requirements.txt
├── generate_proto.sh
└── README.md  (opcional)
```

#### 🤔 Analogia

|Arquivo|Como é criado|Função|
|`calculator.proto`|Manual|Definição das mensagens e serviço|
|`calculator_pb2.py`|Automático (`.proto`)|Mensagens serializadas|
|`calculator_pb2_gprc.py`|Automático (`.proto`)|Stubs do cliente e base do servidor|
|`server.py`|Manual|Implementa o serviço (servidor gRPC)|
|`client.py`|Manual|Consome o serviço (cliente gRPC)|