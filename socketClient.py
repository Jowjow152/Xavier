import socket
import threading
import time

class socketClient:
    HOST, PORT = "localhost", 1234

    

    def __init__(self):
        self.s = socket.socket() 
        self.s.connect((self.HOST, self.PORT))
        self.thread_recieve = threading.Thread(target=self.recieveMessage)
        self.thread_recieve.start()

    def sendMessage(self, message):
        self.s.sendall(bytes(message, "utf-8"))
        #To-do: criar função para enviar mensagens para o servidor

    def recieveMessage(self):
        while True:
            print(self.s.recv(1024).strip())

    def closeConnection(self):
        self.s.close()

    #received = str(socket.recv(1024), "utf-8")
    
   
    #print("Received: {}".format(received))


if __name__ == "__main__":
    client = socketClient()
    client.sendMessage("hello world 1")
    time.sleep(1)
    client.sendMessage("hello world 2")
    time.sleep(1)
    client.sendMessage("hello world 3")
    client.closeConnection()
    