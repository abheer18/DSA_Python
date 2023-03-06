def recursive_method(n):
    if n == 1:
        return
    print(n)
    n = n-1
    recursive_method(n)

n = int(input("Enter the number: "))
recursive_method(n)   #method call