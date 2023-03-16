# COMABINATION SUM - The elements can be used multiple time in order
# to get the sum equal to target.

# array = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]], note that 2 is used two times

ans = []
mylist = []

def combinationSum_I(ind, target):
    if ind == len(arr):
        if target == 0:
            ans.append(mylist[:])
        return

    if arr[ind] <= target:
        mylist.append(arr[ind])
        combinationSum_I(ind, target - arr[ind])
        mylist.pop()
    combinationSum_I(ind+1, target)
    return ans



arr = list(map(int,input("Enter the array elements: ").split()))
target = int(input("Enter the target value: "))
print(combinationSum_I(0,target))

