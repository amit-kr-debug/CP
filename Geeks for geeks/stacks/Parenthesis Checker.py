"""
Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

Input:
The first line of input contains an integer T denoting the number of test cases.  Each test case consists of a string
of expression, in a separate line.

Output:
Print 'balanced' without quotes if the pair of parenthesis is balanced else print 'not balanced' in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ |s| ≤ 105

Example:
Input:
3
{([])}
()
([]

Output:
balanced
balanced
not balanced
"""

tCases = int(input())
for _ in range(tCases):
    par = input()
    stack = []
    top = -1
    flag = True
    for i in range(len(par)):
        if par[i] == '{' or par[i] == '(' or par[i] == '[':
            stack.append(par[i])
            top += 1
        else:
            # print(par[i], stack[top], ord(par[i]), ord(stack[top]) )
            if top >= 0:
                if ord(par[i])-1 == ord(stack[top]) or ord(par[i])-2 == ord(stack[top]):
                    stack.pop()
                    top -= 1
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    if flag and top == -1:
        print("balanced")
    else:
        print("not balanced")
