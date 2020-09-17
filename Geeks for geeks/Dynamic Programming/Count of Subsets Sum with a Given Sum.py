"""


Given an array arr[] of integers and an integer sum, the task is to count all subsets of the given array with a sum
equal to a given sum.

Note: Answer can be very large, so, output answer modulo 109+7

Example 1:

Input: N = 6, arr[] = {2, 3, 5, 6, 8, 10}
       sum = 10
Output: 3
Explanation: {2, 3, 5}, {2, 8}, {10}
Example 2:
Input: N = 5, arr[] = {1, 2, 3, 4, 5}
       sum = 10
Output: 3
Explanation: {1, 2, 3, 4}, {1, 4, 5},
             {2, 3, 5}

Your Task:
You don't need to read input or print anything. Complete the function perfectSum() which takes N, array arr[] and sum
as input parameters and returns an integer value
"""

#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
		dp = [[0 for x in range(sum+1)] for y in range(n+1)]
		for i in range(n + 1) :
			dp[i][0] = 1
		for i in range(n+1):
			for j in range(sum+1):
				if arr[i-1] <= j:
					dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
				else:
					dp[i][j] = dp[i-1][j]
		return dp[n][sum]


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for _ in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends
