"""
Given an array of non-negative integers and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Examples:

Input : arr[] = {4, 1, 10, 12, 5, 2},
          sum = 9
Output : TRUE
{4, 5} is a subset with sum 9.

Input : arr[] = {1, 8, 2, 5},
          sum = 4
Output : FALSE
There exists no subset with sum 4.
"""


# User function Template for Python3
def subsetSum(arr, N, S) :
    dp = [[False for x in range(S + 1)] for y in range(N + 1)]
    for i in range(N + 1) :
        dp[i][0] = True
    for i in range(1, S + 1) :
        dp[0][i] = False
    for i in range(1, N + 1) :
        for j in range(1, S + 1) :
            if arr[i - 1] <= j :
                dp[i][j] = dp[i][j - arr[i - 1]] or dp[i - 1][j]
            else :
                dp[i][j] = dp[i - 1][j]
    if dp[N][S] :
        return 1
    return 0
