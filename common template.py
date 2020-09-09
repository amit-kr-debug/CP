tCases = int(input())
for _ in range(tCases):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))


tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))


arr = []
freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1


tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    k, m = map(int, input().split())