"""
Given an array A[ ] denoting heights of N towers and a positive integer K, modify the heights of each tower either by increasing or decreasing them by K only once and then find out the minimum difference of the heights of shortest and longest towers.

Example

Input  : A[] = {1, 15, 10}, k = 6
Output : 5
Explanation : We change 1 to 7, 15 to
9 and 10 to 4. Maximum difference is 5
(between 4 and 9). We can't get a lower
difference.

Input
The first line of input contains an integer T denoting the number of test cases. Then
T test cases follow. The first line of each test case contains a positive integer K.
The second line of each test case contains a positive integer N, denoting number of towers.
The third line of the test cases contains N integers denoting the heights of N towers.

Output
For each test case in new line print out the minimum difference of heights possible.

Constraints
1 <= T <= 100
0 <   K <= 30
0 <   N <= 30
0 <= A[i] <= 500


Examples
Input
3
2
4
1 5 8 10
3
5
3 9 12 16 20
4
6
100 150 200 250 300 400

Output
5
11
292

Explanation:
Test Case 1: arr[] = {1, 5, 8, 10}. k = 2
The array can be modified as: {3, 3, 6, 8}. The difference between the largest and the smallest is 8-3 = 5.
We can't have a difference less than this.
Test Case 2: arr[] = {3 9 12 16 20}. k = 3
The array can be modified as: {6 12 9 13 17}. The difference between the largest and the smallest is 17-6 = 11.
"""

tCases = int(input())
for _ in range(tCases):
    k = int(input())
    n = int(input())
    arr = list(map(int, input().split()))
    if n > 1:
        minN = min(arr)
        maxN = max(arr)
        # initialising ans with maxN - minN to consider the case if abs((maxN-k) - (minN+k)) > abs(maxN - minN)
        ans = maxN - minN
        maxN -= k
        minN += k
        for i in range(n):
            # first two conditions are to keep the number between min and max values
            if minN <= arr[i] - k <= maxN:
                arr[i] -= k
            elif minN <= arr[i] + k <= maxN:
                arr[i] += k
            # but if that's not possible then we will calculate which will cost us less, subtracting or adding
            else:
                if abs(arr[i] - k - minN) < abs(arr[i] + k - maxN):
                    arr[i] -= k
                else:
                    arr[i] += k
        print(min(ans, max(arr) - min(arr)))
    else:
        print(0)
