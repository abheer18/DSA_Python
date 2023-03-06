# Python program to demonstrate queue implementation using collections.dequeue

from collections import deque

# Initializing a deque with deque() constructor
q = deque()

# Adding/Enqueueing elements to a queue
q.append('a')
q.append('b')
q.append('c')
q.append('d')

print("Initial queue:")
print(q)

# Removing/Dequeuing elements from a queue
print("\nElements dequeued from the queue:")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nFinal queue")
print(q)