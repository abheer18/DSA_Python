
string = input("Enter a string:  ")
res = []
result = ""
count = {}
for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
for item, value in count.items():
    if value > 1:
        res.append(item)
        res.append(value)
    else:
        res.append(item)

print(res)

result = ''.join([str(elem) for elem in res])
print(result.replace("'", '"'))

