"""
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Input:
First line of the input contains no of test cases  T,the T test cases follow.
Each test case consist of 2 space separated integers A and B denoting the size of string str1 and str2 respectively
The next two lines contains the 2 string str1 and str2 .

Output:
For each test case print the length of longest  common subsequence of the two strings .

Constraints:
1<=T<=200
1<=size(str1),size(str2)<=100

Example:
Input:
2
6 6
ABCDGH
AEDFHR
3 2
ABC
AC

Output:
3
2

Explanation
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

LCS of "ABC" and "AC" is "AC" of length 2
"""


def lcs(n, m):
    if n == 0 or m == 0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    if x[n-1] == y[m-1]:
        dp[n][m] = 1 + lcs(n - 1, m - 1)
        return dp[n][m]
    else:
        dp[n][m] = max(lcs(n-1, m), lcs(n, m-1))
        return dp[n][m]


tCases = int(input())
for _ in range(tCases):
    n1, m1 = map(int, input().split())
    dp = [[-1 for i in range(m1+1)]for j in range(n1+1)]
    x = input()
    y = input()
    print(lcs(n1, m1))