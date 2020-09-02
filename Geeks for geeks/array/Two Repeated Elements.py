"""
You are given an array of N+2 integer elements. All elements of the array are in range 1 to N. And all elements occur
once except two numbers which occur twice. Find the two repeating numbers.

Input:
The first line of the input contains an integer T, denoting the total number of test cases. Then T test cases follow
Each test case consists of two lines. First line of each test case contains an integer N denoting the range of numbers
to be inserted in array of size N+2. Second line of each test case contains the N+2 space separated integers denoting
the array elements.

Output:
Print the two elements occuring twice in the array. Order of the two elements must be preserved as in the original list,
i.e., print the element which arrives first(2nd time).

Constraints:
1 ≤ T ≤ 30
1 ≤ N ≤ 105

Example:
Input:
2
4
1 2 1 3 4 3
5
2 4 3 1 2 7 4

Output:
1 3
2 4

Explanation:
Testcase 1: In the given array, 1 and 3 are repeated two times.
"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    freqDict = {}
    for i in arr:
        if i not in freqDict:
            freqDict.update({i: 1})
        else:
            print(i, end=" ")
    print()