"""
Given an array A of size N having distinct elements, the task is to find the next greater element for each element of
the array in order of their appearance in the array. If no such element exists, output -1

Input:
The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each
test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line
of each test case contains N space separated positive integers denoting the values/elements in the array A.

Output:
For each test case, print in a new line, the next greater element for each array element separated by space in order.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1018
Example:
Input
2
4
1 3 2 4
4
4 3 2 1
Output
3 4 4 -1
-1 -1 -1 -1

Explanation:
Testcase1: In the array, the next larger element to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? since it doesn't exist hence -1.
"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [-1 for x in range(n)]
    stack = [0]
    top = 0
    for i in range(1, n):
        while top >= 0 and arr[i] > arr[stack[top]]:
            ans[stack.pop()] = arr[i]
            top -= 1
        stack.append(i)
        top += 1
    for i in ans:
        print(i, end=" ")
    print()