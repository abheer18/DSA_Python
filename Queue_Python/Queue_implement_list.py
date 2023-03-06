
Queue = []
front = -1
rear = -1

def isEmpty(Que):
    if(Que == []):
        return True
    else:
        return False

def enqueue(Que, item):
    Que.append(item)
    if(len(Que) == 1):
        front  = rear = 0
    else:
        rear = len(Que) - 1


def dequeue(Que):
    if(isEmpty()):
        return("Underflow!")
    else:
        i = Que.pop(0)
    if(len(Que) == 0):
        frontt = rearr = None
def peek(Que):
    if(isEmpty(Que)):
        return("Underflow")
    else:
        front = 0
    return Que[front]

def display(Que):
    if(len(Que) == 0):
        print("Queue is empty!")
    elif(len(Que) == 1):
        print(Que[0],'<-- Front <-- Rear')
    else:
        front = 0
        rear = len(Que) - 1
        print(Que[front],'<-- Front')
        for x in range(1,rear):
            print(Que[x])
        print(Que[rear], '<-- Rear')

print("QUEUE IMPLEMENTATION")
while True:
    print("1, enqueue")
    print("2, dequeue")
    print("3, Peek")
    print("4, Display")
    print("5, Exit")

    ch = int(input("Enter the choice [1-5] : "))
    if(ch == 1):
        item = int(input("Enter the item you want to enqueue : "))
        enqueue(Queue,item)
        print("%d added sucessfully"%item)
        input("Press any key to continue....")
    elif(ch == 2):
        item = dequeue(Queue)
        if(item == 'Underflow'):
            print("Underflow! Queue is empty")
        else:
            print("%d is dequeued"%item)
        input("Press any key to continue....")
    elif(ch == 3):
        item = peek(Queue)
        if(isEmpty(Queue)):
            print("Underflow! Queue is Empty")
        else:
            print("Front is: %d" %item)
        input("Press any key to continue....")
    elif(ch == 4):
        display(Queue)
        input("Press any key to continue....")
    elif(ch == 5):
        break
    else:
        print("wrong input!!")




























# #two pointers - Front & Rear
# #intitally - Front & Rear  = -1
#
# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     #ADD element (Enqueue)
#     def enqueue(self, item):
#         self.queue.append(item)
#
#     #REMOVE element (Dequeue)
#     def dequeue(self):
#         if(len(self.queue)) < 1:
#             return None
#         return self.queue.pop(0)
#
#     # Display  the queue
#     def display(self):
#         print(self.queue)
#
#     def size(self):
#         return len(self.queue)
#
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.display()
# q.dequeue()
# print("After removing an element")
# q.display()