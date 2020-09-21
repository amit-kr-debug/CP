tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    ans= []
    temp = []
    sumarr = []
    tempSum = 0
    ansSum = 0
    for i in arr:
        if i > 0:
            temp.append(i)
            tempSum += i
        elif len(temp) > 0:
            ans.append(temp)
            temp = []
            sumarr.append(tempSum)
            tempSum = 0
    if tempSum!=0:
        ans.append(temp)
        sumarr.append(tempSum)
    if len(sumarr)>0:
        index = 0
        dupSUm = [x for x in sumarr]
        max1 = max(sumarr)
        maxindex1 = 0
        maxindex2 = 0
        for i in range(len(sumarr)):
            if sumarr[i] == max1:
                maxindex1 = i
                dupSUm.pop(i)
                break
        max2 = 0
        if len(dupSUm) != 0:
            max2 = max(dupSUm)
        for i in range(len(sumarr)):
            if sumarr[i] == max2:
                maxindex2 = i
        if max2 == 0:
            print(sumarr[maxindex1])
            print(len(ans[maxindex1]), end=" ")
            for i in ans[maxindex1]:
                print(i, end=" ")
        else:
            print(sumarr[maxindex2]+sumarr[maxindex1])
            print(len(ans[maxindex1])+len(ans[maxindex2]), end=" ")
            if maxindex1 > maxindex2:
                maxindex1, maxindex2 = maxindex2, maxindex1
            for i in ans[maxindex1]:
                print(i, end=" ")
            for i in ans[maxindex2][::-1]:
                print(i, end=" ")
        print()
    else:
        print(0)
        print(0)
