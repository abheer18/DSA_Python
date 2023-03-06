r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

matrix = []
print("**Enter the row-order**")

for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end =" ")

for i in range(r):
    for j in range(c):
        if(i%2 == 0):
            print(matrix[i][j], end= " ")
            print()
        elif (i%2 != 0):
            print(matrix[j][i], end =" ")
            print()


