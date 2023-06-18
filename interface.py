import socket
import threading
from logger import write_log
from collections import Counter
import numpy as np

HOST = "localhost"
PORT = 12345
REQUEST_MESSAGE = "REQUEST"
GRANTED_MESSAGE = "GRANTED"
RELEASE_MESSAGE = "RELEASE"
END_MESSAGE = "END"
LOG_FILE_NAME = "interfaceLog.txt"


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def start_interface(Q, fullfilled_processes):


    print("Selecione a ação desejada: ")
        
    option = input("1 - Imprimir fila atual de pedidos\n2 - Imprimir quantidade de vezes que cada processo foi atendido\n3 - Encerrar execução\n")
    
    if option == "1":
        print(Q)
        
    elif option == "2":
        
        Keys = Counter(fullfilled_processes).keys()
        Counts = Counter(fullfilled_processes).values()
        print("Processo: ",Keys)
        print("Contagem: ", Counts)
    
    elif option == "3":
        return END_MESSAGE
        


def main():    
    RUNNING = True
    while RUNNING:
        RUNNING = start_interface()
          
    sock.close()
    print("Execução encerrada")

if __name__ == "__main__":
    main()
