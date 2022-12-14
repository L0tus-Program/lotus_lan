import socket

def client():
    target_host = input("Insira o HOST : ")
    target_port = 80

    #cria um pbjeto socket

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # faz o cliente se conectar

    client.connect((target_host,target_port))

    #envia alguns dados

    client.send(("GET / HTTP|1.1\r\nHost: google.com\r\n\r\n").encode()) # no livro não tem a função encode, mas no python3 passa a ser necessário

    # recebe alguns dados

    response = client.recv(4096)

    print(response)
