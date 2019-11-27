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
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def acceptIncommingConnections():
    """Venter på svar fra en client og giver dem en velkomst"""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to the server" + "Type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client, )).start

def handle_client(client): #Tager 'client' som et agument.
    """Står for den enkelte clients forbindelse"""
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = "Velkommen %s! Hvis du vil quite tryk {quit}" % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s har tilsluttet til serveren" % name
    brodcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            brodcast(msg, name+": ")
        else:
            client.send(bytes("{quit}","utf8"))
            client.close()
            del clients[client]
            brodcast(bytes("%s har forladt chatten" % name, "utf8"))
            break
def brodcast(msg, prefix=""):
    """Brodscaster en besked til alle personerne """
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


if __name__ == "__main__":
    SERVER.listen(5)
    print("venter på forbindelse")
    ACCEPT_THREAD = Thread(target=acceptIncommingConnections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
    
    
