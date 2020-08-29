def rec(start, end):
    print(start, end)
    if start == end:
        return cost
    if start > end:
        return 0
    if matCost[start][end] != 0:
        return matCost[start][end]
    s = 1000000000000000000
    for i in range(start, end+1):
        s = min(s, calculate(start, i) + rec(i+1, end))
    matCost[start][end] = s
    return matCost[start][end]


def calculate(start, end):
    if start == end:
        return cost
    fam = {}
    ans = cost
    for i in range(start, end+1):
        if arr[i] in fam:
            fam[arr[i]] += 1
        else:
            fam.update({arr[i]: 1})
    for values in fam.values():
        if values > 1:
            ans += values
    return ans


tCases = int(input())
for _ in range(tCases):
    n, cost = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = cost
    matCost = [[0 for i in range(1001)] for j in range(1001)]
    fAns = rec(0, n-1)
    print(fAns)