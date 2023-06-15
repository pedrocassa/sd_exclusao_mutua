import socket
import threading
from twoPhaseLocking import TwoPhaseLocking
from datetime import datetime

HOST = "localhost"
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

tpl = TwoPhaseLocking()

def doSomething():
    # Iniciar uma transação
    tpl.start_transaction("T1")

    
    # Ler um item
    valor = tpl.read_item("T1", "item1")
    arquivo.write('-->'+valor+'\n')
    print(valor)

    # Escrever um item
    tpl.write_item("T1", "item1", "novo_valor")

    # Encerrar uma transação
    tpl.end_transaction("T1")

def coordenador():
    # Criar as threads
    thread1 = threading.Thread(target=doSomething)
    

    # Iniciar as threads
    thread1.start()
    

    # Aguardar as threads finalizarem
    thread1.join()

    print("Todas as threads encerradas")

print("Coordenador esperando por requisições...")

arquivo = open("CoordinatorLog.txt", 'w')

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode()
    

    data_e_hora_atuais = datetime.now()
    
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                                                       
    arquivo.write(data_e_hora_em_texto+":"+str(message))

    print(message)
    
    if message == "REQUEST":
        coordenador()
        
            
    elif message == "GRANT":
        break

    elif message == "RELEASE":
        break


sock.close()
print("Programa encerrado")
arquivo.close()
