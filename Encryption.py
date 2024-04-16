
def encrypt(secret, text):
    newvalue = ""
    for i,char in enumerate(text):
        newvalue += chr(ord(char) + ord(secret[i%len(secret)]))        
    return newvalue
print(encrypt("123456","hello"))