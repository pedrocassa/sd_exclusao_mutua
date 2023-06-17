import socket
import threading
from message import create_message, get_values_from_message
from logger import write_log

HOST = "localhost"
PORT = 12345
REQUEST_MESSAGE = "REQUEST"
GRANTED_MESSAGE = "GRANTED"
RELEASE_MESSAGE = "RELEASE"
LOG_FILE_NAME = "clientLog.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive_message():
    data, addr = sock.recvfrom(1024)
    message = data.decode()
    
    sender, receiver, received_message = get_values_from_message(str(message))
    
    if received_message == GRANTED_MESSAGE:
        write_log(LOG_FILE_NAME, sender + " - " + receiver + " - " + received_message)
        
        new_message = create_message(sender, receiver, RELEASE_MESSAGE)

        sock.sendto(new_message.encode(), (HOST, PORT))    

def main():
    m = create_message('1', "2", REQUEST_MESSAGE)
    
    sock.sendto(m.encode(), (HOST, PORT))
    
    thread1 = threading.Thread(target=receive_message())

    thread1.start()
        
    thread1.join()
 
    sock.close()
    
    print("Cliente encerrado")

if __name__ == "__main__":
    main()