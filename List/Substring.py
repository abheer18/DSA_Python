enter = int(input("Enter the String: "))
res = [enter[i: j] for i in range(len(enter))
          for j in range(i + 1, len(enter) + 1)]
print(res)
