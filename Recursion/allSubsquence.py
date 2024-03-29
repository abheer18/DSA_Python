def printSubsequence(arr, indx, mylist):
    # base case
    if indx == len(arr):
        if len(mylist) > 0:
            print(mylist)
        return

    mylist.append(arr[indx])  # add to list
    printSubsequence(arr, indx+1, mylist)  # pick an element
    mylist.pop()  # remove from list
    printSubsequence(arr, indx+1, mylist)  # not pick


arr = [1, 2, 3]
mylist    = []
printSubsequence(arr, 0, mylist)

#arr - [1,2,3]
# SUBSEQUENCE - Every combination (not in continous order)
# [1, 2, 3]
# [1, 2]
# [1, 3]
# [1]
# [2, 3]
# [2]
# [3]
