def twoStrings(s1, s2):
    v = {}
    ls1 = len(s1)
    ls2 = len(s2)
    for j in range(ls1):
        v[s1[j]] = 1

    for j in range(ls2):
        if s2[j] in v:
            return "YES"
    return "NO"


n = int(input())
a = []
for _ in range(n):
    a.append(input())
m = int(input())
b = []
for _ in range(m):
    b.append(input())

for i in range(n):
    print(twoStrings(a[i], b[i]))
