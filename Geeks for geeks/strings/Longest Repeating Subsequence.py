"""
Given a string str, find length of the longest repeating subseequence such that the two subsequence don’t have same
string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in
the original string.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first
line of each test case contains an integer N denoting the length of string str.

The second line of each test case contains the string str consisting only of lower case english alphabets.

Output:

Print the length of the longest repeating subsequence for each test case in a new line.


Constraints:

1<= T <=100

1<= N <=1000


Example:

Input:

2

3

abc

5

axxxy

Output:

0

2
"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    s = input()
    freq = {}
    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            
    print(ans)
