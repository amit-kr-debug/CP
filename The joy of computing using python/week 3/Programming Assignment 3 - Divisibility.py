"""
In this program, create a list of numbers from 1 to 50 named list_1. The numbers should be present in the increasing order: Ex list_1 = [1,2,3,4,5,....,50]

i.e. index zero should be 1, index one should be 2, index two should be 3 and so on.


Given an input let's say a, you have to print the number of elements of list_1 which are divisible by a,  excluding the element which is equal to a.

Input:
Number a

Output:
In a single line, the number of elements (i.e. the count and not the elements) which are divisible by a.

Example:
Input:

24

Output:
1

Explanation: Since there is only one number, i.e. 48 which is divisible by 24 and is in the list_1. We have to exclude the element 24 of list_1 because it is equal to the input.
"""

a = int(input())
count = -1
for i in range(1, 51):
    if i % a == 0:
        count += 1
print(count, end="")
