"""
The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

Example 1:

Input:
N = 7
A[] = {100,180,260,310,40,535,695}
Output: (0 3) (4 6)
Explanation: We can buy stock on day
0, and sell it on 3rd day, which will
give us maximum profit. Now, we buy
stock on day 4 and sell it on day 6.
Example 2:

Input:
N = 5
A[] = {4,2,2,2,4}
Output: (3 4)
Explanation: We can buy stock on day
3, and sell it on 4th day, which will
give us maximum profit.
Your Task:
The task is to complete the function stockBuySell() which takes an array price[] and N as a parameter and finds the days of buying and selling stock and print them. And if there is no profit then print "No Profit". The newline is automatically added by the driver code.

Note: Output format is as follows -
(buy_day sell_day) (buy_day sell_day)

Expected Time Complexity : O(N)
Expected Auxiliary Space: O(N)

Constraints:
2 <= N <= 103
0 <= Ai <= 104
"""


# User function Template for python3

# Complete this function
def stockBuySell(A, n):
    ##Your code here
    minS = A[0]
    index = 1
    minI = 0
    maxI = 0
    while index < n:
        if A[index] <= minS:
            minS = A[index]
            minI = index
            index += 1
            # print(minI)
        else:
            while index < n and A[index] >= A[index - 1]:
                maxI = index
                index += 1
                # print(maxI)
            if index < n:
                minS = A[index]
            if index < n and A[index] < A[index-1]:
                print("(" + str(minI) + " " + str(maxI) + ")", end=" ")
            if index == n and A[index-1] > A[index-2]:
                maxI = index-1
                print("(" + str(minI) + " " + str(maxI) + ")", end=" ")
    print()

def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        stockBuySell(arr, n)

        T -= 1


if __name__ == "__main__":
    main()
