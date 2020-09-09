"""
Given an array of positive integers and two positive integers K1 and K2. Find sum of all elements greater tha K1th and
smaller than K2th smallest elements of array.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test
case contains an integer N, denoting the length of the array. Next line contains N space separated integers of the
array. Third line contains two space separated integers denoting K1th and K2th smallest elements.

Output:
For each test case, output the sum of all the elements between K1th and K2th smallest elements.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= K1, K2 <= 1014

Example:
Input
2
7
20 8 22 4 12 10 14
3 6
6
10 2 50 12 48 13
2 6

Output:
26
73

Explanation:
Test Case 1:
3rd smallest element is 10
6th smallest element is 20
Sum of all element between K1 & K2 is 12 + 14 = 26
"""
# code for distinct elements
import heapq


def kthSmallest(k):
    maxHeap = []
    for i in range(n):
        heapq.heappush(maxHeap, -arr[i])
        if len(maxHeap) > k:
            heapq.heappop(maxHeap)
    return -heapq.heappop(maxHeap)


tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    k1, k2 = map(int, input().split())
    n1, n2 = kthSmallest(k1), kthSmallest(k2)
    ans = 0
    if n1 > n2:
        n2, n1 = n1, n2
    # print(n2, n1)
    for i in arr:
        if n1 < i < n2:
            ans += i
    print(ans)
"""
import heapq
tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    k1, k2 = map(int, input().split())
    maxHeap = []
    ans = 0
    for i in range(n):
        heapq.heappush(maxHeap, -arr[i])
        if len(maxHeap) > k2-1:
            heapq.heappop(maxHeap)

    for i in range(k2-k1-1):
        ans -= heapq.heappop(maxHeap)
    print(ans)
"""