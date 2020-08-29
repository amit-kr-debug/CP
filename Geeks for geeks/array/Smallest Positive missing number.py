"""
You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.
Note: Expected solution in O(n) time using constant extra space.

Input:
First line consists of T test cases. First line of every test case consists of N, denoting the number of elements in array. Second line of every test case consists of elements in array.

Output:
Single line output, print the smallest positive number missing.

Constraints:
1 <= T <= 100
1 <= N <= 106
-106 <= arr[i] <= 106

Example:
Input:
2
5
5 1 2 3 4
5
0 -10 1 3 -20
Output:
6
2

Explanation:
Testcase 1: Smallest positive missing number is 6.
Testcase 2: Smallest positive missing number is 2.
"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = 0
    low = 0
    high = n-1
    while low < high:
        while arr[low] <= 0 and low < n:
            low += 1
        while arr[high] >=0 and high >= 0:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    arr = arr[low:]
    # print(arr)
    n = n-low
    for i in arr:
        if abs(i) <= n:
            arr[abs(i)-1] = -abs(arr[abs(i)-1])
    for i in range(n):
        if arr[i] > 0:
            flag = 1
            break
    # print(arr)
    if flag == 1:
        print(i+1)
    else:
        print(n+1)


