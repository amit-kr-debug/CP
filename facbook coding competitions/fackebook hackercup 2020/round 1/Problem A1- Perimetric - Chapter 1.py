tCases = int(input())
for _ in range(tCases):
    N, K, W = map(int, input().split())
    L = list(map(int, input().split()))
    al, bl, cl, dl = map(int, input().split())
    H = list(map(int, input().split()))
    ah, bh, ch, dh = map(int, input().split())
    m = 10**9+7
    for i in range(K, N):
        L.append((al*L[i-2] + bl*L[i-1] + cl) % dl + 1)
        H.append((ah*H[i-2] + bh*H[i-1] + ch) % dh + 1)

    prevH = H[0]
    prevL = L[0]
    maxH = [0 for x in range(L[N-1]+W+1)]
    P = [0 for x in range(N)]
    P[0] = 2*(prevH+W)
    for j in range(W+1):
        maxH[L[0]+j] = max(H[0], maxH[L[0]+j])

    for i in range(1, N):
        diffL = L[i] - prevL
        diffH = H[i] - maxH[L[i]]
        if diffL <= W:

            if maxH[L[i]] <= H[i]:
                temp = P[i-1] + 2 * diffH + 2 * diffL
                P[i] = temp
                for j in range(W+1):
                    maxH[L[i] + j] = max(H[i], maxH[L[i] + j])
            else:
                P[i] = P[i-1] + 2 * diffL
                for j in range(W + 1):
                    maxH[L[i] + j] = max(H[i], maxH[L[i] + j])
        else:
            P[i] = P[i-1] + 2*(W+H[i])
            for j in range(W + 1):
                maxH[L[i] + j] = max(H[i], maxH[L[i] + j])
        prevH = H[i]
        prevL = L[i]
    print("Case #"+str(_+1) + ":", end=" ")
    pro = 1
    for i in P:
        pro *= i
        pro %= m
    print(pro)