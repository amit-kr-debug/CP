"""
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Input:
First line consists of T test cases. First line of every test case consists of n, denoting the size of array. Second
line of every test case consists of price of ith length piece.

Output:
For each testcase, in a new line, print a single line output consists of maximum price obtained.

Constraints:
1 <= T <= 100
1 <= n <= 100
1 <= Ai <= 100

Example:
Input:
1
8
1 5 8 9 10 17 17 20
Output:
22
"""

tCases = int(input())
for _ in range(tCases):
    S = int(input())
    arr = list(map(int, input().split()))
    N = len(arr)
    length = [x for x in range(1, N+1)]
    # print(length)
    dp = [[0 for x in range(S+1)]for y in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, S+1):
            if length[i-1] <= j:
                dp[i][j] = max(arr[i-1]+dp[i][j-length[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N][S])