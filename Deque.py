# Create by Huimin on 11/7/2021

# Use collections.deque to create and implement a FIFO queue:

from collections import deque # import only one class

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)

print(customQueue)
print(customQueue.popleft())
print(customQueue)
customQueue.append(5)
print(customQueue)
customQueue.clear()
print(customQueue)



