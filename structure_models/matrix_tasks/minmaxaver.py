matrix = [[7,2,4],
          [3,8,6],
          [1,5,9]]

maxnum = matrix[0][0]
minnum = matrix[0][0]
sum = 0
numberofelements = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        numberofelements += 1
        sum = sum + int(matrix[i][j])
        if matrix[i][j] > maxnum:
            maxnum = matrix[i][j]      
        elif matrix[i][j] < minnum:
            minnum = matrix[i][j]

averagematnum = sum/numberofelements

print "Maximum number is %s." % maxnum
print "Minimum number is %s." % minnum
print "Average matrix number is %s" % averagematnum

