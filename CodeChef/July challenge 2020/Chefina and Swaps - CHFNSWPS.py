"""
Chefina has two sequences A1,A2,…,AN and B1,B2,…,BN. She views two sequences with length N as identical if, after they
are sorted in non-decreasing order, the i-th element of one sequence is equal to the i-th element of the other sequence
for each i (1≤i≤N).

To impress Chefina, Chef wants to make the sequences identical. He may perform the following operation zero or more
times: choose two integers i and j (1≤i,j≤N) and swap Ai with Bj. The cost of each such operation is min(Ai,Bj).

You have to find the minimum total cost with which Chef can make the two sequences identical.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test
cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers A1,A2,…,AN.
The third line contains N space-separated integers B1,B2,…,BN.
Output
For each test case, print a single line containing one integer ― the minimum cost, or −1 if no valid sequence of
operations exists.

Constraints
1≤T≤2,000
1≤N≤2⋅105
1≤Ai,Bi≤109 for each valid i
the sum of N over all test cases does not exceed 2⋅106
Subtasks
Subtask #1 (15 points):

T≤20
N≤20
Subtask #2 (85 points): original constraints

Example Input
3
1
1
2
2
1 2
2 1
2
1 1
2 2
Example Output
-1
0
1
Explanation
Example case 1: There is no way to make the sequences identical, so the answer is −1.

Example case 2: The sequence are identical initially, so the answer is 0.

Example case 3: We can swap A1 with B2, which makes the two sequences identical, so the answer is 1.
"""

# tCases = int(input())
# for _ in range(tCases):
#     n = int(input())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     dupA = {}
#     dupA1 = {}
#     duplicatesA = []
#     dupB = {}
#     dupB1 = {}
#     duplicatesB = []
#     for i in A:
#         if i in dupA:
#             if i in dupA1:
#                 dupA1[i] += 1
#             else:
#                 dupA1.update({i: 1})
#             duplicatesA.append(i)
#             dupA.pop(i)
#         else:
#             dupA.update({i: 1})
#     for i in B:
#         if i in dupB:
#             if i in dupA1:
#                 if dupA1[i] == 1:
#                     dupA1.pop(i)
#                 else:
#                     dupA1[i] -= 1
#             else:
#                 if i in dupB1:
#                     dupB1[i] += 1
#                 else:
#                     dupB1.update({i: 1})
#             duplicatesB.append(i)
#             dupB.pop(i)
#         else:
#             dupB.update({i: 1})
#     duplicatesinA = sum(dupA1.values())
#     duplicatesinB = sum(dupB1.values())
#     print(duplicatesinA, duplicatesinB)
#     print(dupA1, dupB1, dupA, dupB)
#     if duplicatesinA == duplicatesinB:
#         if duplicatesinA == 0:
#             for i in dupB:
#                 if i in dupA:
#                     dupA.pop(i)
#             if len(dupA) == 0:
#                 print(0)
#             else:
#                 print(-1)
#         else:
#             for i in dupB:
#                 if i in dupA:
#                     dupA.pop(i)
#             if len(dupA) == 0:
#                 dupList = []
#                 cost = 0
#                 for i in dupA1:
#                     for j in range(dupA1[i]):
#                         dupList.append(i)
#                 for i in dupB1:
#                     for j in range(dupB1[i]):
#                         dupList.append(i)
#                 dupList.sort()
#                 for i in range(len(dupList)//2):
#                     cost += dupList[i]
#                 print(cost)
#             else:
#                 print(-1)
#     else:
#         print(-1)

