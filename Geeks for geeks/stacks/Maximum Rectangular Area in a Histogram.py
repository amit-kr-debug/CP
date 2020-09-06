"""
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of
contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.

Input:
The first line contains an integer 'T' denoting the total number of test cases. T test-cases follow. In each test cases,
the first line contains an integer 'N' denoting the size of array. The second line contains N space-separated integers
A1, A2, ..., AN denoting the elements of the array. The elements of the array represents the height of the bars.

Output:
For each test-case, in a separate line, the maximum rectangular area possible from the contiguous bars.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[i] <= 104

Example:
Input:
2
7
6 2 5 4 5 1 6
4
6 3 4 2
Output:
12
9
"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.append(0)
    n += 1
    nsl = [-1 for x in range(n)]
    nsr = [-1 for y in range(n)]
    stack = [0]
    top = 0
    for i in range(1, n):
        while top >= 0 and arr[i] < arr[stack[top]]:
            nsr[stack.pop()] = i
            top -= 1
        stack.append(i)
        top += 1
    stack = [n-1]
    top = 0
    for i in range(n-2, -1, -1):
        while top >= 0 and arr[i] < arr[stack[top]]:
            nsl[stack.pop()] = i
            top -= 1
        stack.append(i)
        top += 1
    # print(nsr)
    # print(nsl)
    area = 0
    for i in range(n):
        area = max((nsr[i]-nsl[i]-1)*arr[i], area)
    print(area)

