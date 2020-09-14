"""
Given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of
well-formed(balanced) parentheses.

Example 1:

Input: N = 3
Output: ((()))
        (()())
        (())()
        ()(())
        ()()()
Example 2:
Input: N = 1
Output: ()

Your Task:
You don't need to read input or print anything. Complete the function AllParenthesis() which takes N as input parameter
and returns the list of balanced parenthesis.

Expected Time Complexity: O(2N).
Expected Auxiliary Space: O(2*N*X), X = Number of valid Parenthesis.
Constraints:
1 ≤ N ≤ 12
"""


def genPar(op, opn, cls):
    if opn < 0 or opn > cls:
        return
    if opn == cls == 0:
        ans.append(op)
    op1 = op+"("
    genPar(op1, opn-1, cls)
    op2 = op+")"
    genPar(op2, opn, cls-1)


tCases = int(input())
for _ in range(tCases):
    n = int(input())
    ans = []
    genPar("", n, n)
    for i in ans:
        print(i)