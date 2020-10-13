import socket
import sys

serverPort = 15102
ip = ''
try:
    # creating the socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print(
        'Error occours meanwhile creating Server Socket.\nError code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit()
print('Server socket created')

try:
    # now bind the socket to the port and our ip
    serverSocket.bind((ip, serverPort))
except socket.error as msg:
    print(f'Failed to bimd the port {serverPort}\nError code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit()
print(f'Server is now binded @ port {serverPort}')
try:
    serverSocket.listen(1)  # server can handle one connection
except socket.error:
    print('Server is not ready to listen')
    sys.exit()
print('Server is now ready to listen and can handle one connection!')

while 1:  # infinity loop for let the server accept every sent message from the client
    k = 0
    connectSocket, addr = serverSocket.accept()
    if k == 0:
        welcome = f'welcome {addr[0]} to Chris & Gia server !!!'
    k += 1
    connectSocket.send(welcome.encode())
    sentence = connectSocket.recv(1024).decode()
    print(sentence)
    response = input('Write here: ')
    connectSocket.send(response.encode())
    connectSocket.close()

serverSocket.close()
