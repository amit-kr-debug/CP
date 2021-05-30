import math
def cups(N,L,x):
    if sum(x)<L:
        return -1
    else:
        if L%len(x)==0:
            req = L//len(x)
        else:
            req = L//len(x)+1

        for i in range(req, L):
            tmp = 0
            for j in range(0, N):
                if x[j] < i:
                    tmp+=x[j]
                else:
                    tmp+=i
            if tmp>=L:
                return i




print(cups(5, 16, [3, 4, 4, 5, 3]))