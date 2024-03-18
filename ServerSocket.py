import socket
import os

server_ip = "127.0.0.1"
port = 8000
size = 1024
form = "utf-8"

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, port))
    server.listen()
    print("Server is listening on {}:{}".format(server_ip, port))
    
    while True:
        client_socket, client_address = server.accept()
        print("Connected to client:", client_address)

        while True:
            action = client_socket.recv(size).decode(form)
            if action == "upload":
                down_from_client(client_socket)
            elif action == "download":
                up_to_client(client_socket)
            else:
                break

        client_socket.close()
        print("Connection to client closed")

def down_from_client(client_socket):
    filename = client_socket.recv(size).decode(form)
    complete_filename = os.path.join(r"C:\Users\Lenovo\Desktop\ServerFiles", filename)
    with open(complete_filename, "w") as file:
        client_socket.send("Filename received.".encode(form))
        data = client_socket.recv(size).decode(form)
        file.write(data)
    print("File received and saved:", filename)

def up_to_client(client_socket):
    filename = client_socket.recv(size).decode(form)
    completename = os.path.join(r"C:\Users\Lenovo\Desktop\ServerFiles", filename)
    with open(completename, 'r') as file:
        data = file.read()
        client_socket.send(data.encode(form))
    print("File sent:", filename)

run_server()
