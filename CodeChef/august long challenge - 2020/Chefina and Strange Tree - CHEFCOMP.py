tCases = int(input())
for _ in range(tCases):
    n = int(input())
    nestDict = {}

    for i in range(n-1):
        u, v = map(int, input().split())
        if u in nestDict:
            nestDict[u].update({v: 1})
        else:
            nestDict.update({u: {v: 1}})
        if v in nestDict:
            nestDict[v].update({u: 1})
        else:
            nestDict.update({v: {u: 1}})
    p = list(map(int, input().split()))
    # print(p)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = [-1 for k in range(n)]
    for i in range(n):
        visited = [0 for x in range(n)]
        city = p[i]
        q = [city]
        index = 1
        while index:
            source = q.pop()
            index -= 1
            # print("cs", city, source)
            if visited[source-1] == 1:
                continue
            else:
                visited[source-1] = 1
                temp = min(a[city-1], b[source-1])
                b[source-1] = b[source-1] - temp
                if d[source-1] == -1 and b[source-1] <= 0:
                    d[source-1] = i+1
            # print(g[source])
            for key, val in nestDict[source].items():
                # print(val, key)
                if val and visited[key-1] == 0:
                    q.append(key)
                    index += 1
            # print(index)
        for key, val in nestDict[city].items():
            nestDict[key][city] = 0
            nestDict[city][key] = 0

    # print(nestDict)
    for i in d:
        print(i, end=" ")
    print()