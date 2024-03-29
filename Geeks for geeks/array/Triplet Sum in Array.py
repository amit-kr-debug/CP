"""
Given an array A[] of N numbers and another number x, determine whether or not there exist three elements in A[] whose sum is exactly x.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains n and x. Next line contains array elements.

Output:
Print 1 if there exist three elements in A whose sum is exactly x, else 0.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 103
1 ≤ A[i] ≤ 105

Example:
Input:
2
6 13
1 4 45 6 10 8
5 10
1 2 4 3 6

Output:
1
1

Explanation:
Testcase 1: There is one triplet with sum 13 in the array. Triplet elements are 1, 4, 8, whose sum is 13.
"""

"""
#hash based solution  timeC = O(n^2) spaceC= O(n)
tCases = int(input())
for _ in range(tCases):
    n, tSum = map(int, input().split())
    arr = list(map(int, input().split()))
    freqDict = {}
    flag = 0
    for i in arr:
        if i not in freqDict:
            freqDict.update({i: 1})
        else:
            freqDict[i] += 1
    for i in range(n):
        freqDict[arr[i]] -= 1
        for j in range(n):
            if i == j:
                continue
            else:
                freqDict[arr[j]] -= 1
            if tSum-(arr[i]+arr[j]) in freqDict:
                if freqDict[tSum-(arr[i]+arr[j])] > 0:
                    flag = 1
                    break
            freqDict[arr[j]] += 1
        freqDict[arr[i]] += 1
    if flag:
        print(1)
    else:
        print(0)
"""


#two pointer solution timeC = O(n^2) spaceC= O(1)

def find3Numbers(self,A,n,X):
    # Your Code Here
    ans = False
    A.sort()
    for i in range(n - 2):
        a = A[i]
        low = i + 1
        high = n - 1
        while low < high:
            triplet = A[low] + A[high] + a
            if triplet == X:
                ans = True
                return ans
            elif triplet > X:
                high -= 1
            else:
                low += 1
    return ans