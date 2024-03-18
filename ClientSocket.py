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