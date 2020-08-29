"""
Given an array, cyclically rotate an array by one.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test
case contains an integer n denoting the size of the array. Then following line contains 'n' integers forming the array.

Output:
Output the cyclically rotated array by one.

Constraints:
1<=T<=1000
1<=N<=1000
0<=a[i]<=1000

Example:
Input:
2
5
1 2 3 4 5
8
9 8 7 6 4 2 1 3

Output:
5 1 2 3 4
3 9 8 7 6 4 2 1
"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    le = arr.pop()
    arr.insert(0, le)
    for i in arr:
        print(i, end=" ")
    print()