# tCases = int(input())
# for _ in range(tCases):
#     n = int(input())
#
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#
#     dupA = {}
#     dupB = {}
#     dupA1 = {}
#     dupB1 = {}
#     dupBorg = {}
#     for i in A:
#         if i in dupA:
#             dupA[i] += 1
#             dupA1[i] += 1
#         else:
#             dupA.update({i: 1})
#             dupA1.update({i: 1})
#     for i in B:
#         if i in dupBorg:
#             dupBorg[i] += 1
#         else:
#             dupBorg.update({i: 1})
#
#     for i in B:
#         if i in dupA:
#             if dupA[i] == 1:
#                 dupA.pop(i)
#             else:
#                 dupA[i] -= 1
#         else:
#             if i in dupB:
#                 dupB[i] += 1
#             else:
#                 dupB.update({i: 1})
#
#     for i in B:
#         if i in dupA1 and (dupA1[i]+dupBorg[i]) % 2 != 0:
#             if dupA1[i] == 1:
#                 dupA1.pop(i)
#             else:
#                 dupA1[i] -= 1
#         else:
#             if i in dupB1:
#                 dupB1[i] += 1
#             else:
#                 dupB1.update({i: 1})
#
#     for i in dupA:
#         if i in dupA1:
#             dupA1[i] = dupA1[i] - dupA[i]
#
#     for i in dupB:
#         if i in dupB1:
#             dupB1[i] = dupB1[i] - dupB[i]
#
#     flag = 0
#     valuesA = dupA.values()
#     valuesB = dupB.values()
#     for i in valuesA:
#         if i % 2 != 0:
#             flag = 1
#             break
#     for i in valuesB:
#         if i % 2 != 0:
#             flag = 1
#             break
#     print(dupA, dupB, dupB1, dupA1)
#     if flag == 0:
#         dupList = []
#         dupList1 = []
#         dupList2 = []
#         lista = []
#         listb = []
#         cost = 0
#         cost1 = 0
#         for i in dupA:
#             for j in range(dupA[i]//2):
#                 dupList.append(i)
#                 dupList2.append(i)
#                 lista.append(i)
#         for i in dupB:
#             for j in range(dupB[i]//2):
#                 dupList.append(i)
#                 dupList2.append(i)
#                 listb.append(i)
#         for i in dupA1:
#             if dupA1[i] % 2 == 0:
#                 for j in range(dupA1[i]//2):
#                     dupList1.append(i)
#             else:
#                 for j in range((dupA1[i]+dupB1[i])//2):
#                     dupList1.append(i)
#         for i in dupB1:
#             if dupB1[i] % 2 == 0:
#                 for j in range(dupB1[i]//2):
#                     dupList1.append(i)
#             else:
#                 for j in range((dupA1[i]+dupB1[i])//2):
#                     dupList1.append(i)
#
#
#         dupList1.sort()
#         dupList2 = dupList2 + dupList1[0:len(dupList)]
#         print(dupList, dupList1, dupList2, lista, listb)
#         dupList.sort()
#         dupList2.sort()
#         lista.sort()
#         listb.sort()
#
#         # print(dupList, dupList1, dupList2, lista, listb)
#         cost = min(sum(dupList[0:len(dupList)//2]), sum(dupList2[0:len(dupList2)//2]), 2*(len(dupList)//2+1)*dupList2[0] + sum(dupList[0:len(dupList)//2]))
#         # newCost = 100000000000000000
#
#         # if len(dupList2) > 0:
#         #     small = dupList2[0]
#         #     for k in range(len(dupList)//2):
#         #         lista.pop()
#         #         listb.pop()
#         #         templist = lista + listb
#         #         templist.sort()
#         #         newCost = min(newCost, 2*(k+1)*small + sum(templist[0:len(templist)//2]))
#
#         print(cost)
#     else:
#         print(-1)

tCases = int(input())
for _ in range(tCases):
    n = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dupA = {}
    dupB = {}
    dupA1 = {}
    dupB1 = {}
    dupBorg = {}
    for i in A:
        if i in dupA:
            dupA[i] += 1
            dupA1[i] += 1
        else:
            dupA.update({i: 1})
            dupA1.update({i: 1})
    for i in B:
        if i in dupBorg:
            dupBorg[i] += 1
        else:
            dupBorg.update({i: 1})

    for i in B:
        if i in dupA:
            if dupA[i] == 1:
                dupA.pop(i)
            else:
                dupA[i] -= 1
        else:
            if i in dupB:
                dupB[i] += 1
            else:
                dupB.update({i: 1})

    for i in B:
        if i in dupA1 and (dupA1[i]+dupBorg[i]) % 2 != 0:
            if dupA1[i] == 1:
                dupA1.pop(i)
            else:
                dupA1[i] -= 1
        else:
            if i in dupB1:
                dupB1[i] += 1
            else:
                dupB1.update({i: 1})

    for i in dupA:
        if i in dupA1:
            dupA1[i] = dupA1[i] - dupA[i]

    for i in dupB:
        if i in dupB1:
            dupB1[i] = dupB1[i] - dupB[i]

    flag = 0
    valuesA = dupA.values()
    valuesB = dupB.values()
    for i in valuesA:
        if i % 2 != 0:
            flag = 1
            break
    for i in valuesB:
        if i % 2 != 0:
            flag = 1
            break

    if flag == 0:
        cost = 0
        nondupList = []
        duplist = []

        for i in dupA:
            for j in range(dupA[i]//2):
                nondupList.append(i)

        for i in dupB:
            for j in range(dupB[i]//2):
                nondupList.append(i)
        for i in dupB1:
            if dupB1[i] != 0:
                duplist.append(i)
        nondupList.sort()
        duplist.sort()
        if len(duplist) == 0:
            duplist.append(100000000000000000)
        for i in range(len(nondupList)//2):
            if 2*duplist[0] < nondupList[i]:
                cost += 2*duplist[0]*(len(nondupList)//2-i)
                break
            else:
                duplist[0] = min(duplist[0], nondupList[i])
                cost += nondupList[i]
            print(cost)
        print(cost)
    else:
        print(-1)