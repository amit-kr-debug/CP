"""
Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated
by dots.

Input:
The first line contains T denoting the number of testcases. T testcases follow. Each case contains a string S containing
characters.

Output:
For each test case, in a new line, output a single line containing the reversed String.

Constraints:
1 <= T <= 100
1 <= |S| <= 2000

Example:
Input:
2
i.like.this.program.very.much
pqr.mno

Output:
much.very.program.this.like.i
mno.pqr
"""

tCases = int(input())
for _ in range(tCases):
    arr = list(map(str, input().split(".")))
    for i in range(len(arr)-1, 0, -1):
        print(arr[i], end=".")
    print(arr[0])