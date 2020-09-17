"""
Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both
parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explaination:
The two parts are {1, 5, 5} and {11}.

Example 2:

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explaination: This array can never be
partitioned into two such parts.

Your Task:
You do not need to read input or print anything. Your task is to complete the function equalPartition() which takes
the value N and the array as input parameters and returns 1 if the partition is possible. Otherwise, returns 0.


Expected Time Complexity: O(N*sum of elements)
Expected Auxiliary Space: O(N*sum of elements)


Constraints:
1 ≤ N ≤ 100
1 ≤ arr[i] ≤ 1000
"""

# User function Template for Python3


def subsetSum(arr, N, S):
    dp = [[False for x in range(S + 1)] for y in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = True
    for i in range(1, N + 1):
        for j in range(1, S + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else :
                dp[i][j] = dp[i - 1][j]
    if dp[N][S]:
        return 1
    return 0


class Solution:
    def equalPartition(self, N, arr):
        # code here
        S = sum(arr)
        if S % 2 == 0 :
            return subsetSum(arr, N, S // 2)
        else :
            return 0


# {
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__' :
    t = int(input())
    for _ in range(t) :
        N = int(input())
        arr = input().split()
        for it in range(N) :
            arr[it] = int(arr[it])

        ob = Solution()
        if (ob.equalPartition(N, arr) == 1) :
            print("YES")
        else :
            print("NO")
# } Driver Code Ends