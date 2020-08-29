"""
1st sol prisoners
def solution(x, y):

    # Your code here
    freq = {}
    for i in x:
        if i in freq:
            freq[i] += 1
        else:
            freq.update({i: 1})
    for i in y:
        if i in freq:
            if freq[i] == 1:
                freq.pop(i)
            else:
                freq[i] -= 1
        else:
            freq.update({i: 1})
    for key, values in freq.items():
        uni = key
    return uni
"""

"""
2nd level 1st question gearing up
from fractions import Fraction

def solution(pegs):
    aLen = len(pegs)
    fSum = 0
    if aLen % 2 == 0:
        fSum = pegs[aLen - 1] - pegs[0]
    else:
        fSum = -1 * (pegs[0] + pegs[aLen - 1])
    if aLen == 1:
        return [-1, -1]

    if aLen > 2:
        for i in range(1, aLen-1):
            fSum += (-1)**(i+1) * 2 * pegs[i]
    if aLen % 2 == 0:
        fGear = Fraction(2 * (float(fSum)/3)).limit_denominator()
    else:
        fGear = Fraction(2*fSum).limit_denominator()
    if fGear < 2:
        return [-1, -1]
    tempGear = fGear
    rValue = check(pegs, aLen, tempGear)
    if rValue == -1:
        return [-1, -1]
    else:
        return [fGear.numerator, fGear.denominator]


def check(pegs, aLen, tempGear):
    for i in range(0, aLen-2):
        nextTempGear = pegs[i+1] - pegs[i] - tempGear
        if nextTempGear < 1 or tempGear < 1:
            return -1
        tempGear = nextTempGear
    return 1
"""

"""
2nd level 2nd question the bunny prisoner 
"""


def solution(x, y):
    aux = x + y - 1
    return (aux * (aux-1)) // 2 + x

print(solution(3,2))
