"""
Given a sorted array of numbers, value K and an index X in array, find the K closest numbers in position to X in array.

Example: Let array be 11 23 24 75 89, X be 24 and K be 2. Now we have to find K numbers closest to X that is 24. In this
example, 23 and 75 are the closest 2 numbers to 24.

Note: K should be even and in cases with less than k/2 elements on left side or right side, we need to print other side
elements. Like 2 4 5 6 7, X be 6 and K be 4 then answer is 2 4 5 7



Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input C[i].
The third line of each test case contains K and X.

Output:

Print K closest number in position to X in array.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 100
1 ≤ C[i] ≤ 1000

Example:

Input
1
5
2 11 23 24 25
3 11

Output
23 75
"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    k, x = map(int, input().split())
    index = 0
    for i in range(n):
        if arr[i] == x:
            index = i
    if k/2 <= index and k/2 <= n-index-1:
        # print(1)
        for i in range(index-k//2, index):
            print(arr[i], end=" ")
        for i in range(index+1, index+k//2+1):
            print(arr[i], end=" ")
    elif k/2 >= index:
        # print(2)
        for i in range(0, index):
            print(arr[i], end=" ")
        for i in range(index + 1, k+1):
            print(arr[i], end=" ")
    else:
        # print(3)
        for i in range(n-k-1, index):
            print(arr[i], end=" ")
        for i in range(index + 1,n):
            print(arr[i], end=" ")