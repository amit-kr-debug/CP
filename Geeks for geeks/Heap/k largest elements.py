"""
Given an array of N positive integers, print k largest elements from the array.  The output elements should be printed
in decreasing order.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N
and k, N is the size of array and K is the largest elements to be returned. The second line of each test case contains
N input C[i].

Output:
Print the k largest element in descending order.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100
K ≤ N
1 ≤ C[i] ≤ 1000

Example:
Input:
2
5 2
12 5 787 1 23
7 3
1 23 12 9 30 2 50

Output:
787 23
50 30 23

Explanation:
Testcase 1: 1st largest element in the array is 787 and second largest is 23.
Testcase 2: 3 Largest element in the array are 50, 30 and 23.
"""
import heapq
tCases = int(input())
for _ in range(tCases):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in heapq.nlargest(m, arr, key=None):
        print(i, end=" ")
    print()
