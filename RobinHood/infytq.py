# cook your dish here
def check(n1):

    return n1 == n1[::-1]


def getsum(num):
    n1 = int(num)
    flag = 1
    numgr = 100000000000
    numsm = 0
    while flag == 1:  # for finding palindrome greater than the num
        if check(str(n1 + 1)):
            flag = 0
            numgr = n1 + 1
            break
        n1 += 1
    n1 = int(num)
    flag = 1
    while flag == 1 and n1 >= 0:  # for finding palindrome smaller than the num
        if check(str(n1 - 1)):
            flag = 0
            numsm = n1 - 1
            break
        n1 -= 1
    print(numsm, numgr)
    return numsm + numgr


num = 464554545445
while check(str(getsum(num))) == False and num >= 0:
    print(getsum(num))
    num -= 1
sum1 = getsum(num)
print(sum1)


