"""
Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order without using any extra space. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.


Example 1:

Input:
n = 4, arr1[] = [1 3 5 7]
m = 5, arr2[] = [0 2 6 8 9]
Output:
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]
Explanation:
After merging the two
non-decreasing arrays, we get,
0 1 2 3 5 6 7 8 9.
Example 2:

Input:
n = 2, arr1[] = [10, 12]
m = 3, arr2[] = [5 18 20]
Output:
arr1[] = [5 10]
arr2[] = [12 18 20]
Explanation:
After merging two sorted arrays
we get 5 10 12 18 20.


Your Task:
You don't need to read input or print anything. You only need to complete the function merge() that takes arr1, arr2, n and m as input parameters and modifies them in-place so that they look like the sorted merged array when concatenated.


Expected Time Complexity:  O((n+m) log(n+m))
Expected Auxilliary Space: O(1)


Constraints:
1 <= n, m <= 5*104
0 <= arr1i, arr2i <= 107
"""

# User function Template for python3
import math


class Solution:

    # Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        # code here
        total_len = n + m
        gap = math.ceil(total_len / 2)

        while gap != 0:

            p1 = 0
            p2 = gap
            while p2 != total_len:
                if p1 < p2 < n:
                    if arr1[p1] > arr1[p2]:
                        arr1[p1],arr1[p2] = arr1[p2],arr1[p1]
                if p1 < n <= p2:
                    if arr1[p1] > arr2[p2 - n]:
                        arr1[p1],arr2[p2 - n] = arr2[p2 - n],arr1[p1]
                if n <= p1:
                    if arr2[p1 - n] > arr2[p2 - n]:
                        arr2[p1 - n],arr2[p2 - n] = arr2[p2 - n],arr2[p1 - n]
                p1 += 1
                p2 += 1
            if gap == 1:
                gap = 0
            gap = math.ceil(gap / 2)


# {
#  Driver Code Starts
# Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int,input().strip().split())
        arr1 = list(map(int,input().strip().split()))
        arr2 = list(map(int,input().strip().split()))
        ob = Solution()
        ob.merge(arr1,arr2,n,m)
        print(*arr1,end = " ")
        print(*arr2)
# } Driver Code Ends
