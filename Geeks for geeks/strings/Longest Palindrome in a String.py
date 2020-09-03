"""
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ]
where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome
if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index ).

NOTE: Required Time Complexity O(n2).

Input:
The first line of input consists number of the testcases. The following T lines consist of a string each.

Output:
In each separate line print the longest palindrome of the string given in the respective test case.

Constraints:
1 ≤ T ≤ 100
1 ≤ Str Length ≤ 104

Example:
Input:
1
aaaabbaa

Output:
aabbaa

Explanation:
Testcase 1: The longest palindrome string present in the given string is "aabbaa".
"""

tCases = int(input())
for _ in range(tCases):
    s = input()
    startIndex = 0
    endIndex = 0
    maxLen = 0
    mat = [[False for x in range(len(s))] for y in range(len(s))]
    for i in range(len(s)):
        mat[i][i] = True
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            mat[i][i+1] = True
            startIndex = i
            endIndex = i+1
            maxLen = 2
    for i in range(3, len(s)+1):
        for j in range(len(s)+1-i):
            k = j + i - 1
            if s[j] == s[k] and mat[j+1][k-1]:
                mat[j][k] = True
                if i > maxLen:
                    startIndex = j
                    endIndex = k
                    maxLen = i
    print(s[startIndex:endIndex+1])


