import requests
import time
import json
def getResponseFromVT(file_path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': '453af95ed16995efc1d0894c5df35a4e9374de3792225c4a48f46c1f484afbb7'}
    files = {'file': (file_path, open(file_path, 'rb'))}
    response = requests.post(url, files=files, params=params)
    return response.json(),response.status_code

response_json,response_status = getResponseFromVT(r'C:\Users\Lenovo\Documents\Diabetes prediction with KNN.docx')
if response_status != 200:
    print("Error submitting file for scanning")
print(response_json)
sha256 = response_json['sha256']

url = "https://www.virustotal.com/vtapi/v2/file/report"
params = {'apikey': '453af95ed16995efc1d0894c5df35a4e9374de3792225c4a48f46c1f484afbb7', 'resource':sha256}
response = requests.get(url, params=params)
data = response.json()
countpos = 0
counttotal = 0
for i in data['scans']:
    counttotal += 1
    if(data['scans'][i]['detected'] == True):
        countpos += 1
print(f'{countpos} sources out of {counttotal} found the file malicious ')        