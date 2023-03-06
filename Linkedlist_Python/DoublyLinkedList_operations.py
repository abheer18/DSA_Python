
class Node:
    def __init__(self, next = None, prev = None, data = None):
        self.next = next
        self.prev = prev
        self.data = data

class doubly_linkedlist:
    def __init__(self):
        self.head = None


    def add_element(self, new_data):   #1
        new_node = Node(data = new_data)   #newnode ke data part me new data daaldo
        new_node.next = self.head # [newnode].next -> [head]
        if self.head is not None:
            self.head.prev = new_node    #[newnode] <--- prev.[head].next
        self.head = new_node # [newnode] is the new head of the linkedlist

    def display(self, Node):          #2
        while(Node is not None):
            print(Node.data,'-->', end = ' ')
            last = Node
            Node = Node.next   # going forward (iterating)

    def insert(self, prev_node, new_data):    #3
        if prev_node is None:  #doesnt exist
            return 
        new_node = Node(new_data)
        new_node.next = prev_node.next  #jo [prev_node] ka next tha ab use [new_node] ka next bana do
        #   [prev_node] ----> [ordinary_node] , node after insertion
        # [prev_node].next ---> [newnode].(prev_node.next) ---> [ordinary_node]
        prev_node.next = new_node  #linking
        new_node.prev = prev_node  #linking
        if new_node.next is not None:
            new_node.next.prev = new_node  #linking between [newnode] and [ordinarynode]

    def add_element_atlast(self, new_data):          #4
        new_node = Node(new_data)  #made a node
        new_node.next = None   #new node at last so no next
        if self.head is None:   #checking if the ll is empty
            new_node.prev = None
            self.head = new_node
            return
        last = self.head     # helper node to go till last
        while last.next is not None:   # iterating till last node
            last = last.next
        last.next = new_node    #linking last and newnode
        new_node.prev = last   #linking last and newnode
        return

    def delete_atfirst(self):          #5

        if self.head.next == None:
            self.head = None
        else:
            self.head.next.prev = None
        return

    def delete_between(self, prev_node):     #6
        if prev_node == None:
            return
        prev_node.next = None
        prev_node.next = prev_node.next.next

    def delete_fromlast(self):         #7
        if self.head is None:
            return
        last = self.head
        while(last is not None):
            last = last.next
        last.next = None

print('*****DOUBLY LINKED LIST OPERATIONS*****')

dll = doubly_linkedlist()

while True:
    print("1, Add Elementat First")
    print("2, Display the Doubly linkedlist")
    print("3, Insert a node in between ")
    print("4, Add Element at last")
    print("5, Delete a node from First")
    print("6, Delete a node from between")
    print("7, Delete a node at last")
    print("8, EXIT")
    ch = int(input("Enter the choice [1-5] : "))

    if ch == 1:
        element = int(input("Enter the element at the beginning: "))
        dll.add_element_atlast(element)
    elif ch == 2:
        dll.display()

    elif ch == 3:
        previous = int(input("Enter the previous node: "))
        element = int(input("Enter the data in between: "))
        dll.insert(previous, element)

