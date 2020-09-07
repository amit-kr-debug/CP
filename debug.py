"""
level 3 foobar
"""

tCases = int(input())
for _ in range(tCases):
    par = input()
    top = 0
    count = 0
    maxCount = 0
    for i in range(len(par)):
        if par[i] == '(':
            top += 1
        else:
            if top > 0:
                top -= 1
                count += 2
                maxCount = max(count, maxCount)
            else:
                count = 0
                top = 0
                continue
    print(maxCount)