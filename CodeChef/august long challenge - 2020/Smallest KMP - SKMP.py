"""
Chef has a string S. He also has another string P, called pattern. He wants to find the pattern in S, but that might be impossible. Therefore, he is willing to reorder the characters of S in such a way that P occurs in the resulting string (an anagram of S) as a substring.

Since this problem was too hard for Chef, he decided to ask you, his genius friend, for help. Can you find the lexicographically smallest anagram of S that contains P as substring?

Note: A string B is a substring of a string A if B can be obtained from A by deleting several (possibly none or all) characters from the beginning and several (possibly none or all) characters from the end.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single string S.
The second line contains a single string P.
Output
For each test case, print a single line containing one string ― the smallest anagram of S that contains P.

Constraints
1≤T≤10
1≤|P|≤|S|≤105
S and P contain only lowercase English letters
there is at least one anagram of S that contains P
Subtasks
Subtask #1 (20 points): |S|≤1,000
Subtask #2 (80 points): |S|≤105
Example Input
3
akramkeeanany
kaaaa
supahotboy
bohoty
daehabshatorawyz
badawy
Example Output
aaakaeekmnnry
abohotypsu
aabadawyehhorst
"""
"""
tCases = int(input())
for _ in range(tCases):
    s = input()
    p = input()
    sDict = {}
    for i in range(len(s)):
        if s[i] in sDict:
            sDict[s[i]] += 1
        else:
            sDict.update({s[i]: 1})
    ans = ""
    for i in range(len(p)):
        sDict[p[i]] -= 1
    left = ord(p[0])
    for i in range(97, left+1):
        if chr(i) in sDict:
            r = sDict[chr(i)]
            for j in range(r):
                ans += chr(i)
            sDict[chr(i)] = 0
    ans += p
    for i in range(left, 123):
        if chr(i) in sDict:
            r = sDict[chr(i)]
            if r>0:
                for j in range(r):
                    ans += chr(i)
    print(ans)
"""

tCases = int(input())
for _ in range(tCases):
    s = input()
    p = input()
    ans = ""
    lis = ["" for i in range(26)]
    for j in range(len(s)):
        lis[ord(s[j])-97] += s[j]
    for j in range(len(p)):
        lis[ord(p[j])-97] = lis[ord(p[j])-97][:-1]
    lis.append(p)
    lis.sort()
    # print(lis)
    n = len(lis)
    for i in range(n):
        if lis[i] == p:
            if i >= 1 and len(lis[i]) > 1:
                x = lis[i-1][0]
                o = 0
                m = len(p)
                while o < m and x == p[o]:
                    o += 1
                if o < m and ord(x) > ord(p[o]):
                    lis[i-1], lis[i] = lis[i], lis[i-1]
    for i in lis:
        ans += i
    print(ans)