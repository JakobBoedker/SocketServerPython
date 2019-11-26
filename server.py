#!/usr/bin/env python3

"""Server for Multitrådet Chatprogram. """

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}


HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_NET, SOCK_STREAM)
SERVER.bind(ADDR)


def acceptIncommingConnections():
    """Venter på svar fra en client og giver dem en velkomst"""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to the server" + "Type your name and press enter!", "utf-8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client, )).start

def handle_client(client): #Tager 'client' som et agument.
    """Står for den  som et .
