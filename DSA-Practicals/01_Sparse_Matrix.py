rows = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")

for i in range(rows):
    row = []
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)

zero_count = 0

for i in range(rows):
    for j in range(col):
        if matrix[i][j] == 0:
            zero_count += 1

total_element = rows * col

if zero_count > total_element / 2:
    print("The Matrix is a Sparse Matrix")
else:
    print("The Matrix is not Sparse")


