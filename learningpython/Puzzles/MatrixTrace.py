'''
Given a matrix, find its trace.

Example

For

matrix = [[1, 1, 1],
          [0, 5, 0],
          [2, 1, 3]]
the output should be
matrixTrace(matrix) = 9.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix

2-dimensional array of integers representing a square matrix.

Guaranteed constraints:
1 ≤ matrix.length ≤ 5,
matrix[i].length = matrix.length,
0 ≤ matrix[i][j] ≤ 10.

[output] integer

The trace of the given matrix.
'''

def matrixTrace(m):
    s = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if(i == j): s += m[i][j]
    return s


m = [[1,1,1],
     [0,5,0],
     [2,1,3]]

print('Matrix Trace: ', matrixTrace(m))