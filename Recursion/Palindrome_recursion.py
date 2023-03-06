def palindrom_recursion(i, s):
    if i>= len(s)//2:
        return True
    if s[i] != s[len(s) - i -1]:
        return False
    return palindrom_recursion(i+1,s)



string = input("Enter a string: ")
print(palindrom_recursion(0,string))