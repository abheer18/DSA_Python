# def reversearray_recursion(i, arr, n):
#     if i >= n//2:
#         return
#     arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
#     return reversearray_recursion(i+1,arr,n)
#
#
# n = int(input("enter the size of the array: "))
# array = list(map(int,input("Enter the array elements: ").split()))
# print(reversearray_recursion(0,array,n))
#

def reversearray_recursion(i, arr, n):
    if i >= n//2:
        return arr
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return reversearray_recursion(i+1,arr,n)


n = int(input("enter the size of the array: "))
array = list(map(int,input("Enter the array elements: ").split()))
print(reversearray_recursion(0,array,n))
