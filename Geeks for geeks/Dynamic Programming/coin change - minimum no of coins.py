"""
Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an
infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins. Find the minimum number of coins to make
the change. If not possible to make change then output -1

Example 1:

Input: V = 30, M = 3, coins[] = {25, 10, 5}
Output: 2
Explanation: Use one 25 cent coin
and one 5 cent coin
Example 2:
Input: V = 11, M = 4,coins[] = {9, 6, 5, 1}
Output: 2
Explanation: Use one 6 cent coin
and one 5 cent coin

Your Task:
You don't need to read input or print anything. Complete the function minCoins() which takes V, M and array coins as
input parameters and returns the answer.

Expected Time Complexity: O(V*M)
Expected Auxiliary Space: O(V)

Constraints:
1 ≤ V*M ≤ 106
All the elements of array are distinct
"""
import sys
class Solution :
    def minCoins(self, coins, M, V) :
        dp = [[0 for x in range(V + 1)] for y in range(M+1)]
        max_int = sys.maxsize
        for i in range(V+1):
            dp[0][i] = max_int
        for i in range(1, M+1):
            for j in range(1, V+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        if dp[M][V] >= max_int:
            return -1
        return dp[M][V]


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        v,m = input().split()
        v,m = int(v), int(m)
        coins = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minCoins(coins,m,v)
        print(ans)

# } Driver Code Ends
"""
14 9
11 13 5 18 16 22 15 8 21
"""
