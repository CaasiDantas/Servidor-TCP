import socket
import os
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lista de portas reservadas
portas_reservadas = [21, 22, 80, 443, 3306, 8080]

while True:
    try:
        porta = int(input("Digite a porta para a conexão: "))
        
        if porta <= 1024 or porta in portas_reservadas:
            print("Porta inválida. A porta deve ser superior a 1024 e não pode ser uma porta reservada")
            continue
            

        server.bind(("0.0.0.0", porta))
        server.listen(5)

        print("Esperando a conexão...")

        client_socket, address = server.accept()
        os.system("cls" if os.name == "nt" else "clear")

        print("\033[32mConectado com o IP: \033[0m" + address[0])
        time.sleep(1.5)
        os.system("cls" if os.name == "nt" else "clear")

        print("Esperando o Cliente")
        time.sleep(1.5)
        os.system("cls" if os.name == "nt" else "clear")

        while True:
            pacotes_recebidos = client_socket.recv(100000).decode()
            print(f"Mensagem do Cliente: {pacotes_recebidos}")
            
            if pacotes_recebidos.lower().strip() == "tchau":
                print("Fim da conexão")
                break
            
            mensagem_servidor = input("Mensagem do Servidor: ")
            client_socket.send(mensagem_servidor.encode()) 
            
            if mensagem_servidor.lower().strip() == "tchau":
                print("Fim da conexão")
                break

        client_socket.close()
        break  # Sai do loop principal após fechar a conexão

    except ValueError:
        print("Por favor, insira um número válido para a porta.")
    except Exception as error:
        print("Erro: ", error)

    cont = input("Você quer tentar novamente? [s/n]: ").lower()
    os.system("cls" if os.name == "nt" else "clear")

    if cont == "n":
        print("Programa finalizado!")
        break
