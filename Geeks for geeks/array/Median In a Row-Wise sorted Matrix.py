"""
We are given a row wise sorted matrix of size r*c, we need to find the median of the matrix given. It is assumed that r*c is always odd.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains two integers r and c, where r is the number of rows and c is the number of columns in the array a[]. Next r line contains space separated c elements each in the array a[].​

Output:
Print an integer which is the median of the matrix.

Constraints:
1<= T <=100
1<= r,c <=150
1<= a[i][j] <=1000

Example:
Input:
1
3 3
1 3 5
2 6 9
3 6 9

Output:
5
"""

tCases = int(input())
for _ in range(tCases):
    m, n = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    print(l[(n*m//2)])