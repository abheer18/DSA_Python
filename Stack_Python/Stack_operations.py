s = []
top = None

def isEmpty(stk):
    if(stk == []):
        return True
    else:
        return False

def push(stk, item):
    stk.append(item)
    top = len(stk) - 1

def pop(stk):
    if(isEmpty(stk)):
        return("Underflow")
    else:
        i = stk.pop()
        if(len(stk) == 0):
            top = None
        else:
            top = top - 1
    return i

def peek(stk):
    if(isEmpty(stk)):
        print("Underflow")
    else:
        top = len(stk) - 1
        return stk[top]

def display(stk):
    if(isEmpty(stk)):
        print("Stack is empty")
    else:
        top = len(stk) - 1
        print(stk[top],'<--- top')
        for i in range(top-1,-1,-1):
            print(stk[i])

print("STACK IMPLEMENTATION")
while True:
    print("1, Push")
    print("2, Pop")
    print("3, Peek")
    print("4, Display")
    print("5, Exit")

    ch = int(input("Enter the choice [1-5] : "))
    if(ch == 1):
        item = int(input("Enter the item you want to push : "))
        push(s,item)
        print("%d added sucessfully"%item)
        input("Press any key to continue....")
    elif(ch == 2):
        item = pop(s)
        if(item == 'Underflow'):
            print("Underflow! Stack is empty")
        else:
            print("%d is popped"%item)
        input("Press any key to continue....")
    elif(ch == 3):
        item = peek(s)
        if(item == "Underflow"):
            print("Underflow! Stack is Empty")
        else:
            print("%d is at the top"%item)
        input("Press any key to continue....")
    elif(ch == 4):
        display(s)
        input("Press any key to continue....")
    elif(ch == 5):
        break
    else:
        print("wrong input!!")



























# #CREATING STACK
#
# top = -1
# def create_Stack():
#     stack = []
#     return stack
#
# #empty stack
# def is_empty(stack):
#     return len(stack) == 0
#
# # #full stack
# # def is_full(stack):
# #     if(top == len(stack)):
# #         print("The stack is full")
#
# #Adding item (PUSH)
# def push(stack, item):
#     stack.append(item)
#     print("Pushed item : "+item)
#
# #Removing item (POP)
# def pop(stack):
#     if(is_empty(stack)):
#         return "Stack is empty"
#     return stack.pop
#
# stack = create_Stack()
# push(stack, str(10))
# push(stack, str(20))
# push(stack, str(30))
# print(str(stack))
# stack.pop()
# push(stack, str(50))
# push(stack, str(65))
# print(str(stack))
# print("Stack after pop operation: "+str(stack))

