"""
You are given a string S with length N that contains only the 26 lowercase English letters. You are also given a sequence W1,W2,…,W26 of weights corresponding to these letters in the order from 'a' to 'z', i.e. W1 is the weight of 'a', W2 is the weight of 'b' and so on.

We define the weight of a string as the sum of weights of all characters present in it. If a character occurs multiple times in this string, its weight is also counted multiple times.

Next, we define the power of a string s as the sum of weights of all strings r such that s can be represented as r+r+…+r+p, where + denotes string concatenation and p is a prefix of r (possibly empty).

Consider a contiguous substring of S chosen uniformly randomly among all its N(N+1)/2 contiguous substrings. Find the expected value of the power of such a substring. The expected power can be represented as a fraction P/Q, where P and Q are positive integers and Q is coprime with 998,244,353. You should calculate P⋅Q−1 modulo 998,244,353, where Q−1 denotes the multiplicative inverse of Q modulo 998,244,353.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single string S.
The second line contains 26 space-separated integers W1,W2,…,W26.
Output
For each test case, print a single line containing one integer P⋅Q−1 modulo 998,244,353.

Constraints
1≤N≤500,000
1≤Wi≤109 for each valid i
S contains only lowercase English letters
the sum of |S| over all test cases does not exceed 500,000
Subtasks
Subtask #1 (10 points):

N≤100
the sum of |S| over all test cases does not exceed 1,000
Subtask #2 (20 points):

N≤2,000
the sum of |S| over all test cases does not exceed 20,000
Subtask #3 (70 points): original constraints

Example Input
2
aaa
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
abab
1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
Example Output
499122179
698771051
Explanation
Let W(s) and P(s) denote the weight and power of a string s respectively.

Example case 1: There are 3 contiguous substrings "a", 2 contiguous substrings "aa" and 1 contiguous substring "aaa".

"a" is chosen with probability 3/6; we have P(a)=W(a)=1
"aa" is chosen with probability 2/6; P(aa)=W(a)+W(aa)=1+2=3
"aaa" is chosen with probability 1/6; P(aaa)=W(a)+W(aa)+W(aaa)=1+2+3=6
The expected power is (3⋅1+2⋅3+1⋅6)/6=15/6.

Example case 2: The contiguous substrings are "a", "b", "ab", "ba", "aba", "bab", "abab"; the first three of them occur twice. We have P(a)=W(a)=1, P(b)=W(b)=2, P(ab)=W(ab)=1+2=3, P(ba)=W(ba)=3, P(aba)=W(ab)+W(aba)=3+4=7, P(bab)=W(ba)+W(bab)=3+5=8 and P(abab)=W(ab)+W(abab)=3+6=9.

The expected power is (2⋅P(a)+2⋅P(b)+2⋅P(ab)+P(ba)+P(aba)+P(bab)+P(abab))/10=39/10
"""
from functools import reduce
from math import gcd


def lowestForm(x, y):
    g = gcd(x, y)
    x = x // g
    y = y // g
    return x, y


