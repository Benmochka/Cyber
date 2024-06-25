import socket
import threading
import keyboard
import mouse
import pyautogui
import time
import io

size = 1024
form = "utf-8" 
server_ip = "127.0.0.1"
keyboard_port = 5000
mouse_port = 5001
screen_port = 5002
encode = 'utf-8'

class Networks:
    def __init__(self) -> None:
        pass


class Keyboard:
    def __init__(self, server_ip, keyboard_port) -> None:
        self.server_ip = server_ip
        self.keyboard_port = keyboard_port
        self.tcp_kb_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_kb_client.connect(self.server_ip, self.keyboard_port)

    def press_key(event):
        keyboard.press_and_release(event)

    def start_receiving(self):
        while True:
            data = self.tcp_kb_client.recv(1024)
            if not data:
                break
            event = data.decode('utf-8')
            self.press_key(event)
        self.tcp_kb_client.close()


# Create an instance of the KeyboardClient class
keyboard_client = Keyboard(server_ip, keyboard_port)
client_thread = threading.Thread(target=keyboard_client.start_receiving)
client_thread.start()

try:
    client_thread.join()
except KeyboardInterrupt:
    print("Terminating...")
    keyboard_client.tcp_kb_client.close() 

class Mouse:
    def __init__(self, server_ip, mouse_port) -> None:
        self.server_ip = server_ip
        self.mouse_port = mouse_port
        self.tcp_ms_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_ms_client.connect(self.server_ip, self.mouse_port)
    
    def moveAndClick(click_pos,kindofclick):
        mouse.move(click_pos[0], click_pos[1],absolute=True,duration = 0.2)
        if kindofclick == "left":
            mouse.click('left')
        if kindofclick == "right":
            mouse.click('right')  

    def moveAndScroll(scroll_pos,scrollDelta):
        mouse.move(scroll_pos[0], scroll_pos[1],absolute=True,duration=0.2)
        mouse.wheel(scrollDelta)

class Screenshots:
    def __init__(self, server_ip, port):
        self.server_ip = server_ip
        self.port = port
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def take_and_send(self):
        while True:
            scrshot = pyautogui.screenshot()
            byte_arr = io.BytesIO()
            scrshot.save(byte_arr, format='PNG')
            self.udp_socket.sendto(byte_arr.getvalue(), (self.server_ip, self.port))
            time.sleep(1)

screenshots_sender = Screenshots(server_ip, screen_port)
screenshots_thread = threading.Thread(target = screenshots_sender.take_and_send())
screenshots_thread.start()

screenshots_thread.join()
