"""
Given an array A of N integers, find any 3 elements in it such that A[i] < A[j] < A[k] and i < j < k.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains an integer N denoting the size of the array A in the next line are N space-separated values of the array A.

Output:
For each test case in a new line, the output will be 1 if the sub-sequence returned by the function is present in array A else 0. If the sub-sequence returned by the function is not in the format as mentioned then the output will be -1.

User Task:
Your task is to complete the function find3Numbers which finds any 3 elements in it such that A[i] < A[j] < A[k] and i < j < k. You need to return them as a vector, if no such element is present then return the empty vector of size 0.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[i] <= 106, for each valid i

Example:
Input:
2
5
1 2 1 1 3
3
1 1 3
Output:
1
0

Explanation:
Test case 1: a sub-sequence 1 2 3 exist.
Test case 2: no such sub-sequence exist.

Note: The Input/Output format and Examples given are used for the system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.
"""


# User function Template for python3
import sys


def find3number(arr, n):
    fList = []
    tempList = [arr[0]]
    fList.append(tempList)
    emptyList = []
    for i in range(1, n):
        flag = 0
        leng = len(fList)
        for j in range(leng):
            if arr[i] > max(fList[j]):
                fList[j].append(arr[i])
                flag = 1
                if len(fList[j]) == 3:
                    return fList[j]
        if flag == 0:
            temp = [arr[i]]
            fList.append(temp)
    return emptyList

    ans = []
    for i in range(1, n - 1):
        minEle = min(arr[0:i])
        maxEle = max(arr[i + 1:n])
        print(minEle, arr[i], maxEle)
        if minEle < arr[i] < maxEle:
            ans = [minEle, arr[i], maxEle]
            break
    return ans


# {
#  Driver Code Starts
# Initial Template for Python 3


sys.setrecursionlimit(100000)


def isSubSeq(arr, lis, n, m):
    if m == 0:
        return True
    if n == 0:
        return False
    if arr[n - 1] == lis[m - 1]:
        return isSubSeq(arr, lis, n - 1, m - 1)
    return isSubSeq(arr, lis, n - 1, m)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    lis = find3number(arr, n)
    # print(lis)
    # print(isSubSeq(arr, lis, n, len(lis)))
    if len(lis) != 0 and len(lis) != 3:
        print(-1)
        continue
    if len(lis) == 0:
        print(0)
    elif lis[0] < lis[1] and lis[1] < lis[2] and isSubSeq(arr, lis, n, len(lis)):
        print(1)
    else:
        print(-1)

# } Driver Code Ends
