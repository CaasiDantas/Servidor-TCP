import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

porta = int(input("Digite a porta para a conexão: "))

try:

    server.bind(("0.0.0.0", porta))
    server.listen(5)
    print("Esperando a conexão...")
    client_socket, address = server.accept()
    print("Conectado com o IP: " + address[0])

    while True:

        pacotes_recebidos = client_socket.recv(100000).decode()
        print(f"Mensagem do Cliente: {pacotes_recebidos}")
        
        if pacotes_recebidos == "tchau\n" or "Tchau\n":
            print("Fim da conexão")
            break
        
        mensagem_servidor = input("Mensagem do Servidor: ") + "\n"
        client_socket.send(mensagem_servidor.encode()) 
        
        if mensagem_servidor == "tchau\n" or "Tchau\n":
            print("Fim da conexão")
            break

    client_socket.close()

except Exception as error:
    print("Erro: ", error)
