num = input("Please enter a number:")
size = input("Please enter the ram size:")
def ToBinary(num, size):
    binum = ""
    while(num != 0):
        x = int(num) % 2
        binum = str(x) + binum
        num = int(num) /2      
    return binum.zfill(int(size))
def ToNegative(num):
    num = list(num)
    for i in range(0,len(num)-1):
        if(num[i] == '0'):
            num[i] = '1'
        else:
            num[i] = '0'  
    if(num[-1] == 0):
        num[-1] = 1
    else:
        num[-1] = 0
        for i in range(2,len(num)):
            if(num[-i] == 1):
                num[-i] = 0
            else:
                num[-i] = 1
                break           
    num = "".join(str(element) for element in num)                  
    return int(num)
print(ToNegative(ToBinary(num,size)))