"""
level 3 foobar
"""

tCases = int(input())
for _ in range(tCases):
    S = int(input())
    arr = list(map(int, input().split()))
    N = len(arr)
    dp = [[0 for x in range(S+1)]for y in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, S+1):
            if arr[i-1] <= j:
                dp[i][j] = max(1+dp[i][j-arr[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    # for i in dp:
    #     print(i)
    print(dp[N][S])

