"""
Given two arrays: arr1[0..m-1] of size m and arr2[0..n-1] of size n. Task is to check whether arr2[] is a subset of
arr1[] or not. Both the arrays can be both unsorted or sorted. It may be assumed that elements in both array are
distinct.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test
case contains an two integers m and n denoting the size of arr1 and arr2 respectively. The following two lines contains
the space separated elements of arr1 and arr2 respectively.

Output:
Print "Yes"(without quotes) if arr2 is subset of arr1.
Print "No"(without quotes) if arr2 is not subset of arr1.

Constraints:
1 <= T <= 100
1 <= m,n <= 105
1 <= arr1[i], arr2[j] <= 105

Example:
Input:
3
6 4
11 1 13 21 3 7
11 3 7 1
6 3
1 2 3 4 5 6
1 2 4
5 3
10 5 2 23 19
19 5 3

Output:
Yes
Yes
No

Explanation:
Testcase 1: (11, 3, 7, 1) is a subset of first array.
"""

tCases = int(input())
for _ in range(tCases):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    subArr = list(map(int, input().split()))
    freq = {}
    flag = True
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq.update({i: 1})
    for i in subArr:
        if i in freq:
            if freq[i] == 1:
                freq.pop(i)
            else:
                freq[i] -= 1
        else:
            flag = False
    if flag:
        print("Yes")
    else:
        print("No")
