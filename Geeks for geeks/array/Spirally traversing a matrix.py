"""
Given a matrix mat[][] of size M*N. Traverse and print the matrix in spiral form.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each testcase has 2 lines. First line contains M and N respectively separated by a space. Second line contains M*N values separated by spaces.

Output:
Elements when travelled in Spiral form, will be displayed in a single line.

Constraints:
1 <= T <= 100
2 <= M,N <= 10
0 <= Ai <= 100

Example:
Input:
2
4 4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 4
1 2 3 4 5 6 7 8 9 10 11 12

Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
1 2 3 4 8 12 11 10 9 5 6 7
"""

tCases = int(input())
for _ in range(tCases):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    mat = []
    for i in range(n):
        mat.append(arr[i*m:i*m+m])
    # print(mat)
    left, right, top, bottom = 0, m-1, 0, n-1
    count = m*n
    while left <= right and top <= right:
        if left <= right and top <= bottom:
            for i in range(left, right+1):
                print(mat[top][i], end=" ")
            for i in range(top+1, bottom+1):
                print(mat[i][right], end=" ")
        if left < right and top < bottom:
            for i in range(right-1, left-1, -1):
                print(mat[bottom][i], end=" ")
            for i in range(bottom-1, top, -1):
                print(mat[i][left], end=" ")
        top += 1
        bottom -= 1
        right -= 1
        left += 1
