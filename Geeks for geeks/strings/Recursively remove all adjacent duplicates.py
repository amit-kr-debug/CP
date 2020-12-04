"""
Given a string s, recursively remove adjacent duplicate characters from the string s. The output string should not have
any adjacent duplicates.


Input:
The first line of input contains an integer T, denoting the no of test cases. Then T test cases follow. Each test case
contains a string str.

Output:
For each test case, print a new line containing the resulting string.

Constraints:
1<=T<=100
1<=Length of string<=50

Example:
Input:
2
geeksforgeek
acaaabbbacdddd

Output:
gksforgk
acac
"""


# code
def rec(ans,le,s1,pos,taken):
    if pos == -1:
        if len(s1) == 1:
            return s1
        return ans[::-1]
    elif pos == 0:
        if le == s1[pos]:
            taken = True
            return rec(ans,le,s1,pos - 1,taken)
        else:
            if not taken:
                ans += le
            ans += s1[pos]
            return rec(ans,le,s1,pos - 1,taken)

    else:
        if s1[pos] == le:
            taken = True
            return rec(ans,le,s1,pos - 1,taken)
        else:
            if not taken:
                ans += le
            le = s1[pos]
            taken = False
            return rec(ans,le,s1,pos - 1,taken)


def check(s):
    if len(s) == 0:
        return 0
    prev = s[0]
    for i in range(1,len(s)):
        if prev == s[i]:
            return 1
        prev = s[i]
    return 0


tCases = int(input())
for _ in range(tCases):
    s = input()
    fs = rec("",s[-1],s,len(s) - 2,False)

    while check(fs):
        fs = rec("",fs[-1],fs,len(fs) - 2,False)
    print(fs)
