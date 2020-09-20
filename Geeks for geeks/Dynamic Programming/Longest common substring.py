"""
Given two strings X and Y. The task is to find the length of the longest common substring.

Input:
First line of the input contains number of test cases T. Each test case consist of three lines, first of which contains
2 space separated integers N and M denoting the size of string X and Y strings respectively. The next two lines
contains the string X and Y.

Output:
For each test case print the length of longest  common substring of the two strings .

Constraints:
1 <= T <= 200
1 <= N, M <= 100

Example:
Input:
2
6 6
ABCDGH
ACDGHR
3 2
ABC
AC

Output:
4
1

Example:
Testcase 1: CDGH is the longest substring present in both of the strings.
"""

tCases = int(input())
for _ in range(tCases):
    n, m = map(int, input().split())
    dp = [[0 for i in range(m+1)]for j in range(n+1)]
    x = input()
    y = input()
    ans = -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = 0
            ans = max(ans, dp[i][j])
    print(ans)