import socket
import threading
from message import create_message, get_values_from_message

HOST = "localhost"
PORT = 12345
REQUEST_MESSAGE = "REQUEST"
GRANTED_MESSAGE = "GRANTED"
RELEASE_MESSAGE = "RELEASE"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def cord(message):
    sender, receiver, received_message = get_values_from_message(str(message))
    
    if received_message == GRANTED_MESSAGE:
        #AREA CRITICA
        
        mensagem = create_message(sender, receiver, RELEASE_MESSAGE)

        sock.sendto(mensagem.encode(), (HOST, PORT))

def main():
    mensagem = create_message("1", "2", REQUEST_MESSAGE)
    sock.sendto(mensagem.encode(), (HOST, PORT))

    data, addr = sock.recvfrom(1024)
    message = data.decode()

    thread1 = threading.Thread(target=cord(message))

    thread1.start()
        
    thread1.join()
 
    print(message)

    sock.close()
    
    print("Cliente encerrado")

if __name__ == "__main__":
    main()