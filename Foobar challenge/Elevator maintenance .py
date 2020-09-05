def solution(arr):
    l = []
    for i in arr:
        temp = list(map(int, i.split(".")))
        while len(temp) < 3:
            temp.append(-1)
        l.append(temp)
    # print(l)
    d = {}
    for i in range(len(l)):
        if l[i][0] in d:
            if l[i][1] in d[l[i][0]]:
                d[l[i][0]][l[i][1]].update({l[i][2]: 1})
            else:
                d[l[i][0]].update({l[i][1]: {l[i][2]: 1}})
        else:
            d.update({l[i][0]: {l[i][1]: {l[i][2]: 1}}})
    ans = []
    for key, val in sorted(d.items()):
        for key1, val1 in sorted(val.items()):
            for key2, val2 in sorted(val1.items()):
                tempStr = str(key)
                if key1 == -1:
                    pass
                else:
                    tempStr += "."+str(key1)
                    if key2 == -1:
                        pass
                    else:
                        tempStr += "."+str(key2)
                ans.append(tempStr)
    return ans


print(solution(["2.8.7", "2.8.5", "1.9.7", "1.9.2", "1.9.5", "1.8.7", "1"]))

