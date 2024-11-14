import socket
import keyboard
import tkinter
import PIL
import win32api
import mouse

size = 1024
form = "utf-8" 

class Network:
    def __init__(self) -> None:
        pass

    def run_server():
        server_ip = "127.0.0.1"
        port = 8000
        
        server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        server_tcp.bind((server_ip, port))
        server_tcp.listen(1)
        print("Server is listening on {}:{}".format(server_ip, port))


class Keyboard:
    def __init__(self) -> None:
        pass 
    
    def listen_to_click(keyboard_click):
        if keyboard.is_pressed():
            keyboard_click
    
class Mouse:
    def __init__(self) -> None:
        pass
    
    def move_mouse():
        mouse.get_position()

class Screenshots:
    def __init__(self) -> None:
        pass


