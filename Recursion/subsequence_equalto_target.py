
def subsequence_equalto_target(index, list, s, target):
    if index == len(arr):
        if s == target:
            print(list)
        return

    # take
    list.append(arr[index])
    target += arr[index]
    subsequence_equalto_target(index + 1, list, s, target)

    list.pop()
    target -= arr[index]
    subsequence_equalto_target(index + 1, list, s, target)


arr = list(map(int,input().split()))
target = int(input())
subsequence_equalto_target(0, list, 0, target)