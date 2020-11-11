"""
You saw how to create Magic Square of different sizes. It is very important to understand the way the matrices are represented and printed in python.
In this assignment, you will be provided with the number of rows i.e. r and columns i.e. c as the input and your job is to create a matrix of size rxc.
Also, the matrix should have elements starting from 1 to rxc with an increment of one in row manner.

Example:

if r = 2 and c = 3
then the output is

1 2 3
4 5 6

Input Format:
Two numbers r and c in a single line separated by a space.

Output Format:
Elements of the generated matrix.
Each row should be printed in a new line with each element separated by a space.

Example:

Input:
3 4

Output:
1 2 3 4
5 6 7 8
9 10 11 12

Explanation:
In this example the number of rows i.e. r is 3 and the number of columns is i.e. c is 4.
Therefore the size of the matrix is 3x4 which is 12. Which means it should have 12 elements starting from 1.
It should be printed in row manner i.e. the first element should be at the first row and first column, second element at first row and second column and so on.

"""

n, m = map(int, input().split())
mat = [[x+(y*m) for x in range(1, m+1)] for y in range(0, n)]
for row in mat:
    print(" ".join(map(str, row)))