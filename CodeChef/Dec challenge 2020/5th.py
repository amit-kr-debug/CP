for _ in range(int(input())):
    s = input ()
    n = len (s)
    lis = [{} for x in range (n + 1)]
    for i in range(n):
        flag = -1
        if s[i] == '1':
            if flag == 1 or flag == -1:
                flag = 0
            else:
                flag = 1
        lis[1][s[i]] = flag

    for i in range(n - 1):
        flag = -1
        c = s[i]
        if s[i] == '1':
            if flag == 1 or flag == -1:
                flag = 0
            else:
                flag = 1

        for j in range(i + 1, n):
            c += s[j]
            if s[j] == '1':
                if flag == 1 or flag == -1:
                    flag = 0
                else:
                    flag = 1
            lis[len(c)][c] = flag
    print(lis)

    for dic in lis:
        for key in list(dic):
            if dic[key] == 1 and key[::-1] in dic:
                if key == key[::-1]:
                    pass
                else:
                    del dic[key]
    sum = 0
    print(lis)
    for dic in lis:
        sum += len(dic)
    print(sum)

