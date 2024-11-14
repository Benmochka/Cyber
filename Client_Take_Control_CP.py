import socket
<<<<<<< HEAD
import keyboard
import PIL
import win32api


class Network:
    def __init__(self) -> None:
        pass


class Keyboard:
    def __init__(self) -> None:
        pass 

class Mouse:
    def __init__(self) -> None:
        pass

class Screenshots:
    def __init__(self) -> None:
        pass
=======
import threading
import keyboard
import mouse
import pyautogui
import io
import time

class KeyboardClient:
    def __init__(self, server_ip, keyboard_port) -> None:
        self.server_ip = server_ip
        self.keyboard_port = keyboard_port
        self.tcp_kb_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_kb_client.connect((self.server_ip, self.keyboard_port))

    def press_key(self, event):
        keyboard.press_and_release(event)

    def start_receiving(self):
        while True:
            data = self.tcp_kb_client.recv(1024)
            if not data:
                break
            event = data.decode('utf-8')
            self.press_key(event)
        self.tcp_kb_client.close()

keyboard_client = KeyboardClient('127.0.0.1', 5000)
client_thread = threading.Thread(target=keyboard_client.start_receiving)
client_thread.start()

try:
    client_thread.join()
except KeyboardInterrupt:
    print("Terminating...")
    keyboard_client.tcp_kb_client.close()

class MouseClient:
    def __init__(self, server_ip, mouse_port) -> None:
        self.server_ip = server_ip
        self.mouse_port = mouse_port
        self.tcp_ms_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_ms_client.connect((self.server_ip, self.mouse_port))

    def move_and_click(self, click_pos, kindofclick):
        mouse.move(click_pos[0], click_pos[1], absolute=True, duration=0.2)
        if kindofclick == "left":
            mouse.click('left')
        if kindofclick == "right":
            mouse.click('right')

    def move_and_scroll(self, scroll_pos, scrollDelta):
        mouse.move(scroll_pos[0], scroll_pos[1], absolute=True, duration=0.2)
        mouse.wheel(scrollDelta)

    def start_receiving(self):
        while True:
            data = self.tcp_ms_client.recv(1024)
            if not data:
                break
            parts = data.decode('utf-8').split(',')
            if parts[0] == 'click':
                self.move_and_click((int(parts[1]), int(parts[2])), parts[3])
            elif parts[0] == 'scroll':
                self.move_and_scroll((int(parts[1]), int(parts[2])), int(parts[3]))
        self.tcp_ms_client.close()

mouse_client = MouseClient('127.0.0.1', 5001)
mouse_thread = threading.Thread(target=mouse_client.start_receiving)
mouse_thread.start()

try:
    mouse_thread.join()
except KeyboardInterrupt:
    print("Terminating...")
    mouse_client.tcp_ms_client.close()

class ScreenshotsClient:
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

screenshots_sender = ScreenshotsClient('127.0.0.1', 5002)
screenshots_thread = threading.Thread(target=screenshots_sender.take_and_send)
screenshots_thread.start()

try:
    screenshots_thread.join()
except KeyboardInterrupt:
    print("Terminating...")
    screenshots_sender.udp_socket.close()
>>>>>>> cc5eeb87c2a585af5623dcfd95615445c1a752ae
