N = int(input())
dp = [0] * 1001
for i in range(len(dp)):
    if i == 0:
        dp[i] = 1
    if i % 2:
        dp[i] = 0
    elif i == 2:
        dp[i] = 3


def solve(n):
    if dp[n] is None:
        result = solve(n-2) * solve(2)
        i = n - 4
        while(i >= 0):
            result += dp[i] * 2
            i -= 2
        dp[n] = result

    return dp[n]

print(solve(N))
assert(solve(1) == 0)
assert(solve(2) == 3)
assert(solve(3) == 0)
assert(solve(4) == 11)
assert(solve(6) == solve(4) * solve(2) + solve(2) * 2 + 2)
