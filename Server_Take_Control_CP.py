import socket
import threading
import keyboard
import mouse
from PIL import Image

size = 1024
form = "utf-8" 
server_ip = "127.0.0.1"
keyboard_port = 5000
mouse_port = 5001
screen_port = 5002
encode = 'utf-8'


class Keyboard:
    def __init__(self, server_ip, keyboard_port) -> None:
        self.server_ip = server_ip
        self.keyboard_port = keyboard_port
        self.tcp_kb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_kb_socket.bind((self.server_ip, self.keyboard_port))
        self.tcp_kb_socket.listen(1)
        self.client_socket, self.client_address = self.tcp_kb_socket.accept()

    def listen_to_click(self,event):
        if event.event_type == keyboard.KEY_DOWN:
            self.client_socket.sendall(event.name.encode(encode))

    def start_listening(self):
        keyboard.hook(self.listen_to_click)
        keyboard.wait()



keyboard_listener = Keyboard(server_ip, keyboard_port)
keyboard_thread = threading.Thread(target = keyboard_listener.start_listening)
keyboard_thread.start()

try:
    keyboard_thread.join()
except KeyboardInterrupt:
    print("Terminating...")
    keyboard.unhook_all()
    keyboard_listener.client_socket.close()
    keyboard_listener.tcp_kb_socket.close()
    
class Mouse:
    def __init__(self, server_ip, mouse_port) -> None:
        self.server_ip = server_ip
        self.mouse_port = mouse_port
        self.tcp_ms_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_ms_socket.bind(server_ip, mouse_port)
        self.tcp_ms_socket.listen(1)
        self.client_socket, self_client_address = self.tcp_ms_socket.accept()
        self.kindOfClick = ""
    
    def on_click(self, event):
        if event.event_type == mouse.UP and event.button == mouse.LEFT:
            self.client_socket.sendall(event.x.encode(encode),event.y.encode(encode))
            kindOfClick = "left"
            self.client_socket.sendall(kindOfClick.encode(encode))
        elif event.event_type == mouse.UP and event.button == mouse.RIGHT:
            self.client_socket.sendall(event.x.encode(encode),event.y.encode(encode))
            kindOfClick = "right"
            self.client_socket.sendall(kindOfClick.encode(encode))   
       
    def scroll_wheel(self, event):
        if event.event_type == mouse.wheel:
            self.client_socket.sendall(event.x.encode(encode),event.y.encode(encode))
            self.client_socket.sendall(event.delta.encode(encode))
    
    def start_listening(self):
        mouse.hook(self.on_click)
        mouse.hook(self.scroll_wheel)
        mouse.wait

mouse_listener = Mouse(server_ip, mouse_port)      
mouse_thread = threading.Thread(target = mouse_listener.start_listening)
mouse_thread.start()

try:
    mouse_thread.join()
except KeyboardInterrupt:
    print("Terminating...")
    keyboard.unhook_all()
    mouse_listener.client_socket.close()
    mouse_listener.tcp_ms_socket.close()

class Screenshots:
    def __init__(self) -> None:
        pass
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(server_ip, screen_port)

    def recv_and_show(screenshot):
        #recv the image from the socket
        image.show()


