fileName = "matrix.txt"

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

f = open(fileName, "a")
for i in range(0, len(matrix)):
    line = ""
    for j in range(i + 1, len(matrix[i])):
        line = line + str(matrix[i][j]) + " "
    f.write(line + "\n")
    f.flush()
f.close()