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


import socket
import os

server_ip = "127.0.0.1"
port = 8000
size = 1024
form = "utf-8"

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))
    print("Connected to server")

    while True:
        action = input("Enter 'upload' to upload a file, 'download' to download a file, or 'quit' to exit: ")
        if action == "upload":
            upload(client)
        elif action == "download":
            download(client)
        elif action == "quit":
            break
        else:
            print("Invalid action. Please try again.")

    client.close()
    print("Connection to server closed")

def upload(client):
    filepath = input("Enter the filepath you want to upload: ")
    with open(filepath, "r") as file:
        data = file.read()
    client.send("upload".encode(form))
    client.send(os.path.basename(filepath).encode(form))
    response = client.recv(size).decode(form)
    print(response)
    client.send(data.encode(form))
    print("File uploaded successfully")

def download(client):
    filename = input("Enter the filename you want to download: ")
    client.send("download".encode(form))
    client.send(filename.encode(form))
    data = client.recv(size).decode(form)
    with open(filename, "w") as file:
        file.write(data)
    print("File downloaded successfully")

run_client()