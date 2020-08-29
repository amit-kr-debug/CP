"""
You are given an array a consisting of n integers. You have to find the length of the smallest (shortest) prefix of elements you need to erase from a to make it a good array. Recall that the prefix of the array a=[a1,a2,…,an] is a subarray consisting several first elements: the prefix of the array a of length k is the array [a1,a2,…,ak] (0≤k≤n).

The array b of length m is called good, if you can obtain a non-decreasing array c (c1≤c2≤⋯≤cm) from it, repeating the following operation m times (initially, c is empty):

select either the first or the last element of b, remove it from b, and append it to the end of the array c.
For example, if we do 4 operations: take b1, then bm, then bm−1 and at last b2, then b becomes [b3,b4,…,bm−3] and c=[b1,bm,bm−1,b2].

Consider the following example: b=[1,2,3,4,4,2,1]. This array is good because we can obtain non-decreasing array c from it by the following sequence of operations:

take the first element of b, so b=[2,3,4,4,2,1], c=[1];
take the last element of b, so b=[2,3,4,4,2], c=[1,1];
take the last element of b, so b=[2,3,4,4], c=[1,1,2];
take the first element of b, so b=[3,4,4], c=[1,1,2,2];
take the first element of b, so b=[4,4], c=[1,1,2,2,3];
take the last element of b, so b=[4], c=[1,1,2,2,3,4];
take the only element of b, so b=[], c=[1,1,2,2,3,4,4] — c is non-decreasing.
Note that the array consisting of one element is good.

Print the length of the shortest prefix of a to delete (erase), to make a to be a good array. Note that the required length can be 0.

You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤2⋅104) — the number of test cases. Then t test cases follow.

The first line of the test case contains one integer n (1≤n≤2⋅105) — the length of a. The second line of the test case contains n integers a1,a2,…,an (1≤ai≤2⋅105), where ai is the i-th element of a.

It is guaranteed that the sum of n does not exceed 2⋅105 (∑n≤2⋅105).

Output
For each test case, print the answer: the length of the shortest prefix of elements you need to erase from a to make it a good array.

Example
inputCopy
5
4
1 2 3 4
7
4 3 3 8 4 5 2
3
1 1 1
7
1 3 1 4 5 3 2
5
5 4 3 2 3
outputCopy
0
4
0
2
3
"""


tCases = int(input())
for _ in range(tCases):
    n = int(input())
    a = list(map(int, input().split()))
    index = n-1
    while index > 0:
        if a[index] > a[index-1]:
            break
        index -= 1
    while index > 0:
        if a[index] < a[index-1]:
            break
        index -= 1
    print(index)