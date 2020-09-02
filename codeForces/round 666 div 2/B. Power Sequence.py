"""
Let's call a list of positive integers a0,a1,...,an−1 a power sequence if there is a positive integer c, so that for every 0≤i≤n−1 then ai=ci.

Given a list of n positive integers a0,a1,...,an−1, you are allowed to:

Reorder the list (i.e. pick a permutation p of {0,1,...,n−1} and change ai to api), then
Do the following operation any number of times: pick an index i and change ai to ai−1 or ai+1 (i.e. increment or decrement ai by 1) with a cost of 1.
Find the minimum cost to transform a0,a1,...,an−1 into a power sequence.

Input
The first line contains an integer n (3≤n≤105).

The second line contains n integers a0,a1,...,an−1 (1≤ai≤109).

Output
Print the minimum cost to transform a0,a1,...,an−1 into a power sequence.

Examples
inputCopy
3
1 3 2
outputCopy
1
inputCopy
3
1000000000 1000000000 1000000000
outputCopy
1999982505
"""
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
nRoot = arr[n - 1] ** (1.0 / float(n - 1))
n1Root = int(nRoot)+1
n2Root = int(nRoot)
ans = 0
ans1 = 0
n1 = 1
n2 = 1
for i in range(n):
    ans += abs(arr[i] - n1)
    ans1 += abs(arr[i] - n2)
    if i != n - 1:
        n1 *= n1Root
        n2 *= n2Root
print(min(ans1, ans))