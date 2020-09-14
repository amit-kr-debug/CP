"""
Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them.
Output should be printed in sorted increasing order of strings.

Input:  str[] = "ABC"
Output: (A B C)(A BC)(AB C)(ABC)
Input:
First line contains the test cases T.  1<=T<=10
Each test case have one line string S of characters of length  N.  1<=N<=10

Output:
One line per test case, every string enclosed in ().(See example). Output should be printed in sorted order.

Example:
Input:
2
AB
ABC

Output:
(A B)(AB)
(A B C)(A BC)(AB C)(ABC)
"""


def spaceSep(op, index):
    if index == len(arr):
        ans.append(op)
        return
    op1 = op+arr[index]
    op2 = op+" "+arr[index]
    index += 1
    spaceSep(op1, index)
    spaceSep(op2, index)


tCases = int(input())
for _ in range(tCases):
    str1 = input()
    arr = []
    ans = []
    arr[:0] = str1
    spaceSep(arr[0], 1)
    for i in ans[::-1]:
        print("("+i+")", end="")
    print()
