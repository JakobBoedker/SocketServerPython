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
        top.close()


def socket_closing(event=None):
    """Lukker Socket før GUI"""
    my_msg.set("{quit}")
    send()
