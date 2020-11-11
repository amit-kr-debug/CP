"""
Python can easily handle large numbers. You can store a huge number easily in python.
In this program, you have to calculate the Factorial of a number.
Given a number k its factorial is i.e. k! = 1x2x3x4x....xk.
For example, if k = 4, 4! = 1x2x3x4 = 24
Read more about Factorial here

Given an input k, you have to print the factorial of k.

Input format:
The number k in a single line

Output Format:
k! in a single line

Example:

Input:
5

Output:
120

Explanation:
Here k is 5, hence 5! is 1x2x3x4x5 which is equal to 120.
"""

k = int(input())
fact = 1
for i in range(1, k+1):
    fact *= i
print(fact)