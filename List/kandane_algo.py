print("Enter the array elements:" )
arr = list(map(int,input().split()))
n = len(arr)

def max_Subarray(arr, n):
    # assigning the variables
    maxNow = arr[0]
    maxEnd = 0

    # using the for-loop
    for n in range(0, n):
        maxEnd = maxEnd + arr[n]
        if maxEnd < 0:
            maxEnd = 0

        elif (maxNow < maxEnd):
            maxNow = maxEnd

    return maxNow


# defining the array
# printing the maximum subarray sum for the users
print("Maximum Subarray Sum:", max_Subarray(arr, n))