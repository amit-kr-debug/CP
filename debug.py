"""
level 3 foobar
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


class Solution :
    def equalPartition(self, N, arr) :
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