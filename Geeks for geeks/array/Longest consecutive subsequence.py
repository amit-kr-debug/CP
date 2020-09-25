"""
Given an array arr[] of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

Input:
The first line of input contains T, number of test cases. First line of line each test case contains a single integer N.
Next line contains N integer array.

Output:
Print the output of each test case in a seprate line.

Constraints:
1 <= T <= 100
1 <= N <= 105
0 <= a[i] <= 105

Example:
Input:
2
7
2 6 1 9 4 5 3
7
1 9 3 10 4 20 2


Output:
6
4

Explanation:
Testcase 1:  The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.

Testcase2: 1, 2, 3, 4 is the longest consecutive subsequence.

"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(set(map(int, input().split())))
    arr.sort()
    count = 1
    ans = 1
    if n > 1:
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] == 1:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
    ans = max(ans, count)
    print(ans)
