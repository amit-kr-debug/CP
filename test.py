k = int(input())
c = int(input())
s = []
for _ in range(c):
    querry = list(input().split())
    if querry[0] == "PUT":
        s.append(int(querry[1]))
    elif querry[0] == "REMOVE_LARGEST":
        m = max(s)
        for i in range(len(s)):
            if s[i] == m:
                s.pop(i)
s.sort()
for i in s:
    print(i, end=" ")
