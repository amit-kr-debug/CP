"""
Chef made N pieces of cakes, numbered them 1 through N and arranged them in a row in this order. There are K possible types of flavours (numbered 1 through K); for each valid i, the i-th piece of cake has a flavour Ai.

Chef wants to select a contiguous subsegment of the pieces of cake such that there is at least one flavour which does not occur in that subsegment. Find the maximum possible length of such a subsegment of cakes.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two integers N and K.
The second line contains N space-separated integers A1,A2,…,AN.
Output
For each test case, print a single line containing one integer ― the maximum length of a valid subsegment.

Constraints
1≤T≤1,000
1≤N≤105
2≤K≤105
1≤Ai≤K for each valid i
the sum of N over all test cases does not exceed 106
Subtasks
Subtask #1 (50 points):

N≤103
K=2
the sum of N over all test cases does not exceed 104
Subtask #2 (50 points): original constraints

Example Input
2
6 2
1 1 1 2 2 1
5 3
1 1 2 2 1
Example Output
3
5
"""

tCases = int(input())
for t in range(tCases):
    numCakes, numFlavour = map(int, input().split())
    index = {}
    cakes = list(map(int, input().split()))
    maxLength = 0
    lList = []
    for i in range (numCakes):
        if cakes[i] in index:
            index[cakes[i]] = i
        else:
            index.update({cakes[i]:i})
        maxLength += 1
        if len(index) == numFlavour:
            lastFlavour = min(index, key=index.get)
            lastIndex = index[lastFlavour]
            index.pop(lastFlavour)
            lList.append(maxLength-1)
            maxLength = i - lastIndex
    lList.append(maxLength)
    print(max(lList))