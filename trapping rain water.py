"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.
Examples:

Input: arr[]   = {2, 0, 2}
Output: 2
"""

import numpy as np

tCases = int(input())

for t in range(0, tCases):
    length = int(input())
    input_list = np.array(input().split(), int)

    biggest = maximum = input_list[0]
    totalWater = 0
    water = 0
    for i in range(0, length):
        x = input_list[i]
        if i < length - 1:
            maximum = np.amax(input_list[i + 1:])

        if x <= biggest <= maximum:
            water = biggest - x
            totalWater += water
        else:
            if maximum >= x:
                biggest = x
            else:
                biggest = maximum

    print(totalWater)