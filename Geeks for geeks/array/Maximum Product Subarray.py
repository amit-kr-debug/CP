"""
Given an array A that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray such that after taking the mod by 1000000007, the product is maximum.

Input:
First line of input contain number of test cases T. First line of test case contain the size of array and second line of test case contain the array elements.

Output:
Output the maximum product of subarray.

Constraints:
1 <= T <= 100
1 <= N <= 104
-104 <= Ai <= 104

Example:
Input:
3
5
6 -3 -10 0 2
6
2 3 4 5 -1 0
10
8 -2 -2 0 8 0 -6 -8 -6 -1

Output:
180
120
288

Explanation:
Testcase 1: Subarray with maximum product is 6, -3, -10 which gives product as 180.
"""


tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    mul = 1
    prev = 1
    firstNeg = 1
    ans = -10000000000000000000000000000
    for i in range(n):
        mul *= arr[i]
        ans = max(ans, mul)
        if arr[i] < 0:
            if firstNeg == 1:
                firstNeg = mul
            prev *= mul
            if prev > 0:
                mul = prev
                prev = 1
                ans = max(ans, mul)
            else:
                mul = 1
                if firstNeg != 1:
                    ans = max(ans, prev//firstNeg)
        if arr[i] > 0:
            ans = max(ans, prev*mul//firstNeg)
        if arr[i] == 0:
            mul = 1
            prev = 1
            firstNeg = 1
    print(ans)


"""
second solution

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    max_so_far = 1
    max_at_pos = 1
    min_at_pos = 1
    for i in range(n):
        if arr[i]>0:
            max_at_pos = max_at_pos*arr[i]
            min_at_pos =  min (min_at_pos * arr[i], 1)
        if arr[i]==0:
            max_at_pos = 1
            min_at_pos = 1
        if arr[i]<0:
            temp = max_at_pos
            max_at_pos = max(min_at_pos*arr[i], 1)
            min_at_pos = temp*arr[i]
        max_so_far = max(max_at_pos, max_so_far)
    print(max_so_far)
"""