import socket
import keyboard
import PIL
import win32api
import mouse


class Network:
    def __init__(self) -> None:
        pass


class Keyboard:
    def __init__(self) -> None:
        pass 

    def press_key(event):
        keyboard.press_and_release(event)

class Mouse:
    def __init__(self) -> None:
        pass
    
    def moveAndClick(click_pos,kindofclick):
        mouse.move(click_pos[0],click_pos[1],absolute=True,duration = 0.2)
        if kindofclick == "left":
            mouse.click('left')
        if kindofclick == "right":
            mouse.click('right')    
    def moveAndScroll(scroll_pos,scrollDelta):
        mouse.move(scroll_pos[0], scroll_pos[1],absolute=True,duration=0.2)
        mouse.wheel(scrollDelta)
class Screenshots:
    def __init__(self) -> None:
        pass