import socket
import os
import time 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

porta = int(input("Digite a porta para a conexão: ") + "\n")

try:

    server.bind(("0.0.0.0", porta))
    server.listen(5)
    print("Esperando a conexão...")
    client_socket, address = server.accept()
    os.system("cls")
    print("\033[32mConectado com o IP: \033[0m" + address[0])
    time.sleep(1.5)
    os.system("cls")
    print("Esperando o Cliente")
    time.sleep(1.5)
    os.system("cls")

    while True:
        pacotes_recebidos = client_socket.recv(100000).decode()
        print(f"Mensagem do Cliente: {pacotes_recebidos}")
        
        if pacotes_recebidos == "tchau\n" or pacotes_recebidos == "Tchau\n":
            print("Fim da conexão")
            break
        
        mensagem_servidor = input("Mensagem do Servidor: ")
        client_socket.send(mensagem_servidor.encode()) 
        
        if mensagem_servidor == "tchau\n" or mensagem_servidor == "Tchau\n":
            print("Fim da conexão")
            break

    client_socket.close()

except Exception as error:
    print("Erro: ", error)
