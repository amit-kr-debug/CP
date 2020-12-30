import math
d1, v1, d2, v2, p = map(int, input().split())
days = 0
flag = 1

if d1 > d2:
    if p/v2 > (d1 - d2):
        p -= (d1 - d2) * v2
        days = d1 - d2
    else:
        flag = 0
        days = math.ceil(p/v2)

elif d2 > d1:
    if p/v1 > (d2 - d1):
        p -= (d2 - d1) * v1
        days = d2 - d1
    else:
        flag = 0
        days = math.ceil(p/v1)
if flag:
    days += math.ceil(p/(v1+v2))
print(days)

