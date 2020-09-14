"""
Given a string of length n, print all the possible subsets of the string in a lexiographically-sorted order.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first
line of each test case contains an integer n denoting the length of the string. The second line of each test case
contains the string consisting of lower-case english alphabets.

Output:
For each testcase, in a new line, print all the possible subsets (except the null subset) in a sorted order with a
space between each subset.

Constraints:
1 <= T <= 100
1 <= n <= 16

Example:
Input:
1
3
abc
Output:
a ab abc ac b bc c
"""
arr = []


def powerSet(output, inp):
    if len(inp) == 0:
        arr.append(output)
        return
    # print(inp)
    temp = inp.pop()
    output1 = output
    output2 = output + temp
    powerSet(output2, inp)
    powerSet(output1, inp)
    inp.append(temp)


tCases = int(input())
for _ in range(tCases):
    n = int(input())
    str1 = input()
    arr1 = []
    arr1[:0] = str1
    arr1.reverse()
    powerSet("", arr1)
    arr.pop()
    arr.sort()
    for i in arr:
        print(i, end=" ")
    print()