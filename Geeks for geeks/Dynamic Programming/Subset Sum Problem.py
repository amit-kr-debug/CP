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

class Solution:
    def equalPartition(self, n, arr):
        S = sum(arr)
        if S%2 == 0:
            S //= 2
        else:
            return 0
        dp = [[False for x in range(S+1)] for y in range(n+1)]
        for i in range(N+1):
            dp[i][0] = True
        for i in range(1, N+1):
            for j in range(1, S+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i][j-arr[i-1]] or dp[i-1][j]

                else:
                    dp[i][j] = dp[i-1][j]
        for i in dp:
            print(i)
        if dp[n][S]:
            return 1
        return 0

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr1 = list(map(int, input().split()))
        ob = Solution()
        if ob.equalPartition(N, arr1) == 1:
            print("YES")
        else:
            print("NO")
