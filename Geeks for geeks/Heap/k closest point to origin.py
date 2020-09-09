"""
Given a list of n points on 2D plane, the task is to find the K (k < n) closest points to the origin O(0, 0).
Note: The distance between a point P(x, y) and O(0, 0) using the standard Euclidean Distance.
Examples:

Input: [(1, 0), (2, 1), (3, 6), (-5, 2), (1, -4)], K = 3
Output: [(1, 0), (2, 1), (1, -4)]
Explanation:
Square of Distances of points from origin are
(1, 0) : 1
(2, 1) : 5
(3, 6) : 45
(-5, 2) : 29
(1, -4) : 17
Hence for K = 3, the closest 3 points are (1, 0), (2, 1) & (1, -4).

Input: [(1, 3), (-2, 2)], K = 1
Output: [(-2, 2)]
Explanation:
Square of Distances of points from origin are
(1, 3) : 10
(-2, 2) : 8
Hence for K = 1, the closest point is (-2, 2).
"""

import heapq

n = 3
arr = [[3, 3], [5, -1], [-2, 4]]
k = 2

maxHeap = []

for i in range(n):
    heapq.heappush(maxHeap, (-arr[i][0]**2-arr[i][1]**2, arr[i]))
    if len(maxHeap) > k:
        heapq.heappop(maxHeap)
for i in range(k):
    a, b = heapq.heappop(maxHeap)
    print(b, -a)