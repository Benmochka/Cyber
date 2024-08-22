import socket
import threading
import keyboard
import mouse
from PIL import Image
import io

size = 1024
form = "utf-8"
server_ip = "127.0.0.1"
keyboard_port = 5000
mouse_port = 5001
screen_port = 5002
encode = 'utf-8'

class KeyboardServer:
    def __init__(self, server_ip, keyboard_port) -> None:
        self.server_ip = server_ip
        self.keyboard_port = keyboard_port
        self.tcp_kb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_kb_socket.bind((self.server_ip, self.keyboard_port))
        self.tcp_kb_socket.listen(1)
        self.client_socket, self.client_address = self.tcp_kb_socket.accept()

    def listen_to_click(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            self.client_socket.sendall(event.name.encode(encode))

    def start_listening(self):
        keyboard.hook(self.listen_to_click)
        keyboard.wait()

keyboard_listener = KeyboardServer(server_ip, keyboard_port)
keyboard_thread = threading.Thread(target=keyboard_listener.start_listening)
keyboard_thread.start()

try:
    keyboard_thread.join()
except KeyboardInterrupt:
    print("Terminating...")
    keyboard.unhook_all()
    keyboard_listener.client_socket.close()
    keyboard_listener.tcp_kb_socket.close()

class MouseServer:
    def __init__(self, server_ip, mouse_port) -> None:
        self.server_ip = server_ip
        self.mouse_port = mouse_port
        self.tcp_ms_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_ms_socket.bind((self.server_ip, self.mouse_port))
        self.tcp_ms_socket.listen(1)
        self.client_socket, self.client_address = self.tcp_ms_socket.accept()

    def on_click(self, event):
        if event.event_type == mouse.is_pressed("right"):
            position = mouse.get_position()
            click = "right"
            self.client_socket.sendall(click.encode(encode))
            self.client_socket.sendall(position.encode(encode))
        if event.event_type == mouse.is_pressed("left"):
            position = mouse.get_position()
            click = "left"
            self.client_socket.sendall(click.encode(encode))
            self.client_socket.sendall(position.encode(encode))

    def on_scroll(self, event):
        if event.event_type == mouse.scroll
        self.client_socket.sendall(message.encode(encode))

    def start_listening(self):
        mouse_listener = mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll)
        mouse_listener.start()
        mouse_listener.join()

mouse_listener = MouseServer(server_ip, mouse_port)
mouse_thread = threading.Thread(target=mouse_listener.start_listening)
mouse_thread.start()

try:
    mouse_thread.join()
except KeyboardInterrupt:
    print("Terminating...")
    mouse_listener.client_socket.close()
    mouse_listener.tcp_ms_socket.close()

class ScreenshotsServer:
    def __init__(self, server_ip, port):
        self.port = port
        self.server_ip = server_ip
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind((self.server_ip, self.port))

    def recv_and_show(self):
        while True:
            data, addr = self.udp_socket.recvfrom(65536)
            byte_arr = io.BytesIO(data)
            image = Image.open(byte_arr)
            image.show()

screenshots_receiver = ScreenshotsServer(server_ip, screen_port)
screenshots_thread = threading.Thread(target=screenshots_receiver.recv_and_show)
screenshots_thread.start()

try:
    screenshots_thread.join()
except KeyboardInterrupt:
    print("Terminating...")
    screenshots_receiver.udp_socket.close()