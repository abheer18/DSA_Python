my_list = []    #empty list

def add_element(ele):    #add element
    my_list.append(element)

def delete_element(elem):    #delete element
    my_list.remove(element)

def display(my_list):         #display the list
    for i in my_list:
        print(i)

def update_element(index, element):   #update element
    my_list[index] = element
    display(my_list)

def sort_list(my_list):     #sort list
    my_list.sort()

print("*****LIST OPERATIONS IMPLEMENTATION******")   #calling of operations
while True:
    print("1, ADD ELEMENT")
    print("2, DELETE ELEMENT")
    print("3, DISPLAY")
    print("4, UPDATE ELEMENT")
    print("5, SORT LIST")
    print("6, EXIT")

    ch = int(input("Enter the choice [1-6] : "))
    if(ch == 1):
        element = int(input("Add the element in the list: "))
        add_element(element)
        print("%d added sucessfully" % element)
        input("Press any key to continue....")
    elif (ch == 2):
        element = int(input("Delete the element in the list: "))
        delete_element(element)
        print("%d deleted sucessfully" % element)
        input("Press any key to continue....")
    elif (ch == 3):
        print("Display the list: ")
        display(my_list)
        input("Press any key to continue....")
    elif (ch == 4):
        index = int(input("Enter the index of the list: "))
        element = int(input("Enter the new element: "))
        delete_element(index, element)
        input("Press any key to continue....")
    elif (ch == 5):
        sort_list(my_list)
        input("Press any key to continue....")
    elif (ch == 6):
        break
    else:
        print("wrong input!!")










