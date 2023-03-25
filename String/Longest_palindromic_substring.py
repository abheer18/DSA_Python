
word = input("Enter the string: ")

start = 0
maxlen = 1

for i in range(1,len(word)):
    #even palindrome
    left = i-1
    right = i

    while(left >= 0 and right < len(word) and word[left] == word[right]):
        if right - left + 1 > maxlen:
            maxlen  = right - left + 1
            start = left
        left -= 1
        right += 1

    #odd palindrome
    left = i-1
    right = i+1

    while(left >= 0 and right < len(word) and word[left] == word[right]):
        if right - left + 1 > maxlen:
            maxlen = right - left + 1
            start = left
        left -= 1
        right -= 1

print(word[start : start + maxlen])
