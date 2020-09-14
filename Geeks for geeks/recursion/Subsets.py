"""
Given an array of integers that might contain duplicates, return all possible subsets.

Note:

        Elements in a subset must be in non-descending order.
        The solution set must not contain duplicate subsets.
        The subsets must be sorted lexicographically.

Input:
First line of input contains number of testcases T. For each testcase, there will be two line of input, first of which contains N and next contains N space seperated integers. Every test case has two lines. First line is N, size of array.

Output:
One line per test case, every subset enclosed in () and in every set intergers should be space seperated.(See example)

Constraints:
1 <= T <= 500
1 <= N <= 12
1 <= x <= 9

Example:
Input:
2
3
1 2 2
4
1 2 3 3

Output:
()(1)(1 2)(1 2 2)(2)(2 2)
()(1)(1 2)(1 2 3)(1 2 3 3)(1 3)(1 3 3)(2)(2 3)(2 3 3)(3)(3 3)

Explanation:
Testcase 1: Subsets are
[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]
"""


def powerSet(output, inp):
    if len(inp) == 0:
        if output not in dict1:
            dict1.update({output[:-1]: 1})
        return
    # print(inp)
    temp = inp.pop()
    output1 = output
    output2 = output + str(temp) + " "
    powerSet(output1, inp)
    powerSet(output2, inp)
    inp.append(temp)


tCases = int(input())
for _ in range(tCases):
    n = int(input())
    dict1 = {}
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    powerSet("", arr)
    for key, val in sorted(dict1.items()):
        print("("+key+")", end="")
    print()