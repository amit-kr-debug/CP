"""
Given a string which may contains lowercase and uppercase chracters. The task is to remove all  duplicate characters
from the string and print the resultant string.  The order of remaining characters in the output should be same as
in the original string.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases
follows. Each test case contains a string.

Output:
Print the resultant string after removing duplicate characters from string.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100

Example:
Input:
2
geeksforgeeks
HappyNewYear

Output:
geksfor
HapyNewYr

Explanation:
Testcase 1: After removing duplicate characters such as e, k, g, s, we have string as geksfor.
"""

tCases = int(input())
for _ in range(tCases):
    s = input()
    freq = {}
    for i in s:
        if i in freq:
            continue
        else:
            freq.update({i: 1})
            print(i, end="")
    print()