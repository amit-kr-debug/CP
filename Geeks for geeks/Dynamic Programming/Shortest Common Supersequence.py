"""
Given two strings str1 and str2, find the length of the smallest string which has both, str1 and str2 as its
sub-sequences.
Note: str1 and str2 can have both uppercase and lowercase letters.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains two
space-separated strings.

Output:
For each testcase, in a new line, output the length of the required string.

Expected Time Complexity: O(Length(str1) * Length(str2)).
Expected Auxiliary Space: O(Length(str1) * Length(str2)).

Constraints:
1 <= T <= 100
1<= |str1|, |str2| <= 100

Example:
Input:
2
abcd xycd
efgh jghi
Output:
6
6
Explanation:
Test Case 1: One of the shortest answer can be abxycd, which is of length 6.
"""


def lcs(x, y):
    n = len(x)
    m = len(y)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return n+m-dp[n][m]


tCases = int(input())
for _ in range(tCases):
    s1, s2 = input().split()
    print(lcs(s1, s2))