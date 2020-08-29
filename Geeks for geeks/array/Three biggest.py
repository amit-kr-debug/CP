"""
Given an array with all distinct elements, find the largest three
elements. Expected time complexity is O(n) and extra space is O(1).
Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23
"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    first = -10**18
    second = -10**18
    third = -10**18
    for i in arr:
        if i > first:
            third = second
            second = first
            first = i
        elif i > second:
            third = second
            second = i
        elif i > third:
            third = i
    print(first, second, third)