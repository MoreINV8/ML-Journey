import time
import threading

def count(num:int) :
    for i in range(num) :
        print(f"{num}: {i}")
        time.sleep(0.2)
        print("using threads:",threading.active_count())
        
start = time.time()
for i in range(10) :
    t = threading.Thread(target=count, kwargs={"num":i})
    t.start()
    t.join()
    
print("took:", time.time() - start)