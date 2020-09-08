"""
Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

Input:
The first line of input contains an integer T, denoting the number of testcases. Then T test cases follow. Each test case consists of three lines. First line of each testcase contains an integer N denoting size of the array. Second line contains N space separated integer denoting elements of the array. Third line of the test case contains an integer K.

Output:
Corresponding to each test case, print the kth smallest element in a new line.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= arr[i] <= 105
1 <= K <= N

Example:
Input:
2
6
7 10 4 3 20 15
3
5
7 10 4 20 15
4
Output:
7
15
"""
import heapq
tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    for i in range(n):
        arr[i] *= -1
    maxHeap = []
    heapq.heapify(maxHeap)
    for i in range(n):
        heapq.heappush(maxHeap, arr[i])
        if len(maxHeap) > k:
            heapq.heappop(maxHeap)
    print(heapq.heappop(maxHeap)*-1)


"""
2nd sol
tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    # print(heapq.nsmallest(k, arr, key=None).pop())
    heapq._heapify_max(arr)
    for i in range(n-k):
        heapq._heappop_max(arr)
    print(heapq._heappop_max(arr))
"""