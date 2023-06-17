import socket
import threading
from message import create_message, get_values_from_message
from thread_id import get_new_thread_id
from twoPhaseLocking import TwoPhaseLocking

HOST = "localhost"
PORT = 12345
REQUEST_MESSAGE = "REQUEST"
GRANTED_MESSAGE = "GRANTED"
RELEASE_MESSAGE = "RELEASE"
LOG_FILE_NAME = "clientLog.txt"
SLEEP_TIME = 1000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tpl = TwoPhaseLocking()

def receive_message(id):
    data, addr = sock.recvfrom(1024)
    message = data.decode()
    
    sender, received_message = get_values_from_message(str(message))
    
    if received_message == GRANTED_MESSAGE:
        tpl.start_transaction("T1")
    
        tpl.write_item("T1", id, received_message)

        tpl.end_transaction("T1")
        
        new_message = create_message(sender, RELEASE_MESSAGE)

        sock.sendto(new_message.encode(), (HOST, PORT))    

def main():
    r = 5
    
    while(r > 0):
        new_thread_id = get_new_thread_id()
        
        m = create_message(new_thread_id, REQUEST_MESSAGE)
        
        sock.sendto(m.encode(), (HOST, PORT))
        
        thread1 = threading.Thread(target=receive_message(new_thread_id))

        thread1.start()
            
        thread1.join()
        
        r = r - 1
    
    sock.close()    
    print("Cliente encerrado")

if __name__ == "__main__":
    main()