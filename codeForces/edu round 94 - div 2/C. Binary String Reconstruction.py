tCases = int(input())
for _ in range(tCases):
    s = input()
    x = int(input())
    n = len(s)
    W = [0 for i in range(n)]
    S = [0 for i in range(n)]
    s1 = ""
    w1 = ""
    for i in range(n):
        if i+1 > x and int(s[i]) == 1:
            W[i - x] = 1
        if i+1+x <= n and int(s[i]) == 1:
            W[i + x] = 1
    for i in range(n):
        if i+1 > x and int(W[i]) == 1:
            S[i - x] = 1
        if i+1+x <= n and int(W[i]) == 1:
            S[i + x] = 1
    for i in range(n):
        s1 += str(S[i])
        w1 += str(W[i])
    if s1 == s:
        print(w1)
    else:
        print(-1)