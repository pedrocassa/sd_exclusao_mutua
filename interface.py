import socket
import threading
from logger import write_log

HOST = "localhost"
PORT = 12345
REQUEST_MESSAGE = "REQUEST"
GRANTED_MESSAGE = "GRANTED"
RELEASE_MESSAGE = "RELEASE"
LOG_FILE_NAME = "interfaceLog.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def start_interface():
    print("Selecione a ação desejada: ")
        
    option = input("1 - Imprimir fila atual de pedidos\n2 - Imprimir quantidade de vezes que cada processo foi atendido\n3 - Encerrar execução\n")
    
    if option == "1":
        write_log(LOG_FILE_NAME, REQUEST_MESSAGE.encode())
    
        sock.sendto(REQUEST_MESSAGE.encode(), (HOST, PORT))
        return True
        
    elif option == "2":
        pass
    
    elif option == "3":
        write_log(LOG_FILE_NAME, REQUEST_MESSAGE.encode())
        
        sock.sendto(RELEASE_MESSAGE.encode(), (HOST, PORT))
        return False
        


def main():    
    RUNNING = True
    while RUNNING:
        RUNNING = start_interface()
          
    sock.close()
    print("Execução encerrada")

if __name__ == "__main__":
    main()