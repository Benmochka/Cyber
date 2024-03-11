import requests
import os

def scanFileAtVT(file_path):
    ##sending the file for scanning
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': '453af95ed16995efc1d0894c5df35a4e9374de3792225c4a48f46c1f484afbb7'}
    files = {'file': (file_path, open(file_path, 'rb'))}
    response = requests.post(url, files=files, params=params)
    response_json = response.json()
    if response.status_code != 200:
        print("Error submitting file for scanning")
    
    ##sending the response to get the report
    sha256 = response_json['sha256']
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    params = {'apikey': '453af95ed16995efc1d0894c5df35a4e9374de3792225c4a48f46c1f484afbb7', 'resource':sha256}
    response1 = requests.get(url, params=params)
    data = response1.json()

    ##printing how many sources found it malicious
    try:
        countpos = 0
        counttotal = 0
        for i in data['scans']:
            counttotal += 1
            if(data['scans'][i]['detected'] == True):
                countpos += 1
        return f'{countpos} sources out of {counttotal} found ' + os.path.basename(file_path) + ' malicious'
    except KeyError:
        return "The file couldn't be scanned"     

def getFiles(path):
    for filename in os.listdir(path):
        print("--" + filename)
        fullname = os.path.join(path, filename)
        if os.path.isdir(fullname): 
            getFiles(fullname)
        else:
            scanFileAtVT(fullname) 


import tkinter as tk
from tkinter import filedialog
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def select_file():
    file_path = filedialog.askopenfilename()
    return file_path
def AtClick():
    file_path = file_path_var.get()
    if file_path:
        if os.path.isdir(file_path):
            result = getFiles(file_path)
            result = str(result) 
            result_text.delete('1.0', tk.END)  
            result_text.insert(tk.END, result)
        elif os.path.isfile(file_path):
            result = scanFileAtVT(file_path)
            result = str(result)  # Convert the result to a string
            result_text.delete('1.0', tk.END)  # Clear previous result
            result_text.insert(tk.END, result)

w = tk.Tk()
w.title('Antivirus - Virus Total API')

e2 = tk.Label(w, text='Antivirus made by Benjamin Vaniche, Enjoy!')
e2.grid(row=0, column=0, columnspan=2)

file_path_var = tk.StringVar()

button1 = ttk.Button(w, text='Select a file', command=lambda: file_path_var.set(select_file()))
button1.grid(row=1, column=0)

button2 = ttk.Button(w, text='Scan the file', command=AtClick)
button2.grid(row=1, column=1)

result_text = tk.Text(w, height=10, width=50)
result_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

w.mainloop()
            

