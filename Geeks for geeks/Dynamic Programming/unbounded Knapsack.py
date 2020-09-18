"""
Given weights(wt[]) and values(val[])related to N items and the maximum capacity allowed for these items. What is the
maximum value we can achieve if we can pick any weights any number of times for a total allowed weight of W?

Example 1:

Input: N = 2, W = 3
val = {1, 1}
wt = {2, 1}
Output: 3
Explaination: Pick the 2nd element for
three times.
Example 2:

Input: N = 4, W = 8
val = {1, 4, 5, 7}
wt = {1, 3, 4, 5}
Output: 11
Explaination: The optimal choice is to pick the
2nd and 4th element.
Your Task:
You do not need to read input or print anything. Your task is to complete the function knapSack() which takes the values
N, W and the arrays val[] and wt[] as input parameters and returns the maximum possible total value.

Expected Time Complexity: O(N*W)
Expected Auxiliary Space: O(W)

Constraints:
1 ≤ N, W ≤ 1000
1 ≤ val[i], wt[i] ≤ 100
"""

class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [[0 for x in range(W+1)] for y in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, W+1):
                if wt[i-1] <= j:
                    dp[i][j] = max(val[i-1]+dp[i][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
            return dp[N][W]
