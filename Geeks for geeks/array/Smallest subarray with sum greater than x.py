"""
Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.

Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).

Example 1:

Input:
A[] = {1, 4, 45, 6, 0, 19}
x  =  51
Output: 3
Explanation:
Minimum length subarray is
{4, 45, 6}

Example 2:
Input:
A[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Explanation:
Minimum length subarray is {10}


Your Task:
You don't need to read input or print anything. Your task is to complete the function sb() which takes the array A[],
its size N and an integer X as inputs and returns the required ouput.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N, x ≤ 105
1 ≤ A[] ≤ 104
"""


class Solution:
    def sb(self,a,n,x):
        # Your code goes here
        currSum = 0
        minL = n + 1

        start = 0
        end = 0

        while end < n:
            while currSum <= x and end < n:
                currSum += a[end]
                end += 1
            while start < n and currSum > x:
                minL = min(minL,end - start)
                currSum -= a[start]
                start += 1

        return minL


# {
#  Driver Code Starts
def main():
    T = int(input())

    while (T > 0):
        sz = [int(x) for x in input().strip().split()]
        n,m = sz[0],sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().sb(a,n,m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends