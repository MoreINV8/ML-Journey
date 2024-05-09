from collections import deque
import threading
import time

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
# 1.
def placeOrder(order:str, queue:Queue) -> None:
    print("current working thread:", threading.active_count())
    print(order, "is in process...")
    time.sleep(0.5)
    queue.enqueue(order)
    print(order, "process finish")
    
def serveOrder(queue:Queue) -> None:
    print("current working thread:", threading.active_count())
    print("start serve...")
    time.sleep(2)
    queue.dequeue()
    print("served...")

orders = ['pizza','samosa','pasta','biryani','burger']
queue = Queue()

print("1.")
for order in orders :
    place = threading.Thread(target= placeOrder, args=(order, queue, ))
    serve = threading.Thread(target= serveOrder, args=(queue, ))
    
    place.start()
    serve.start()
    
    place.join()
    serve.join()

# 2.
counterQ = Queue()
counterQ.enqueue("1")
print("2.")
while True :
    current = counterQ.dequeue()
    print(current, end=", ")
    if current == "1010" :
        break
    counterQ.enqueue(current + "0")
    counterQ.enqueue(current + "1")