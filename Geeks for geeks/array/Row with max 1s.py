"""
Given a boolean 2D array where each row is sorted. Find the row with the maximum number of 1s.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case contains n and m, where n is the number of rows and m is the number of columns.
The second line of each test case contains the array elements.

Output:
Print the row with the maximum number of 1s.

Constraints:
1 ≤ T ≤ 50
1 ≤ n,m ≤ 103

Example:
Input:
2
4 4
0 1 1 1 0 0 1 1 1 1 1 1 0 0 0 0
2 2
0 0 1 1

Output:
2
1

Explanation :
Testcase 1 : Row 2 is having maximum number of 1s (0-based indexing).
"""

tCases = int(input())
for _ in range(tCases):
    val = list(map(int, input().split()))
    n = val[0]
    m = val[1]
    arr = []
    while len(arr) < n * m:
        try:
            arr += list(map(int, input().split()))
        except:
            break
    ans = 0
    j = m - 1
    for i in range(m):
        if arr[i] == 1:
            j = i
            break

    for i in range(n):
        try:
            while j >= 0 and arr[j + i * m] == 1:
                j = j - 1
                ans = i
        except:
            print(i * m + j, len(arr))
    print(ans)
