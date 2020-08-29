tCases = int(input())
for _ in range(tCases):
    n = int(input())
    s1 = input()
    s2 = input()
    flag = 1
    uc = []
    for i in range(n):
        if ord(s1[i]) > ord(s2[i]):
            flag = -1
            break
        elif ord(s1[i]) != ord(s2[i]):
            uc.append(i)
    if flag == -1:
        print(flag)
    else:
        pass
