def get_sum(num, line1):
    w = len(line1)
    line = line1[:]
    for i in range(w):
        if num <= 0:
            break
        temp = min(line[i], num)
        line[i] = line[i] - temp
        num = num - temp
    # print(line)
    if num > 0:
        return 0
    sum1 = sum(line)
    aux = [0 for x in range(w)]
    for i in range(w):
        aux[i] = line[i]*(sum1 - line[i])
    sum2 = sum(aux)
    # print(sum2)
    sum2 //= 2
    sum3 = 0
    for i in range(w):
        sum3 += line[i]*(sum2 - aux[i])
    # print(sum3)
    sum3 //= 3
    return sum3


tCases = int(input())
for _ in range(tCases):
    n, c, k = map(int, input().split())
    colours = {}
    lines = [[]]
    # mat = [0]
    for i in range(n):
        a, b, color = map(int, input().split())
        if color in colours:
            if a in colours[color]:
                colours[color][a] += 1
            else:
                colours[color].update({a: 1})
        else:
            colours.update({color: {a: 1}})
    V = [0]
    V[1:] = list(map(int, input().split()))
    for i in range(1, c+1):
        lines_set = []
        if i in colours:
            # print(colours[i])
            for key, val in colours[i].items():
                lines_set.append(val)
            # lines_set.sort()
            lines.append(lines_set)

    sumLine = [[-1000000000 for i in range(c + 1)] for j in range(k + 1)]
    fMat = [[1000000000000000 for i in range(c+1)] for j in range(k+1)]

    count = 0
    for i in range(0, k+1):
        fMat[i][0] = 0
    for i in range(k+1):
        for j in range(1, c+1):
            remLine = i//V[j]
            for p in range(remLine+1):
                r = p*V[j]
                # mat.append(r)
                if sumLine[p][j] == -1000000000:
                    count += 1
                    sumLine[p][j] = get_sum(p, lines[j])
                fMat[i][j] = min(fMat[i][j], fMat[i-r][j-1] + sumLine[p][j])
    # for i in range(k+1):
    #     for j in range(c):
    #         remLine = i // V[j+1]
    #         for p in range(remLine):
    #             r = p * V[j+1]
    #             fMat[i][j+1] = min(fMat[i][j+1], fMat[i-r][j-1+1] + sumLine[p+1][j+1])
    ans = fMat[k][c]
    print(ans)
