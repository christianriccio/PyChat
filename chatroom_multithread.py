from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def accept_incoming_connections(): # accepting connections
    while True: # the while loop will wait for ever for connections
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to the Chat Room !\n_Write your name in the box\n_Press ENTER ", "utf8"))
        addresses[client] = client_address # every client's address is stored into address dictionary
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):  # Takes client socket as argument, this function is for client mangement, here we want to handle a single connection
    name = client.recv(buffer_sz).decode("utf8")
    welcome = 'Welcome %s! At the moment, there are %s clients connected.' % (name, str(len(clients)))
    client.send(bytes(welcome, "utf8"))
    client.send(bytes("Type {exit} to exit", 'utf8'))
    msg = "%s has joined the chat!" % name # every client will receive a message for every new user that will join the chat
    broadcast_MESSAGES(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(buffer_sz)
        if msg != bytes("{exit}", "utf8"):
            broadcast_MESSAGES(msg, name + ": ")
        else:
            client.send(bytes("{exit}", "utf8")) # if the client type {quit} will automaticcaly be quitted from the chat by the server
            client.close()
            del clients[client] # naturraly the user that have quitted will be deleted from the client's list
            broadcast_MESSAGES(bytes("%s has left the chat." % name, "utf8"))
            break



def broadcast_MESSAGES(msg, prefix=""):  # prefix is for name identification, here we also send a message from the user to all the other partecipants to the chatroom

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)

clients = {}
addresses = {}
HOST = ''
PORT = 15102
buffer_sz = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection from users !!!")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()