"""
Given a binary matrix. Find the maximum area of a rectangle formed only of 1s in the given matrix.

Example 1:

Input:
n = 4, m = 4
M[][] = {{0 1 1 0},
         {1 1 1 1},
         {1 1 1 1},
         {1 1 0 0}}
Output: 8
Explanation: For the above test case the
matrix will look like
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
the max size rectangle is
1 1 1 1
1 1 1 1
and area is 4 *2 = 8.
Your Task:
Your task is to complete the function maxArea which returns the maximum size rectangle area in a binary-sub-matrix with all 1’s. The function takes 3 arguments the first argument is the Matrix M[ ] [ ] and the next two are two integers n and m which denotes the size of the matrix M.

Expected Time Complexity : O(n*m)
Expected Auixiliary Space : O(m)

Constraints:
1<=n,m<=1000
0<=M[][]<=1

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.
"""


def MAH(arr, n):
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
    return area


def maxRectangle(M, n, m):
    # code here
    arr = M[0]
    area = MAH(arr, m)
    for i in range(1, n):
        for j in range(m):
            if M[i][j]!=0:
                arr[j]+=M[i][j]
            else:
                arr[j]=0
        area = max(area, MAH(arr, m))
    return area
