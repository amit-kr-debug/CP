"""
Given the marks of five subjects, you have to calculate and print the average of the total marks.

Input:

Marks of different subjects in new line.

Output:

output the average number

Example:

Input:

24
21
35
41
52

Output:
34.6

Explanation :  The marks are s1 = 24, s2 = 21, s3 = 35, s4 = 41, s5 = 52, hence the average is 34.6
"""

s = int(input())
s += int(input())
s += int(input())
s += int(input())
s += int(input())
print(s/5, end="")