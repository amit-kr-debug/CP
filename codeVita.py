n = int(input())
s = []
platform = [0 for _ in range(100000)]
for i in range(n):
    m, p = map(int, input().split())
    for j in range(m, m+p+1):
        platform[j] += 1
print(max(platform))
