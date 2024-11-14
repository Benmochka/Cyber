# Server Code (Controlled Machine)
import socket
import threading
import pyautogui
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController, Button
from PIL import ImageGrab
import io
import time
import cv2
import numpy as np

class RemoteServer:
    def __init__(self, ip="0.0.0.0"):
        self.ip = ip
        self.keyboard = KeyboardController()
        self.mouse = MouseController()

    def start(self):
        threading.Thread(target=self.mouse_server).start()
        threading.Thread(target=self.keyboard_server).start()
        threading.Thread(target=self.screen_server).start()

    def mouse_server(self):
        mouse_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mouse_socket.bind((self.ip, 5001))
        mouse_socket.listen(1)
        conn, addr = mouse_socket.accept()
        print("Mouse connected by", addr)
        
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            command = data.split(",")
            if command[0] == "move":
                x, y = command[1], command[2]
                self.mouse.position = (int(x), int(y))
            elif command[0] == "click":
                button = Button.left if command[1] == "left" else Button.right
                self.mouse.click(button)
            elif command[0] == "scroll":
                dx, dy = int(command[1]), int(command[2])
                self.mouse.scroll(dx, dy)

    def keyboard_server(self):
        keyboard_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        keyboard_socket.bind((self.ip, 5002))
        keyboard_socket.listen(1)
        conn, addr = keyboard_socket.accept()
        print("Keyboard connected by", addr)
        
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            self.keyboard.press(data)
            self.keyboard.release(data)

    def screen_server(self):
        screen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        screen_socket.bind((self.ip, 5003))
        screen_socket.listen(1)
        conn, addr = screen_socket.accept()
        print("Screen connected by", addr)
        
        while True:
            screenshot = ImageGrab.grab()
            with io.BytesIO() as buf:
                screenshot.save(buf, format='JPEG')
                screen_data = buf.getvalue()
            
            conn.sendall(len(screen_data).to_bytes(4, 'big'))
            conn.sendall(screen_data)
            time.sleep(1)

class RemoteClient:
    def __init__(self, server_ip):
        self.server_ip = server_ip

    def start(self):
        threading.Thread(target=self.mouse_client).start()
        threading.Thread(target=self.keyboard_client).start()
        threading.Thread(target=self.screen_client).start()

    def mouse_client(self):
        mouse_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mouse_socket.connect((self.server_ip, 5001))
        
        while True:
            x, y = pyautogui.position()
            mouse_socket.sendall(f"move,{x},{y}".encode())
            if pyautogui.mouseDown():
                mouse_socket.sendall("click,left".encode())
            if pyautogui.mouseUp():
                mouse_socket.sendall("click,right".encode())
            scroll_x, scroll_y = pyautogui.scroll()
            if scroll_x != 0 or scroll_y != 0:
                mouse_socket.sendall(f"scroll,{scroll_x},{scroll_y}".encode())
            time.sleep(0.01)

    def keyboard_client(self):
        keyboard_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        keyboard_socket.connect((self.server_ip, 5002))
        
        def on_press(key):
            try:
                keyboard_socket.sendall(key.char.encode())
            except AttributeError:
                pass
        
        from pynput import keyboard
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def screen_client(self):
        screen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        screen_socket.connect((self.server_ip, 5003))
        
        while True:
            length = int.from_bytes(screen_socket.recv(4), 'big')
            screen_data = b''
            while len(screen_data) < length:
                packet = screen_socket.recv(length - len(screen_data))
                if not packet:
                    break
                screen_data += packet
            
            img_array = np.frombuffer(screen_data, dtype=np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            
            cv2.imshow('Remote Screen', img)
            if cv2.waitKey(1) == 27:
                break

        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Start server or client based on the role
    role = input("Enter 'server' to start as server, 'client' to start as client: ").strip().lower()
    if role == 'server':
        server = RemoteServer()
        server.start()
    elif role == 'client':
        server_ip = input("Enter the server IP address: ").strip()
        client = RemoteClient(server_ip)
        client.start()
    else:
        print("Invalid role. Please enter 'server' or 'client'.")
