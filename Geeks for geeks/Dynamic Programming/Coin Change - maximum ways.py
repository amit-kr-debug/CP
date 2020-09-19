"""
Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of
S = { S1, S2, .. , SM } valued coins.

Example 1:

Input:
n = 4 , m = 3
S[] = {1,2,3}
Output: 4
Explanation: Four Possible ways are:
{1,1,1,1},{1,1,2},{2,2},{1,3}.

​Example 2:

Input:
n = 10 , m = 4
S[] ={2,5,3,6}
Output: 5
Explanation: Five Possible ways are:
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5}
and {5,5}.


Your Task:
You don't need to read input or print anything. Your task is to complete the function count() which accepts an array
S[] its size m and n as input parameter and returns the number of ways to make change for N cents.



Expected Time Complexity: O(m*n).
Expected Auxiliary Space: O(n).


Constraints:
1 <= n,m <= 103
"""

#User function Template for python3

#User function Template for python3

class Solution:
    def count(self, S, m, n):
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if S[i-1] <= j:
                    dp[i][j] = dp[i][j-S[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]


#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends