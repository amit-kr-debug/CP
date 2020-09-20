"""
Given two sequences, print the longest subsequence present in both of them.
Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

#User function Template for python3

class Solution:
    def longest_common_subsequences(self, x, y):
        n = len(s)
        m = len(t)
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if x[i - 1] == y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        i = n
        j = m
        ans = ""
        while i != 0 and j != 0:
            # print(i,j)
            if x[i-1] == y[j-1]:
                ans += x[i-1]
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1

        return ans[::-1]



#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = 1
    for _ in range(T):
        s, t = input().split()
        ob = Solution()
        a = ob.longest_common_subsequences(s, t)
        print(a)




# } Driver Code Ends