
for _ in range(int(input())):
    XOR = [0,1]
    x, y = map(int, input().split())

    for i in range(2, y+1):
        XOR.append(i ^ XOR[i-1])

    print(sum(XOR[x:y+1]))