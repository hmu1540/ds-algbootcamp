# Created by Huimin on 11/7/2021

# Use Multiprocssing.Queue class to create and implement a FIFO quque

from multiprocessing import Queue

customQueue = Queue(maxsize=3)
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.get())
