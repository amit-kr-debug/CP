"""
Given an integer array. The task is to find the first repeating element in the array i.e., an element that occurs more
than once and whose index of first occurrence is smallest.

Input :
The first line contains an integer T denoting the total number of test cases. In each test cases, First line is number
of elements in array N and second line contains N space separated integer values of the array.

Output:
In each separate line print the index of first repeating element, if there is not any repeating element then print “-1”
(without quotes). Use 1 Based Indexing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 106

Example:
Input:
3
7
1 5 3 4 3 5 6
4
1 2 3 4
5
1 2 2 1 3
Output:
2
-1
1

Explanation:
Testcase 1: 5 is appearing twice and its first appearence is at index 2 which is less than 3 whose first occuring index
is 3.
Testcase 2: None of the elements are occuring twice . So, the answer is -1.
Testcase 3: 1 is appearing twice and its first appearence is at index 1 which is less than 2 whose first occuring is at
index 2.
"""


tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    dupDict = {}
    ans = -1
    for i in arr:
        if i in dupDict:
            dupDict[i] += 1
        else:
            dupDict.update({i: 1})
    for i in range(n):
        if dupDict[arr[i]]>1:
            ans = i+1
            break
    print(ans)