

def subsequence_equalto_target(index, arr, s, target, cur_list):
    """
    Recursively explore all possible subsequences of the input array `arr` and print those
    subsequences whose sum is equal to the target sum `target`.
    """
    # Base case: if we have reached the end of the array, check if the sum of the current subsequence is equal to the target
    if index == len(arr):
        if s == target:
            print(cur_list)
        return

    # Recursive case:
    # Case 1: Take the current element and add it to the current subsequence
    cur_list.append(arr[index])
    subsequence_equalto_target(index + 1, arr, s + arr[index], target, cur_list)

    # Case 2: Don't take the current element and move on to the next element
    cur_list.pop()
    subsequence_equalto_target(index + 1, arr, s, target, cur_list)



arr = list(map(int,input("Enter the array elements: ").split()))
target = int(input("Enter the target value : "))
cur_list = []
subsequence_equalto_target(0, arr, 0, target, cur_list)


# Take input from user for array elements
# arr = list(map(int, input("Enter the array elements separated by space: ").split()))
#
# # Take input from user for target sum
# target = int(input("Enter the target sum: "))
#
# # Initialize an empty list to keep track of the current subsequence being considered
# cur_list = []
#
# # Call the recursive function to find all subsequences of the input array `arr` whose sum is equal to the target sum `target`
# subsequence_equalto_target(0, arr, 0, target, cur_list)

