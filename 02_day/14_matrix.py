matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, 10],
]

print(matrix[0])
print(matrix[0][0])

for sublist in matrix:
    for item in sublist:
        print(item)

matrix = []
for i in range(5):
    sublist = []
    for j in range(5):
        sublist.append(j)
    matrix.append(sublist)

print(matrix)
