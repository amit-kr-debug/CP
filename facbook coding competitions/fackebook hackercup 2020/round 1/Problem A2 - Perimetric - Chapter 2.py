tCases = int(input())
for _ in range(tCases):
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    al, bl, cl, dl = map(int, input().split())
    W = list(map(int, input().split()))
    aw, bw, cw, dw = map(int, input().split())
    H = list(map(int, input().split()))
    ah, bh, ch, dh = map(int, input().split())
    m = 10 ** 9 + 7
    for i in range(K, N):
        L.append((al * L[i - 2] + bl * L[i - 1] + cl) % dl + 1)
        H.append((ah * H[i - 2] + bh * H[i - 1] + ch) % dh + 1)
        W.append((aw * W[i - 2] + bw * W[i - 1] + cw) % dw + 1)
    limit = -1
    for i in range(N):
        limit = max(L[i] + W[i], limit)
    P = [0 for x in range(N)]
    P[0] = 2 * (H[0] + W[0])
    trav = [0 for x in range(limit+1)]
    exists = [0 for x in range(limit+1)]
    minl = L[0]
    maxl = L[0] + W[0]
    for j in range(L[0]+1, L[0]+W[0]+1):
        if trav[j] == 0:
            trav[j] = H[0]
            # print(trav[j])
            exists[j] = 1
    # print(trav)
    i = 1
    hleft =0
    hright = 0
    while i < N:
        leftl = L[i]
        rightl = L[i]+W[i]
        if leftl < minl:
            minl = leftl
            hleft = H[i]
        if rightl > maxl:
            maxl = rightl
            hright = H[i]
        for j in range(leftl+1, rightl+1):
            if exists[j] == 0:
                exists[j] = 1
        for j in range(leftl + 1, rightl + 1):
            if trav[j] == 0 and exists[j] != 0:
                trav[j] = H[i]
        breadth = maxl-minl
        lv = 0
        lf = 0
        height = trav[minl]
        # print(trav[minl+1])
        for j in range(minl+1, maxl+1):
            # print(trav[j])
            if trav[j] != trav[j-1]:
                if trav[j] == 0 and trav[j-1] != 0:
                    lv = j-1
                    # print("a")
                if j != minl+1 and trav[j-1] == 0 and trav[j] != 0:
                    fv = j-1
                    breadth -= (fv-lv)
                    # print("b")
                if trav[j] > trav[j-1]:
                    height += trav[j] - trav[j - 1]
                    # print("c")
                elif trav[j] < trav[j-1]:
                    height += trav[j-1] - trav[j]
                    # print("d")
            # print(height, breadth)
        height += trav[maxl]
        # print(breadth)
        P[i] = (2*breadth + height) % m
        i += 1
    # print(P)
    print("Case #" + str(_ + 1) + ":", end=" ")
    pro = 1
    for i in P:
        pro *= i
        pro %= m
    print(pro)