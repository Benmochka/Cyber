from threading import Thread

counter = 0
def add():
    global counter
    for _ in range(1000000):
        counter += 1
    
def decrement():
    global counter
    for _ in range(1000000):
        counter -= 1    

thread1 = Thread(target = add)  
thread2 = Thread(target = decrement)
thread1.start()
thread2.start()    
thread1.join() 
thread2.join()
print(counter)