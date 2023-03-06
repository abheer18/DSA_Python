def fibonacci_number(num):
    if num <= 1:
        return num
    last = fibonacci_number(num-1)
    secondlast = fibonacci_number(num-2)
    return last + secondlast

number = int(input("Enter the number: "))
print(fibonacci_number(number))