def factors(n):
    return list(set(reduce(list.__add__,
                           ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m

        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        x = x + m0

    return x


tCases = int(input())
for _ in range(tCases):
    md = 998244353
    s = input()
    w = list(map(int, input().split()))
    n = len(s)

    rDict = {}
    wDict = {}
    pDict = {}

    for i in range(n):
        for j in range(n - i):
            temp = s[i:n - j]
            if temp in rDict:
                rDict[temp] += 1
            else:
                rDict.update({temp: 1})
                weight = 0
                for k in range(len(temp)):
                    weight += w[ord(temp[k]) - 97]
                wDict.update({temp: weight})
    for i in wDict:
        l1 = len(i)
        weight = 0
        for j in range(l1):
            subStr = i[:l1 - j]
            l2 = l1 - j
            k = l1 // l2
            r = l1 % l2
            if r == 0:

                if subStr * k == i:
                    weight += wDict[subStr]

            elif r != 0 and subStr * k + subStr[:r] == i:
                weight += wDict[subStr]

        pDict.update({i: weight})

    p = 0
    for i in pDict:
        p += pDict[i] * rDict[i]
    q = sum(rDict.values())
    p, q = lowestForm(p, q)
    q1 = modInverse(q, md)
    print(p * q1 % md)
    # print(pDict, wDict)





"""
tCases = int(input())
for _ in range(tCases):
    md = 998244353
    s = input()
    w = list(map(int, input().split()))
    n = len(s)
    if n <= 110:
        rDict = {}
        wDict = {}
        pDict = {}
        for i in range(n):
            for j in range(n - i):
                temp = s[i:n - j]
                if temp in rDict:
                    rDict[temp] += 1
                else:
                    rDict.update({temp: 1})
                    weight = 0
                    for k in range(len(temp)):
                        # print(temp[k], 97-ord(temp[k]), w[ord(temp[k])-97])
                        weight += w[ord(temp[k]) - 97]
                    wDict.update({temp: weight})
        # print(rDict, wDict)
        # print(w[1])
        for i in wDict:
            l = len(i)
            l2 = l
            weight = 0
            if l > 2:
                if l % 2 == 0:
                    l1 = l
                    fact = factors(l)
                    fact.sort()
                    # print(fact)
                    m = fact.pop()
                    if m == 2:
                        while l > 1:
                            if i[:l // 2] == i[l // 2:l]:
                                weight += wDict[i[:l // 2]]
                                l = l // 2
                                # print(i, i[:l // 2], l)
                            else:
                                break
                    # print(fact)
                    for k in fact:
                        l = l1
                        # print(i, k)
                        # print(i[:l // k] * k,"  ", i)
                        if k!=1 and i[:l // k] * k == i:
                            weight += wDict[i[:l // k]]
                            # print(weight)
                    if i[0] == i[l - 1]:
                        weight += wDict[i[:l - 1]]
                        l = l1 - 1
                        j = i[0:l]
                        l1 = l
                        fact = factors(l)
                        fact.sort()
                        fact.pop()
                        for k in fact:
                            l = l1
                            # print(k)
                            # print(j[:l // k] * k, "  ", j)
                            if k!=1 and j[:l // k] * k == j:
                                weight += wDict[i[:l // k]]

                else:
                    if i[0] == i[l - 1]:
                        weight += wDict[i[:l - 1]]
                        # print(i, weight)
                        l = l - 1
                        j = i[0:l]
                        l1 = l
                        # l = l//2
                        fact = factors(l)
                        fact.sort()
                        m = fact.pop()
                        # print(fact)
                        if m == 2:
                            while l > 1:
                                if j[:l // 2] == j[l // 2:l]:
                                    weight += wDict[i[:l // 2]]
                                    l = l // 2
                                    # print(i, i[:l // 2], l)
                                else:
                                    break
                        for k in fact:
                            l = l1
                            # print(k)
                            # print(j[:l // k] * k, "  ", j)
                            if k!=1 and j[:l // k] * k == j:
                                weight += wDict[i[:l // k]]
                        # print(l1+1, i, i[0]*l1)
                        if l1+1 > 3 and i[0]*(l1+1) == i:
                            weight += wDict[i[0]]
                    else:
                        fact = factors(l)
                        fact.sort()
                        m = fact.pop()
                        # print(fact)
                        for k in fact:
                            l = l2
                            # print(k)
                            # print(j[:l // k] * k, "  ", j)
                            if k != 1 and i[:l // k] * k == i:
                                weight += wDict[i[:l // k]]
                        # print(l1+1, i, i[0]*l1)
                        if l2 + 1 > 3 and i[0] * (l2 + 1) == i:
                            weight += wDict[i[0]]
                weight += wDict[i]
                pDict.update({i: weight})
                # print(i, weight)
            elif l == 2:
                if i[0] == i[l - 1]:
                    weight += wDict[i[:l - 1]]
                weight += wDict[i]
                pDict.update({i: weight})

            else:
                weight = wDict[i]
                pDict.update({i: wDict[i]})
        q = modInverse(sum(rDict.values()), md)
        # q = sum(rDict.values())
        p = 0
        for i in pDict:
            p += pDict[i] * rDict[i]
        print(p * q % md)
        # print(pDict, wDict)
        # print(p, q)
    else:
        print(44444444)
        
        
        
        
    for i in wDict:
        u = len(i)
        l1 = u
        weight = 0
        temp = []
        if u > 2:
            fact=factors(u)
            fact.sort()
            for k in fact:
                j=i[:u // k]
                # print(k, i, j*k)
                if j * k == i and j not in temp:
                    temp.append(j)
                    weight+=wDict[j]
            if i[0] == i[u - 1]:
                i1=i[:u - 1]
                fact=factors(u - 1)
                fact.sort()
                for k in fact:
                    j=i1[:u // k]
                    # print(k, i1, j * k)
                    if j * k == i1 and j not in temp:
                        temp.append(j)
                        weight+=wDict[j]
            pDict.update({i: weight})
        elif u == 2:
            if i[0] == i[u - 1]:
                weight+=wDict[i[:u - 1]]
            weight+=wDict[i]
            pDict.update({i: weight})

        elif u == 1:
            weight = wDict[i]
            pDict.update({i: wDict[i]})
        # print(i, temp)
        
        
        
        for i in wDict:
            l1 = len(i)
            weight = 0
            for j in wDict:
                l2 = len(j)
                if l1 >= l2:
                    k = l1//l2
                    r = l1 % l2
                    if j == i[:l2]:
                        if r == 0:
                            if j*k == i:
                                weight += wDict[j]
                        elif r != 0 and j[:r] == i[l1-r:]:
                            if j*k == i[:l1-r]:
                                weight += wDict[j]
            pDict.update({i: weight})
"""