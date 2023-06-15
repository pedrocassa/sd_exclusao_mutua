import socket

HOST = "localhost"
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main():
    mensagem = input("Digite uma mensagem para enviar ao servidor (ou 'sair' para encerrar): ")
    sock.sendto(mensagem.encode(), (HOST, PORT))
        
    sock.close()
    print("Cliente encerrado")

if __name__ == "__main__":
    main()