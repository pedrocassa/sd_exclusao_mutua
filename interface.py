import socket
import threading
from datetime import datetime

HOST = "localhost"
PORT = 12345
MESSAGE = "REQUEST"
MESSAGE2 = "RELEASE"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

interfacetext = open("InterfaceLog.txt", 'w')

def start_interface():
    print("Selecione a ação desejada: ")
        
    option = input("1 - Imprimir fila atual de pedidos\n2 - Imprimir quantidade de vezes que cada processo foi atendido\n3 - Encerrar execução\n")
    
    if option == "1":
        data_e_hora_atuais = datetime.now()
    
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                                                       
    
        interfacetext.write(data_e_hora_em_texto+":"+str(MESSAGE.encode())+'\n')
        sock.sendto(MESSAGE.encode(), (HOST, PORT))
        return True
        
    elif option == "2":
        pass
    
    elif option == "3":
        
        data_e_hora_atuais = datetime.now()
    
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                                                       
    
        interfacetext.write(data_e_hora_em_texto+":"+str(MESSAGE2.encode())+'\n')
        sock.sendto(MESSAGE2.encode(), (HOST, PORT))
        return False
        


def main():    
    RUNNING = True
    while RUNNING:
        RUNNING = start_interface()
          
    sock.close()
    print("Execução encerrada")
    interfacetext.close()

if __name__ == "__main__":
    main()