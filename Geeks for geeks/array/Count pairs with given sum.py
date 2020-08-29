"""
Given an array of integers, and an integer  ‘K’ , find the count of pairs of elements in the array whose sum is equal to 'K'.

Input:
First line of the input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains 2 space separated integers N and K denoting the size of array and the sum respectively. Second line of each test case contains N space separated integers denoting the elements of the array.

Output:
Print the count of pairs of elements in the array whose sum is equal to the K.

Constraints:
1<=T<=50
1<=N<=50
1<=K<=50
1<=A[i]<=100

Example:
Input
2
4 6
1  5  7 1
4 2
1 1 1 1
Output
2
6
"""

tCases = int(input())
for _ in range(tCases):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    r = {}
    for i in arr:
        if i in r:
            r[i] += 1
        else:
            r.update({i: 1})
    for i in arr:
        if m-i in r:
            count += r[m-i]
        if i == m-i:
            count -= 1
    print(count//2)
