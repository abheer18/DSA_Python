s = 'Abheer'

ans = []
def print_all_substrings(s):
    if len(s) == 0:
        return
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            ans.append(s[i:j])
    print_all_substrings(s[1:])
    return ans

print(print_all_substrings(s))
