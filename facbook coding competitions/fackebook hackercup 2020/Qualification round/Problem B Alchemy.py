tCases = int(input())
for _ in range(tCases):
    n = int(input())
    string = input()
    countA = 0
    countB = 0
    for i in range(n):
        if string[i] == 'A':
            countA += 1
        else:
            countB += 1
    print("Case #"+str(_+1)+":", end=" ")
    if abs(countA-countB) == 1:
        print('Y')
    else:
        print('N')