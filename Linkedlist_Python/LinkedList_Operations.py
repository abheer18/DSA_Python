class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Insert at beginning
    def insertAtBegin(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #insertInBetween
    def insertInBetween(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be a linkedlist")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    #insert At End
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if(self.head == None):
            self.head = new_node
            return
        temp = self.head
        while(temp is not None):
            temp = temp.next
        temp = new_node

    #deleting a node
    def deleteNode(self,position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            temp = self.head.next
            head = None
            return
    #search an element in linkedlist

    def searchElement(self, key):
        temp = self.head
        while(temp is not None):
            if temp.data == key:
                return True
            temp = temp.next
        return False

    #sort the linkedlist
    def sortLinkedlist(self, head):
        temp = self.head
        help = Node(None)
        help = temp.next
        if temp is None:
            return
        else:
            while(temp is not None):
                help = temp.next
                while(help is not None):
                    if temp.data > help.data:
                        temp.data, help.data = help.data, temp.data
                    help = help.next
                    temp = temp.next

    #Printing the linkedlist

    def printLinkedlist(self):
        if self.head is None:
            print("The linkedlist is empty")
        else:
            temp = self.head
            while(temp is not None):
                print(str(temp.data)+ " ", end="")
                temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.insertAtEnd(50)
    llist.insertAtBegin(20)
    llist.insertAtBegin(10)
    llist.insertAtBegin(60)
    llist.insertAtBegin(800)
    print('linked list:')
    llist.printLinkedlist()
    print()
    item_to_find = 10
    if(llist.searchElement(item_to_find)):
        if llist.searchElement(item_to_find):
            print(str(item_to_find) + " is found")
        else:
            print(str(item_to_find) + " is not found")
    llist.sortLinkedlist(llist.head)
    print("Sorted List: ")
    llist.printLinkedlist()










