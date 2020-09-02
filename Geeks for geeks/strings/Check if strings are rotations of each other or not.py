"""
Given strings s1 and s2, you need to find if s2 is a rotated version of the string s1. The strings are lowercase.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows.
Each testcase contains two lines for s1 and s2.

Output:
For each testcase, in a new line, you need to print 1 if s2 is a rotated version of s1; else print 0.

Constraints:
1 <= T <= 103
1 <= |s1|, |s2| <= 107

Example:
Input:
4
geeksforgeeks
forgeeksgeeks
mightandmagic
andmagicmigth
mushroomkingdom
itsamemario
geekofgeeks
geeksgeekof

Output:
1
0
0
1

Explanation:
Testcase 1: s1 is geeksforgeeks, s2 is forgeeksgeeks. Clearly, s2 is a rotated version of s1 as s2 can be obtained by
left-rotating s1 by 5 units.
"""

tCases = int(input())
for _ in range(tCases):
    str1 = input()
    str2 = input()
    if len(str1) == len(str2):
        str1 += str1
        if str1.count(str2) > 0:
            print(1)
        else:
            print(0)
    else:
        print(0)

