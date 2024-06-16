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

        


class Keyboard:
    def __init__(self) -> None:
        pass 
    
    def listen_to_click(event):
        key_pressed = []
        if event.event_type == keyboard.KEY_DOWN:
            key_pressed.append(event.name)
        #send key_pressed with socket
        key_pressed.clear()    

    
class Mouse:
    def __init__(self) -> None:
        pass
    
    def on_click(event):
        click_positions = []
        kindOfClick = ""
        if event.event_type == mouse.UP and event.button == mouse.LEFT:
            click_positions.append(event.x, event.y)
            kindOfClick = "left"
        elif event.event_type == mouse.UP and event.button == mouse.RIGHT:
            click_positions.append(event.x,event.y)
            kindOfClick = "right"
        #send clickpositions and kindofclick with the socket    
        click_positions.clear()
    mouse.hook(on_click)      

    def scroll_wheel(event):
        scroll_positions = []
        scroll_delta = []
        if event.event_type == mouse.wheel:
            scroll_positions.append(event.x,event.y)
            scroll_delta.append(event.delta)
        #send delta and positions with socket
        scroll_delta.clear()
        scroll_positions.clear()
    mouse.hook(scroll_wheel)    

class Screenshots:
    def __init__(self) -> None:
        pass


