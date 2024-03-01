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
    countpos = 0
    counttotal = 0
    for i in data['scans']:
        counttotal += 1
        if(data['scans'][i]['detected'] == True):
            countpos += 1
    print(f'{countpos} sources out of {counttotal} found ' + os.path.basename(file_path) + ' malicious')        

def getFiles(path):
    for filename in os.listdir(path):
        print("--" + filename)
        fullname = os.path.join(path, filename)
        if os.path.isdir(fullname): 
            getFiles(fullname)
        else:
            scanFileAtVT(fullname) 

import tkinter as tk
from tkinter import *
w = tk.Tk()
w.title('Antivirus - Virus Total API')
Label(w, text='Enter your file/folder you want to check').grid(row=1)
e1 = Entry(w)
e1.grid(row=1, column=1)
e2 = Label(w, text='Antivirus made by Benjamin Vaniche, Enjoy!')
e2.grid(row=10, column=10)
w.mainloop()

