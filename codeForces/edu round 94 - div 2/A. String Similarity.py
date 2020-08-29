tCases = int(input())
for _ in range(tCases):
    n = int(input())
    s = input()
    ans = ""
    for i in range(n):
        ans += s[n-1]
    print(ans)