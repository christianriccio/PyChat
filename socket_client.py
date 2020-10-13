import socket  # importing the required module
import sys  # for exit the system

host = input("Isert host's Ip you would comunicate with: ")
port = int(input('Insert a valid port number: '))
response=''
run='yes'
while run == 'yes':
    try:
    # creating the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.socket function will create the socket and then return if such a descriptor in case we need it forward
# AF_INET represent the family of  addresses to use, in particular this would work with IPv4
# SOCK_STREAM this will set the Type of connection, meaning in thi case TCP connection
    except socket.error as msg:
        print('Error occours meanwhile creating socket.\n Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
        sys.exit()
# let's connect :)
    try:
        print("Trying contact the server")
        s.connect((host, port))
        print(f'You are connected to {host} ')
        print(s.recv(4096).decode('utf-8'))
    except socket.error:
        print('Hostname could not be found. Exiting')
        raise Exception("Corresponding hostname is not responding")
        sys.exit()


    message=input('Type here your text message: ')
    try:
        print("Sending message")
        s.send(message.encode())

    except socket.error:
    # Send failed
        print('Send failed')
        sys.exit()
    print('Message send successfully')

# let's recive a response
    response = s.recv(4096)
# the value as parameter in the function recv represents the buffer, or the quantity of data to be downloaded at time
#becouse in some cases the response could be passed in pieces, for get an entire text I put the while cycle
    if len(response) > 0:
        print(f"Server @ {host} says: ")
        print(response.decode('utf-8'))
        response = s.recv(4096)
    s.close()