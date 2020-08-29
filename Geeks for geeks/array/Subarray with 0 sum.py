"""
Given an array a[] of N positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. The next line contains N space separated integers forming the array.

Output:
Print "Yes" ( without quotes) if there exist a subarray of size at least one with sum equal to 0 or else print "No" ( without quotes).

Constraints:
1 <= T <= 100
1 <= N <= 104
-105 <= a[i] <= 105

Example:
Input:
2
5
4 2 -3 1 6
5
4 2 0 1 6

Output:
Yes
Yes

Explanation:
Testcase 1: 2, -3, 1 is the subarray with sum 0.

"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    sumDict = {arr[0]: 0}
    auxSum = arr[0]
    flag = False
    for i in arr[1:]:
        auxSum += i
        if auxSum == 0:
            flag = True
            break
        if auxSum in sumDict:
            flag = True
            break
        else:
            sumDict.update({auxSum: 1})

    if flag:
        print("Yes")
    else:
        print("No")