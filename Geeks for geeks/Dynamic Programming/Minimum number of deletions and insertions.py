"""
Given two strings str1 and str2. The task is to remove or insert the minimum number of characters from/in str1 so as to
transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1
and inserted to some another point.

Example 1:

Input: str1 = "heap", str2 = "pea"
Output: 3
Explanation: 2 deletions and 1 insertion
p and h deleted from heap. Then, p is
inserted at the beginning One thing to
note, though p was required yet it was
removed/deleted first from its position
and then it is inserted to some other
position. Thus, p contributes one to the
deletion_count and one to the
insertion_count.
Example 2:

Input : str1 = "geeksforgeeks"
str2 = "geeks"
Output: 8
Explanation: 8 insertions


Your Task:
You don't need to read or print anything. Your task is to complete the function minOperations() which takes both
strings as input parameter and returns the minimum number of operation required.

Expected Time Complexity: O(|str1|*|str2|)
Expected Space Complexity: O(|str1|*|str2|)

Constraints:
1 ≤ |str1|, |str2| ≤ 1000
All the characters are lower case English alphabets
"""


# User function Template for python3
class Solution :
    def minOperations(self, x, y) :
        n = len(x)
        m = len(y)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if x[i-1] == y[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return n+m-2*dp[n][m]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__' :
    T = int(input())
    for i in range(T) :
        s1, s2 = input().split()
        ob = Solution()
        ans = ob.minOperations(s1, s2)
        print(ans)
# } Driver Code Ends
