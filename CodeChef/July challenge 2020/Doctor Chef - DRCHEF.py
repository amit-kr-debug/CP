"""
Chef is multi-talented. He has developed a cure for coronavirus called COVAC-19. Now that everyone in the world is infected, it is time to distribute it throughout the world efficiently to wipe out coronavirus from the Earth. Chef just cooks the cure, you are his distribution manager.

In the world, there are N countries (numbered 1 through N) with populations a1,a2,…,aN. Each cure can be used to cure one infected person once. Due to lockdown rules, you may only deliver cures to one country per day, but you may choose that country arbitrarily and independently on each day. Days are numbered by positive integers. On day 1, Chef has x cures ready. On each subsequent day, Chef can supply twice the number of cures that were delivered (i.e. people that were cured) on the previous day. Chef cannot supply leftovers from the previous or any earlier day, as the cures expire in a day. The number of cures delivered to some country on some day cannot exceed the number of infected people it currently has, either.

However, coronavirus is not giving up so easily. It can infect a cured person that comes in contact with an infected person again ― formally, it means that the number of infected people in a country doubles at the end of each day, i.e. after the cures for this day are used (obviously up to the population of that country).

Find the minimum number of days needed to make the world corona-free.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and x.
The second line contains N space-separated integers a1,a2,…,aN.
Output
For each test case, print a single line containing one integer ― the minimum number of days.

Constraints
1≤T≤103
1≤N≤105
1≤ai≤109 for each valid i
1≤x≤109
the sum of N over all test cases does not exceed 106
Subtasks
Subtask #1 (20 points): a1=a2=…=aN
Subtask #2 (80 points): original constraints

Example Input
3
5 5
1 2 3 4 5
5 1
40 30 20 10 50
3 10
20 1 110
Example Output
5
9
6
"""
# tCases = int(input())
# for _ in range(tCases):
#     c, med = map(int, input().split())
#     # print(c, med)
#     ppl = list(map(int, input().split()))
#     ppl.sort()
#     ppl1 = [x for x in ppl]
#     days = 0
#     if ppl[0] == ppl[c-1]:
#         if ppl[0] <= med:
#             print(c)
#         else:
#             while ppl[0] != 0:
#                 if med <= ppl[0]:
#                     ppl[0] = ppl[0]-med
#                 else:
#                     med = ppl[0]
#                     ppl[0] = 0
#                 if ppl[0]*2 >= ppl[1]:
#                     ppl[0] = ppl[1]
#                 else:
#                     ppl[0] *= 2
#                 med *= 2
#                 days += 1
#             days += len(ppl) - 1
#             print(days)
#     else:
#         if ppl[c-1] <= med:
#             print(c)
#         else:
#             i = 0
#             while med < ppl[c-1]:
#                 while med <= ppl[i]:
#                     ppl[i] -= med
#                     med *= 2
#
#                     if ppl[i] * 2 >= ppl1[i]:
#                         ppl[i] = ppl1[i]
#                     else:
#                         ppl[i] *= 2
#                     days += 1
#                     print(days, ppl)
#                     print(ppl[i], med)
#                 low = 0
#                 high = c - 1
#                 possibleIndex = -1
#
#                 while low <= high:
#                     mid = (low + high) // 2
#                     if ppl1[mid] == med:
#                         possibleIndex = mid
#                         break
#
#                     elif ppl1[mid] > med:
#                         high = mid - 1
#
#                     else:
#                         possibleIndex = mid
#                         low = mid + 1
#
#                 if possibleIndex == -1:
#                     i = c-1
#                 else:
#                     i = possibleIndex
#                 if ppl1[i] < med:
#                     med = ppl[i]
#                 print(ppl[i], med)
#             print(days)

tCases = int(input())
for _ in range(tCases):
    c, med = map(int, input().split())
    # print(c, med)
    ppl = list(map(int, input().split()))
    ppl.sort()
    ppl1 = [x for x in ppl]
    days = 0
    if ppl[0] == ppl[c-1]:
        if ppl[0] <= med:
            print(c)
        else:
            while ppl[0] != 0:
                if med <= ppl[0]:
                    ppl[0] = ppl[0]-med
                else:
                    med = ppl[0]
                    ppl[0] = 0
                if ppl[0]*2 >= ppl[1]:
                    ppl[0] = ppl[1]
                else:
                    ppl[0] *= 2
                med *= 2
                days += 1
            days += len(ppl) - 1
            print(days)
    else:
        if ppl[c-1] <= med:
            print(c)
        else:
            i = 0
            low = 0
            high = c - 1
            possibleIndex = -1

            while low <= high:
                mid = (low + high) // 2
                if ppl1[mid] == med:
                    possibleIndex = mid
                    break

                elif ppl1[mid] > med:
                    possibleIndex = mid
                    high = mid - 1

                else:
                    low = mid + 1

            if possibleIndex == -1:
                i = c-1
            else:
                i = possibleIndex

            # print(ppl[i])
            while med < ppl[i]:
                med *= 2
                days += 1
            med = ppl[i]
            ppl[i] = 0
            prev = i
            med *= 2
            days += 1
            print(ppl, days)
            while med < ppl1[c-1]:
                low = 0
                high = c - 1
                possibleIndex = -1
                while low <= high:
                    mid = (low + high) // 2
                    if ppl1[mid] == med:
                        possibleIndex = mid
                        break
                    elif ppl1[mid] > med:
                        high = mid - 1
                    else:
                        possibleIndex = mid
                        low = mid + 1
                if possibleIndex == prev:
                    med *= 2
                    days += 1
                else:
                    i = possibleIndex
                    med = ppl[i]
                    ppl[i] = 0
                    prev = i
                    med *= 2
                    days += 1
                print(ppl, days, med)
            for i in range(c):
                if ppl[i] > 0:
                    days += 1
            print(days)
