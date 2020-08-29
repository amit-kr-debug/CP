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

    visited = [0 for x in range(limit + 1)]
    wall = [0 for x in range(limit + 1)]
    P = [0 for x in range(N)]
    P[0] = 2 * (W[0] + H[0])
    for i in range(L[0] + 1, L[0] + W[0] + 1):
        visited[i] = 1
    wall[L[0]] = 1
    wall[L[0] + W[0]] = 1
    for i in range(1, N):
        flag = 0
        count = 0
        wallCount = 0
        wallToAdd = 0
        il = wall[L[i]]
        ilw = wall[L[i] + W[i]]
        # print(wall)
        if wall[L[i]] == 1 or wall[L[i] + W[i]]:
            flag = 1

        for j in range(L[i] + 1, L[i] + W[i] + 1):
            # print(j)
            if visited[j] == 0:
                visited[j] = 1
                count += 1
            else:
                visited[j] += 1
                flag = 1
        if visited[L[i]] == 0 and wall[L[i]] == 0:
            wall[L[i]] = 1
            wallToAdd += 1
        if visited[L[i] + W[i]] == 1 and wall[L[i] + W[i]] == 0:
            wall[L[i] + W[i]] = 1
            wallToAdd += 1
        if wall[L[i]] == 1 or wall[L[i] + W[i]] == 1:
            for j in range(L[i] + 1, L[i] + W[i]):
                if wall[j] == 1:
                    wallCount += 1
                    wall[j] = 0
        if wallToAdd == 1 and wallCount == 0:
            wallCount = 1
            if il == 1:
                wall[L[i]] = 0
            else:
                wall[L[i] + W[i]] = 0
        print(wallToAdd, wallCount)
        # print(wall)
        if flag == 1:
            if wallCount < 3:
                P[i] = P[i - 1] + 2 * count
            else:
                # print(count)
                P[i] = P[i - 1] + 2 * count + (wallToAdd - wallCount) * H[i]
        else:

            P[i] = P[i - 1] + 2 * (W[i] + H[i])
        # print(P[i])
        # print(P[i], count)
        # print(wall)
    print(P)
    # print(visited)
    print("Case #" + str(_ + 1) + ":", end=" ")
    pro = 1
    for i in P:
        pro *= i
        pro %= m
    print(pro)