"""
Given two strings in lowercase, find the longest string whose permutations are subsequence of given two strings.
The output longest string must be sorted.

Examples:

Input  :  str1 = "pink", str2 = "kite"
Output : "ik"
The string "ik" is the longest sorted string
whose one permutation "ik" is subsequence of
"pink" and another permutation "ki" is
subsequence of "kite".

Input  : str1 = "working", str2 = "women"
Output : "now"

Input  : str1 = "geeks" , str2 = "cake"
Output : "ek"

Input  : str1 = "aaaa" , str2 = "baba"
Output : "aa"
Input:
First line of the input contains no of test cases  T, then T test cases follow. Each test case consist of 2 space
separated integers n and m denoting the size of string str1 and str2 respectively. The next two lines contains the
2 string str1 and str2 .


Output:
For each test case print the output string in sorted order.


Constraints:
1 <= T <= 30
1 <= size(str1),size(str2)<= 100


Example:
Input:
2
6 6
abcdef
edgfhr
3 2
abc
ca

Output:
def
ac
"""

tCases = int(input())
for _ in range(tCases):
    n,m = map(int, input().split())
    str1 = input()
    str2 = input()
    freqDict = {}
    freq = [0]*26
    for i in str1:
        if i not in freqDict:
            freqDict[i] = 1
        else:
            freqDict[i] += 1
    for i in str2:
        if i in freqDict:
            if freqDict[i] == 1:
                freqDict.pop(i)
            else:
                freqDict[i] -= 1
            freq[ord(i)-97] += 1
    for i in range(26):
        for j in range(freq[i]):
            print(chr(i+97), end="")
    print()