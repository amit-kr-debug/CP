"""
ou are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For
each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.


Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution:
    def findTargetSumWays(self, nums: list, S: int) -> int:
        TS = sum(nums)
        if TS >= S:
            nums.sort(reverse=True)
            N = len(nums)
            # print(TS)
            if (TS+S)%2 == 0:
                S = (TS + S)//2
                dp = [[0 for x in range(S+1)] for y in range(N+1)]
                # print(dp)
                for i in range(N+1):
                    dp[i][0] = 1
                for i in range(1, N+1):
                    for j in range(S+1):
                        if nums[i-1] <= j:
                            dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                        else:
                            dp[i][j] = dp[i-1][j]
                return dp[N][S]
            else:
                return 0
        else:
            return 0


ob = Solution()
a = ob.findTargetSumWays([7,9,3,8,0,2,4,8,3,9], 0)
# a = ob.findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0)
# a = ob.findTargetSumWays([1,1,1,1,1],3)
print(a)