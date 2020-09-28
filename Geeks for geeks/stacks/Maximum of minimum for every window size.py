"""
Given an integer array A[] of size N. The task is to find the maximum of the minimum of every window size in the array.
Note: Window size varies from 1 to n.

Input:
The first line contains an integer T denoting the total number of test cases. In each test cases, the first line
contains an integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN
denoting the elements of the array.

Output:
In each seperate line, print the array of numbers of size N for each of the considered window size 1, 2 , ..., N
respectively.

Constraints:
1 <= T <= 50
1 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
7
10 20 30 50 10 70 30
3
10 20 30

Output:
70 30 20 10 10 10 10
30 20 10

Explaination:
Testcase 1:
First element in output indicates maximum of minimums of all windows of size 1. Minimums of windows of size 1 are {10},
 {20}, {30}, {50}, {10}, {70} and {30}. Maximum of these minimums is 70.
Second element in output indicates maximum of minimums of all windows of size 2. Minimums of windows of size 2 are {10},
{20}, {30}, {10}, {10}, and {30}. Maximum of these minimums is 30.
Third element in output indicates maximum of minimums of all windows of size 3. Minimums of windows of size 3 are {10},
{20}, {10}, {10} and {10}. Maximum of these minimums is 20.
Similarly other elements of output are computed.
"""

tCases = int(input())
for _ in range(tCases) :
    n = int(input())
    arr = list(map(int, input().split()))
    pse = [-1 for i in range(n)]
    nse = [n for i in range(n)]
    stack = [n - 1]
    index = 0

    for i in range(n - 2, -1, -1) :
        while index >= 0 and arr[stack[index]] > arr[i] :
            pse[stack.pop()] = i
            index -= 1
        stack.append(i)
        index += 1
    # pse[0] = 0
    stack = [0]
    index = 0

    for i in range(1, n) :
        while index >= 0 and arr[stack[index]] > arr[i] :
            nse[stack.pop()] = i
            index -= 1
        stack.append(i)
        index += 1

    ans = [0] * (n + 1)

    for i in range(n) :
        Len = nse[i] - pse[i] - 1
        ans[Len] = max(ans[Len], arr[i])

    for i in range(n - 1, 0, -1) :
        ans[i] = max(ans[i], ans[i + 1])

    for i in range(1, n + 1) :
        print(ans[i], end=" ")
    print()


