def printSubsequence(arr, indx, ds):
    # base case
    if indx == len(arr):
        if len(ds) > 0:
            print(ds)
        return

    ds.append(arr[indx])  # add to list
    printSubsequence(arr, indx+1, ds)  # pick an element
    ds.pop()  # remove from list
    printSubsequence(arr, indx+1, ds)  # not pick


arr = [1, 2, 3]
ds = []
printSubsequence(arr, 0, ds)
