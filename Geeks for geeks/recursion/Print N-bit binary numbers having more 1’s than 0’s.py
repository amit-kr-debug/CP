"""
Given a positive integer N, print all N bit binary numbers having more 1’s than 0’s for any prefix of the number.

Input:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test
case contains an integer N.

Output:
For each test case, print all N bit binary numbers in decreasing order in a newline.

Constraints:
1<=T<=20
1<=N<=20

Example:
Input:
2
2
3
Output:
11 10
111 110 101
"""


def findNums(op, n1, n0):
    if n1 > n or n0 > n1:
        return
    if n0 <= n1 and n1+n0 == n:
        ans.append(op)
        return
    op1 = op + "1"
    op2 = op + "0"
    findNums(op1, n1+1, n0)
    findNums(op2, n1, n0+1)


tCases = int(input())
for _ in range(tCases):
    n = int(input())
    ans = []
    findNums("", 0, 0)
    for i in ans:
        print(i, end=" ")
    print()




