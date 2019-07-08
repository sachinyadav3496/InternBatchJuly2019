import random 
import time
ch = [ 0,1]

class mygen():
    def __iter__(self):
        return self
    def __next__(self):
        return random.choice(ch)


for var in mygen() : 
    print(var,end=' ',flush=True)
    time.sleep(0.1)
