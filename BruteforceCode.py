import hashlib

def bruteforce_code(hash):
    num = 999999
    while num != 000000:
        if hashlib.md5(str(num).encode()).hexdigest() == hash:
            return num
        else:
            num -= 1

print(bruteforce_code('3cc6520a6890b92fb55a6b3d657fd1f6'))
