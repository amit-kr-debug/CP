def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def getMinCost(n:int, k:int, s:str, b:list):
    start = 0
    s = Convert(s)
    minCost = 100000000
    totalCost = 0
    if k != 1 :
        index = k
        flag = False
        totalCost = 0
        for i in range(1, k):
            if s[i-1] != s[i]:
                flag = True
                break
            if b[i-1] <= minCost:
                minCost = b[i-1]
                index = i-1


        if not flag:
            if b[k-1] <= minCost:
                minCost = b[k-1]
                index = k-1
            totalCost += minCost
            if s[index] == "0":
                s[index] = "1"
            else:
                s[index] = "0"

        while index < n-1:
            flag = False
            minCost = 100000000
            print(index)
            for i in range(index+1, min(index+k, n)):
                if s[i - 1] != s[i]:
                    flag = True
                    index = i
                    break
                if b[i - 1] <= minCost:
                    minCost = b[i - 1]
                    index = i - 1

            if not flag:
                if b[min(index+k, n) - 1] <= minCost:
                    minCost = b[min(index+k, n) - 1]
                    index = min(index+k, n) - 1
                totalCost += minCost
                if s[index] == "0":
                    s[index] = "1"
                else:
                    s[index] = "0"
    return totalCost


print(getMinCost(5,1,"00110",[2,1,1,1,1]))