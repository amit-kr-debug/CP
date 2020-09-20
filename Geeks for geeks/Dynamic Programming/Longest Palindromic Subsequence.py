"""
Given a String, find the longest palindromic subsequence

Input:
The first line of input contains an integer T, denoting no of test cases. The only line of each test case consists of a
string S(only lowercase)

Output:
Print the Maximum length possible for palindromic subsequence.

Constraints:
1<=T<=100
1<=|Length of String|<=1000


Examples:
Input:
2
bbabcbcab
abbaab
Output:
7
4
"""


def lcs(x,y):
    n = len(x)
    m = len(y)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]


tCases = int(input())
for _ in range(tCases):
    s = input()
    s1 = s[::-1]
    # print(s, s1)
    print(lcs(s, s1))
