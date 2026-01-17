n = int(input("Enter the order of Identity matrix : "))
null_matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            null_matrix[i][j] = 1
print("Identity matrix : ")
for element in null_matrix:
    print(element)