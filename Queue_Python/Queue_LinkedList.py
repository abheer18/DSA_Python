class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        # Check if queue is empty
        if self.front is None:
            self.front = self.rear = Node(data)
            return

        self.rear.next = Node(data)
        self.rear = self.rear.next

    def dequeue(self):
        # Check if queue is empty
        if self.front is None:
            print("Queue underflow!")
            return

        data = self.front.data
        self.front = self.front.next
        return data

    def is_empty(self):
        return self.front is None


q = Queue()

print("Enqueuing: ", 1, 2, 3, 4, 5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print("Dequeueing")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())