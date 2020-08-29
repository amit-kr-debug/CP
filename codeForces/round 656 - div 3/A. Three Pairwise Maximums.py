"""
You are given three positive (i.e. strictly greater than zero) integers x, y and z.

Your task is to find positive integers a, b and c such that x=max(a,b), y=max(a,c) and z=max(b,c), or determine that it is impossible to find such a, b and c.

You have to answer t independent test cases. Print required a, b and c in any (arbitrary) order.

Input
The first line of the input contains one integer t (1≤t≤2⋅104) — the number of test cases. Then t test cases follow.

The only line of the test case contains three integers x, y, and z (1≤x,y,z≤109).

Output
For each test case, print the answer:

"NO" in the only line of the output if a solution doesn't exist;
or "YES" in the first line and any valid triple of positive integers a, b and c (1≤a,b,c≤109) in the second line. You can print a, b and c in any order.
Example
input
5
3 2 3
100 100 100
50 49 49
10 30 20
1 1000000000 1000000000
output
YES
3 2 1
YES
100 100 100
NO
NO
YES
1 1 1000000000
"""

tCases = int(input())
for _ in range(tCases):
    a1 = list(map(int, input().split()))
    maxele = max(a1)
    nDict = {}
    for i in a1:
        if i in nDict:
            nDict[i] += 1
        else:
            nDict.update({i: 1})
    a = {k: v for k, v in sorted(nDict.items(), key=lambda item: item[1], reverse=True)}
    flag = -1
    tempList = []
    count = 0
    # print(a, maxele)
    flag1 = 0
    for i in a:
        tempList.append(i)
        if i == 1:
            flag1 = 1

    for i in a:
        if a[i] > 2 and count == 0 and maxele == i:
            flag = 2

        elif a[i] == 2 and count == 0 and maxele == i:
            flag = 1
        count += 1
    if flag == 1 and flag1 == 0:
        print("YES")
        for i in tempList:
            print(i, end=" ")
        print(tempList[len(tempList)-1]-1)
    elif flag == 1 and flag1 == 1:
        print("YES")
        for i in tempList:
            print(i, end=" ")
        print(tempList[1])
    elif flag == 2:
        print("YES")
        print(tempList[0], tempList[0], tempList[0])
    else:
        print("NO")