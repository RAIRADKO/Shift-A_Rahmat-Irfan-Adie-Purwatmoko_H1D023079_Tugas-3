import numpy as np
from collections import deque

arr = np.array([1, 2, 3, 4, 5])
print("Array Numpy:", arr)

queue = deque([10, 20, 30])
print("Queue sebelum operasi:", queue)

queue.append(40)
print("Queue setelah append:", queue)

queue.popleft()
print("Queue setelah popleft:", queue)
