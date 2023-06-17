import socket
import threading
from twoPhaseLocking import TwoPhaseLocking
from logger import write_log
from message import create_message, get_values_from_message

HOST = "localhost"
PORT = 12345
REQUEST_MESSAGE = "REQUEST"
GRANTED_MESSAGE = "GRANTED"
RELEASE_MESSAGE = "RELEASE"
LOG_FILE_NAME = "coordinatorLog.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

tpl = TwoPhaseLocking()
Q = []

print("Coordenador esperando por requisições...")

def mutual_exclusion(received_message):
    if received_message == REQUEST_MESSAGE:
        if len(Q) == 0:
            new_message = create_message(receiver, sender, GRANTED_MESSAGE)
            sock.sendto(new_message.encode(), (addr))
        Q.append({
            "addr": addr,
            "id": sender,
        })
        
    elif received_message == RELEASE_MESSAGE:
        Q.pop(0)
        if len(Q) > 0:
            process = str(Q[0])
            new_message = create_message(receiver, process.id, GRANTED_MESSAGE)
            sock.sendto(new_message.encode(), (process.addr))

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode()
    
    sender, receiver, received_message = get_values_from_message(str(message))
    
    print(received_message)
    
    write_log(LOG_FILE_NAME, str(received_message))

    if received_message == "END":
        break
        
    mutual_exclusion_thread = threading.Thread(target=mutual_exclusion(received_message))
    
    mutual_exclusion_thread.start()
    
    mutual_exclusion_thread.joint()
    

sock.close()
print("Programa encerrado")

