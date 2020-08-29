"""
Consider the following operations on a triple of integers. In one operation, you should:

Choose an integer d and an arithmetic operation ― either addition or multiplication.
Choose a subset of elements of the triple.
Apply the arithmetic operation to each of the chosen elements, i.e. either add d to each of them or multiply each of
them by d.
For example, if we have a triple (3,5,7), we may choose to add 3 to the first and third element, and we get (6,5,10)
using one operation.

You are given an initial triple (p,q,r) and a target triple (a,b,c). Find the minimum number of operations needed to
transform (p,q,r) into (a,b,c).

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test
cases follows.
The first line of each test case contains three space-separated integers p, q and r.
The second line contains three space-separated integers a, b and c.
Output
For each test case, print a single line containing one integer ― the minimum required number of operations.

Constraints
1≤T≤1,000
|p|,|q|,|r|,|a|,|b|,|c|≤109
Subtasks
Subtask #1 (10 points): |p|,|q|,|r|,|a|,|b|,|c|≤10
Subtask #2 (90 points): original constraints

Example Input
2
3 5 7
6 5 10
8 6 3
9 7 8
Example Output
1
2
Explanation
Example case 1: We add 3 to the first and third element of (3,5,7) to form (6,5,10).

Example case 2: We can add 1 to each element to form (9,7,4) and then multiply the third element by 2.
"""
import random


def count_one(d: list):
    count = 0
    for i in range(3):
        if d[i] == 0:
            count += 1
    return count


def count_zeros(d: list):
    count = 0
    for i in range(3):
        if d[i] == 0:
            count += 1
    return count


def find_quotient(initTuple: list, finalTuple: list):
    quotient = []
    remainder = []
    for i in range(3):
        quotient.append(finalTuple[i] // initTuple[i])
        remainder.append(finalTuple[i] % initTuple[i])
    return quotient, remainder


def find_diff(initTuple: list, finalTuple: list):
    diff = []
    for i in range(3):
        diff.append(finalTuple[i] - initTuple[i])
    return diff


def compare_diff(diff: list):
    count = 0
    for i in range(3):
        for j in range(3 - i):
            if diff[i] != diff[j] and diff[i] != 0:
                count += 1
    if count > 1:
        return -1
    return 1


def compare_quotient(quotient: list):
    count = 0
    for i in range(3):
        for j in range(3 - i):
            if quotient[i] != quotient[j] and quotient[i] != 1:
                count += 1
    if count > 1:
        return -1
    return 1


tCases = int(input())
for _ in range(tCases):
    # initTuple = list(map(int, input().split()))
    # finalTuple = list(map(int, input().split()))
    initTuple = random.sample(range(-5, -1), 3)
    finalTuple = random.sample(range(-10, -5), 3)
    print(initTuple, finalTuple)
    diff = find_diff(initTuple, finalTuple)
    quotient, remainder = find_quotient(initTuple, finalTuple)
    noOfZeros = count_zeros(diff)
    noOfOnes = count_one(quotient)
    if noOfZeros != 3:
        result = compare_diff(diff)
        result1 = compare_quotient(quotient)
        noOfZeros = count_zeros(remainder)
        if (result == 1 or result1 == 1) and noOfZeros > 0:
            print("1")
        else:
            dict = {}
            value = 0
            oneOne = 0
            for i in range(3):
                if quotient[i] in dict:
                    dict[quotient[i]] += 1
                    value = quotient[i]
                else:
                    dict.update({quotient[i]: 1})
            if 1 in dict:
                dict.pop(1, None)
                oneOne = 1
            length = len(dict)
            if length == 1:
                ans = 0
                d = min(diff)
                result = compare_diff(remainder)
                if result == 1:
                    ans = 2
                else:
                    ans = 3
                tempDiff = diff
                tempDiff.sort()
                if tempDiff[2] == tempDiff[1] + tempDiff[0]:
                    ans = min(2, ans)
                dList = [d] * 3
                dList = find_diff(dList, diff)
                result = compare_diff(dList)
                if result == 1:
                    ans = min(2, ans)
                print(ans)
            elif length == 2:
                if oneOne == 1:
                    print("2")
                else:
                    ans = 0
                    index = []
                    for i in range(3):
                        if value == quotient[i]:
                            index.append(i)
                    if remainder[index[0]] == remainder[index[1]] == diff[3 - index[0] - index[1]]:
                        ans = 2
                    else:
                        ans = 3
                    d = min(diff)
                    tempDiff = diff
                    tempDiff.sort()
                    if tempDiff[2] == tempDiff[1] + tempDiff[0]:
                        ans = min(2, ans)
                    dList = [d] * 3
                    dList = find_diff(dList, diff)
                    result = compare_diff(dList)
                    if result == 1:
                        ans = min(2, ans)
                    print(ans)
            elif length == 3:
                ans = 0
                q = min(quotient)
                d = min(diff)
                if q > 0:
                    for i in range(3):
                        initTuple[i] = initTuple[i] * q
                    diff1 = find_diff(initTuple, finalTuple)
                    result = compare_diff(diff1)
                    if result == 1:
                        ans = 2
                    else:
                        ans = 3
                tempDiff = diff
                tempDiff.sort()
                if tempDiff[2] == tempDiff[1] + tempDiff[0]:
                    ans = min(2, ans)
                dList = [d]*3
                dList = find_diff(dList, diff)
                result = compare_diff(dList)
                if result == 1:
                    ans = min(2, ans)
                print(ans)
            else:
                print("3")
    else:
        print("0")
