from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
from threading import Thread
import json
from sqlConnector import DbConnector

def incomming_connections():

    while True:

        client, addr = SERVER.accept()
        print(f'A client has connected {client} {addr}')
        
        Thread(target=single_client, args=(client,)).start()

def broadcast_msg(msg):

    print(msg)
    conn.createMessage(msg["text"],msg["userId"],msg["date"])
    for client in clients:
        client.send((json.dumps(msg)).encode())

def single_client(client):

    client_name = 'Anonymous'
    clients[client] = client_name

    while True:
        msg = client.recv(BUFFERSIZE).strip()
        if msg == EXIT_CMD.encode('utf8'):
            print(f'{clients[client]} has disconnected ')
            client.close()
            del clients[client]
            break
        else:
            msg = json.loads(msg)
            broadcast_msg(msg)

if __name__ == "__main__":

    clients = {}

    conn = DbConnector()

    HOST = '127.0.0.1'
    PORT = 1234
    BUFFERSIZE = 1024
    ADDR = (HOST, PORT)
    EXIT_CMD = "exit()"
    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    SERVER.bind(ADDR)
    SERVER.listen(2)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=incomming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
            
   