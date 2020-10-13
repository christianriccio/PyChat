from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

def receive_msg(): # Handles receiving of messages

    while True:
        try:
            msg = client_socket.recv(buffer_sz).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break

def send_msg(event=None):  # event is passed by binders.

    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{exit}":
        client_socket.close()
        top.quit()

def on_closing(event=None):

    my_msg.set("{exit}")
    send_msg()

top = tkinter.Tk()
top.title("CHAT ROOM")
messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Here we create the window for messaging.
msg_list = tkinter.Listbox(messages_frame, height=30, width=80, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send_msg)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send_msg)
send_button.pack()
top.protocol("WM_DELETE_WINDOW", on_closing)
# socket management
HOST = input('Enter host: ')
PORT = int(input('Enter port: '))
buffer_sz = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
receive_thread = Thread(target=receive_msg)
receive_thread.start()
tkinter.mainloop()  # Starts GUI