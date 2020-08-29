"""
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number
is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case first line contains
N(size of array). The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ C[i] ≤ 107

Example:
Input:
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output:
4
9

Explanation:
Testcase 1: Given array : 1 2 3 5. Missing element is 4.
"""
"""
# if the array is sorted
tCases = 1
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    low = 0
    high = n-2
    if n > 2:
        count = 0
        while low < high:
            # print(low, high)
            # print(arr[low], arr[high])
            mid = (low + high) // 2
            if arr[mid] == mid+1:
                low = mid+1
            elif arr[mid] > mid+1:
                high = mid
        print(low+1)
    elif n == 2:
        if arr[0] == 1:
            print(2)
        elif arr[0] == 2:
            print(1)
    elif n == 1:
        print(1)
"""

