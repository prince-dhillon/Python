n = int(input("Enter number of Rows of the Matrix : "))
l = []
for i in range(n):
    row = []
    l.append(row)
    for j in range(n):
        row.append(int(input(f"Enter {i,j} element of row : ")))
transpose = [[0 for o in range(n)] for o in range(n)]
for i in range(len(l)):
    for j in range(len(l)):
        transpose[i][j] = l[j][i]
print("Entered Matrix : ",l)
print("Transposed Matrix : ",transpose)