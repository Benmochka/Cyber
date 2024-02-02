num = input("Please enter a number:")
size = input("Please enter the ram size:")
tempbinum = ""
def ToBinary(num, size):
    while(num != 0):
        x = int(num) % 2
        tempbinum += (str(x))
    addZero = len(tempbinum) - size
    for i in range (addZero):
        binum += "0"
        i+=1
    binum += tempbinum
    return binum
print(ToBinary(num,size))

    