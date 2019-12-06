#!/usr/bin/env python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

def receive():
   """Står for at receive beskeder"""
   while True:
        try:
            msg = client_socket_recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break 

def send(event=None):
    """Står for at sende beskeder"""
    msg = my_msg.get()
    my_msg.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def socket_closing(event=None):
    """Lukker Socket før GUI"""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chatter")

message_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar() # til at få beskederne sendt
my_msg.set("Skriv din besked her.")
scrollbar = tkinter.Scrollbar(message_frame) #Til at se forrige beskeder

msg_list = tkinter.Listbox(message_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()

message_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("VM_DELETE_WINDOW", socket_closing)



HOST = input("Enter host: ")
PORT = input("Enter port: ")

if not PORT:
    PORT = 33000
else:
    PORN = int(PORT)


BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()
