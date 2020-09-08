"""
Given a non-empty array of integers, find the top K elements which have the highest frequency in the array.
If two numbers have the same frequency then the larger number should be given preference.

Example 1:

Input:
N = 6
A[] = {1,1,1,2,2,3}
K = 2
Output: 1 2
Example 2:

Input:
N = 8
A[] = {1,1,2,2,3,3,3,4}
K = 2
Output: 3 2
Explanation: Elements 1 and 2 have the
same frequency ie. 2. Therefore, in this
case, the answer includes the element 2
as 2 > 1.
User Task:
The task is to complete the function TopK() that takes the array and integer K as input and returns a list of top K
frequent elements.

Expected Time Complexity : O(NlogN)
Expected Auxilliary Space : O(N)

Constraints:
1 <= N <= 103
1<=A[i]<=104
"""
import heapq
tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    minHeap = []
    for key, val in freq.items():
        heapq.heappush(minHeap, (val, key))
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    minHeap.sort()
    for i in range(k):
        val, key = minHeap.pop()
        print(key, end=" ")
    print()



"""
2nd sol
tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for key, val in sorted(freq.items(), key = lambda kv:(kv[1], kv[0]), reverse=True):
        if k > 0:
            print(key, end=" ")
            k -= 1
"""