"""
A sorted array A[ ] with distinct elements is rotated at some unknown point, the task is to find the minimum element in it.

Expected Time Complexity: O(Log n)

Input:

The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of an integer N, where N is the size of array.
The second line of each test case contains N space separated integers denoting array elements.

Output:
Corresponding to each test case, in a new line, print the minimum element in the array.

Constraints:

1 ≤ T ≤ 200
1 ≤ N ≤ 500
1 ≤ A[i] ≤ 1000

Example:

Input
2
5
4 5 1 2 3
6
10 20 30 40 50 5 7

Output
1
5
"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0] > arr[n-1]:
        low = 0
        high = n-1
        while low < high:
            mid = (low+high) // 2
            # print(arr[low], arr[high], arr[mid])
            if arr[low] > arr[mid] or arr[mid] < arr[high]:
                high = mid
            else:
                low = mid+1

        print(arr[low])
    else:
        print(arr[0])