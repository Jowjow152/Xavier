from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
from threading import Thread
import json

def incomming_connections():

    while True:

        client, addr = SERVER.accept()
        print(f'A client has connected {addr}')
        
        Thread(target=single_client, args=(client,)).start()

def broadcast_msg(msg, name=""):

    print(msg)
    for client in clients:
        client.send((json.dumps(msg)).encode())

def get_clients():
    
    real_clients_num = 0
    real_clients_name = []

    for k,v in clients.items():
        if v != 'Annonymous':
            real_clients_num += 1
            real_clients_name.append(v)

    return real_clients_num, real_clients_name
        

def single_client(client):

    client_name = 'Anonymous'
    clients[client] = client_name

    while True:
        msg = client.recv(BUFFERSIZE).strip()
        print(msg)
        
        if msg == 'online()'.encode('utf8'):            
            real_clients_num, real_clients_name = get_clients()
            client.send(f'Online users {real_clients_num} : {real_clients_name}'.encode('utf8'))
        elif NAME_CMD.encode('utf8') in msg:
            new_client_name = msg.decode('utf8').replace(NAME_CMD + ' ', '')
            clients[client] = new_client_name
        elif msg == EXIT_CMD.encode('utf8'):
            print(f'{clients[client]} has disconnected ')
            client.close()
            client_leaving = clients[client]
            del clients[client]
            broadcast_msg(f'{client_leaving} has left the room!'.encode())
            break
        else:
            msg = json.loads(msg)
            broadcast_msg(msg, clients[client] + ': ')

if __name__ == "__main__":

    clients = {}

    HOST = '127.0.0.1'
    PORT = 1234
    BUFFERSIZE = 1024
    ADDR = (HOST, PORT)
    EXIT_CMD = "exit()"
    NAME_CMD = "name()"
    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    SERVER.bind(ADDR)
    SERVER.listen(2)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=incomming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
            
   