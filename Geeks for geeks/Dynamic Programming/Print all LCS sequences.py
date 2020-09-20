"""
You are given two strings a and b. Now your task is to print all longest common sub-sequences in lexicographical order.

Example 1:

Input: s = abaaa, t = baabaca
Output: aaaa abaa baaa
Example 2:

Input: s = aaa, t = a
Output: a

Your Task:
You do not need to read or print anything. Your task is to complete the function all_longest_common_subsequences()
which takes string a and b as first and second parameter respectively and returns a list of strings which contains
all possible longest common subsequences in lexicographical order.


Expected Time Complexity: O(n^4)
Expected Space Complexity: O(K * n) where K is a constant less than n.


Constraints:
1 <= Length of both strings <= 100
"""

#User function Template for python3

class Solution:
    def all_longest_common_subsequences(self, x, y):
        n = len(s)
        m = len(t)
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if x[i - 1] == y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        for i in dp:
            print(i)
        return ["amit", "kumar"]




#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = 1
    for _ in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.all_longest_common_subsequences(s, t)
        for i in ans:
            print(i, end=" ")
        print()




# } Driver Code Ends