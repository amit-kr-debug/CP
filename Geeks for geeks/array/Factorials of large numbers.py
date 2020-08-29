"""
Given an integer, the task is to find factorial of the number.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,the number whose factorial is to be found

Output:
Print the factorial of the number in separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000

Example:
Input
3
5
10
2

Output
120
3628800
2
"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)