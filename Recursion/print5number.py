
def recursiveMethod(i):

    if i == 5:
        return
    i += 1
    print(i)
    recursiveMethod(i)

i = 0
print("printing numbers: ",recursiveMethod(i))