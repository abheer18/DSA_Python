# COMABINATION SUM II - The elements cannot be used multiple time in order
# to get the sum equal to target.


# array = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ], note that 2 is used two times

ans = []
mylist = []



def combinationSum_II(ind, target):
    if target == 0:
        ans.append(mylist[:])
        return

    for i in range(ind, len(arr)):
        if i > ind and arr[i] == arr[i-1]:
            continue
        if arr[i] > target:
            break
        mylist.append(arr[i])
        combinationSum_II(i+1,target - arr[i])
        mylist.pop()
    return ans


arr = list(map(int,input("Enter the elements of the array: ").split()))
arr.sort()
target = int(input("Enter the target element: "))
print(combinationSum_II(0,target))

