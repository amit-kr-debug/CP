"""
level 3 foobar
"""

def solution(x):
    n = int(x)
    b = bin(n)
    stepCount = 0
    if n == 1:
        return 0
    while len(b) > 4:
        i = len(b)-1
        if b[i] == '0':
            stepCount += 1
            n >>= 1
            b = bin(n)
        elif n > 58:
            tempNS = n-1
            tempNB = n+1
            btemp1, btemp2 = bin(tempNS), bin(tempNB)
            c1, c2 = 0, 0
            c1Max, c2Max = -1, -1
            for j in range(len(btemp1)):
                if btemp1[j] == '1':
                    c1 += 1
                    c1Max = max(c1Max, c1)
                else:
                    c1 = 0
                if btemp2[j] == '1':
                    c2 += 1
                    c2Max = max(c2Max, c2)
                else:
                    c2 = 0
            # print(tempNS, tempNB)
            # print(c1Max, c2Max)
            # print(btemp1, btemp2)
            if c1Max <= c2Max:
                n = tempNB
                n >>= 1
                b = bin(n)
                stepCount += 2
            else:
                n = tempNS
                n >>= 1
                b = bin(n)
                stepCount += 2
        else:
            tempNS = n - 1
            tempNB = n + 1
            btemp1, btemp2 = bin(tempNS), bin(tempNB)
            if btemp1.count("1") > btemp2.count("1"):
                n = tempNB
                n >>= 1
                b = bin(n)
                stepCount += 2
            else:
                n = tempNS
                n >>= 1
                b = bin(n)
                stepCount += 2

        # print(n, stepCount, sep=" cost = ")
        # print(b)
    if n == 3:
        stepCount += 2
    if n == 2:
        stepCount += 1
    return stepCount


def recursion(n, N, maxE, dp):
    if n <= 1:
        return 0
    if n > N+1:
        return maxE
    if n % 2 == 1:
        if n+1 not in dp:
            dp[n+1]=1+recursion(n+1,N,maxE,dp)
        if n-1 not in dp:
            dp[n-1]=1+recursion(n-1,N,maxE,dp)
        return min(dp[n+1],dp[n-1])
    if n % 2 == 0:
        if n//2 not in dp:
            dp[n//2] = 1+recursion(n//2, N, maxE, dp)
        return dp[n//2]


def solution1(x):
    n = int(x)
    maxE = 10000000000000000000000000000
    dp = {}
    v = recursion(n, n, maxE, dp)
    return v


for i in range(1000):
    if solution(i) != solution1(i):
        print(i, solution(i), solution1(i))
        break

print(solution(63))
# print(bin(62))
# print(bin(63))
# print(bin(64))