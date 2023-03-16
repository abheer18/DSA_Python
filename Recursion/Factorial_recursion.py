
def recursionFact(n):
    if n == 1:    #base case
        return n
    else:
        return n*recursionFact(n-1)

num = int(input("Enter the number: "))
print(recursionFact(num))