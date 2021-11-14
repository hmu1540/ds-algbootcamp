# Created by Huimin on 11/7/2021

# Use Queue module to create and implement a FIFO queue

import queue as q # import whole module

customQueue = q.Queue(maxsize=3)
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())
customQueue.ta