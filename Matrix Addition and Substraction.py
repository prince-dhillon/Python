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
result = []
rows_l = len(l)
rows_m = len(m)
cols_l = len(l[0])
cols_m = len(m[0])
if rows_l == rows_m and cols_l == cols_m:
    for i in range(rows_l):
        row = []
        result.append(row)
        for j in range(cols_m):
            row.append(l[i][j] + m[i][j])
else:
    print("Matrices having different dimensions cannot be added")
print(f"Result of A + B = {result}")