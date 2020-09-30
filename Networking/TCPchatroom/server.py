import threading
import socket

host = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
  for client in clients:
    client.send(message)

def handle(client):
  while True:
    try:
      # try to receive a message from the client, then broadcast the message
      message = client.recv(1024)
      broadcast(message)
    except:
      # get the index of the list, then remove it
      index = clients.index(client)
      clients.remove(client)
      client.close()
      # get the index of the nickname, then remove it
      nickname = nicknames[index]
      broadcast(f"{nickname} left the chat".encode("ascii"))
      nicknames.remove(nickname)
      break

def receive():
  while True:
    # listen for clients
    client, address = server.accept()
    # print once a client connects
    print(f"Connected to {str(address)}")

    # send codeword NICK, to indicate client must send nickname
    client.send("NICK".encode("ascii"))
    # After client types nickname, server gets the nickname
    nickname = client.recv(1024).decode("ascii")
    nicknames.append(nickname)
    clients.append(client)

    print(f"Nickname of the client is {nickname}!")
    broadcast(f"{nickname} joined the chat!".encode("ascii"))
    client.send("Connected to the server!".encode("ascii"))

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()

print(f"Listening to port: {port}")
receive()