import random
tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    temp = "abcdefghijklmnopqrstuvwxyz"
    temp *= 5
    ans = []
    ans.append(temp)
    index = 0
    for i in range(n):
        temp1 = ans[index]
        # print(temp1[arr[i]])
        temp = ans[index][:arr[i]]
        temp += ans[index][arr[i]-1]
        temp += ans[index][arr[i]+1:]
        ans.append(temp)
        index += 1
    for i in ans:
        print(i)
