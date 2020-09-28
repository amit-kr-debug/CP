"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s) :
    news = ""
    prev = ""
    for i in range(len(s)) :
        if i == 0 :
            news += s[0].upper()
        elif prev == " " :
            news += s[i].upper()
        else :
            news += s[i]
        prev = s[i]
    return news


if __name__ == '__main__' :
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
