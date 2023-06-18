import threading
from client import Client


cl = Client()
def main():    
    RUNNING = 0
    while RUNNING<3:
        thread1 = threading.Thread(target=cl.main(RUNNING))
        thread2 = threading.Thread(target=cl.main(RUNNING))
        thread3 = threading.Thread(target=cl.main(RUNNING))
        
        thread1.start()

        thread2.start()

        thread3.start()
        
        
        thread1.join()
        
        thread2.join()

        thread3.join()

        RUNNING +=1
          
    
    print("Execução encerrada")

if __name__ == "__main__":
    main()
