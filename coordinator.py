import socket
import threading
from twoPhaseLocking import TwoPhaseLocking
from logger import write_log
from logger import write_int
from message import create_message, get_values_from_message
from thread_id import get_new_thread_id
from interface import start_interface

HOST = "localhost"
PORT = 12345
REQUEST_MESSAGE = "REQUEST"
GRANTED_MESSAGE = "GRANTED"
RELEASE_MESSAGE = "RELEASE"
END_MESSAGE = "END"
LOG_FILE_NAME = "coordinatorLog.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

tpl = TwoPhaseLocking()
Q = []
fullfilled_processes = []

print("Coordenador esperando por requisições...")

def interface(received_message, id, addr):
    pos_end =start_interface(Q, fullfilled_processes)
    print("Message: ",received_message)
    if pos_end == END_MESSAGE:
        new_message = create_message(id, END_MESSAGE)
        sock.sendto(new_message.encode(), (addr))
        write_log(LOG_FILE_NAME, END_MESSAGE)
        Q.append(addr)   
    else: 
        mutual_exclusion_thread = threading.Thread(target=mutual_exclusion(received_message, new_thread_id, addr))
    
        mutual_exclusion_thread.start()
    
        mutual_exclusion_thread.join()

def mutual_exclusion(received_message, id, addr):
    if received_message == REQUEST_MESSAGE:
        if len(Q) == 0:
            new_message = create_message(id, GRANTED_MESSAGE)
            sock.sendto(new_message.encode(), (addr))
            write_log(LOG_FILE_NAME, GRANTED_MESSAGE)            
        Q.append(addr)
        
    elif received_message == RELEASE_MESSAGE:
        fullfilled_processes.append(Q[0])
        Q.pop(0)
        if len(Q) > 0:
            process = str(Q[0])
            new_message = create_message(id, GRANTED_MESSAGE)
            sock.sendto(new_message.encode(), (process))
            write_log(LOG_FILE_NAME, GRANTED_MESSAGE)
    
    


while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode()
    
    print(message)
    
    sender, received_message = get_values_from_message(str(message))
    
    print(received_message)
    
    write_log(LOG_FILE_NAME, str(sender) + " - " + str(received_message))

    if received_message == "END":
        break
    
    new_thread_id = get_new_thread_id()
        
    mutual_exclusion_thread = threading.Thread(target=interface(received_message, new_thread_id, addr))
    
    mutual_exclusion_thread.start()
    
    mutual_exclusion_thread.join()

    
    
    
    

sock.close()
print("Programa encerrado")

