l = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
if len(l[0]) == len(m):
    for i in range(len(l)):
        for j in range(len(m[0])):
            for k in range(len(l[0])):
                result[i][j] += l[i][k] * m[k][j]
else:
    print("Multiplication is not possible")
for element in result:
    print(element)