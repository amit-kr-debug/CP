"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.
Examples:

Input: arr[]   = {2, 0, 2}
Output: 2
"""


def trappingWater(self,arr,n):
    # Code here
    GR = [-1 for i in range(n)]
    GL = [-1 for i in range(n)]
    maxR = arr[n - 1]
    maxL = arr[0]
    for i in range(1,n):
        maxL = max(maxL,arr[i])
        GL[i] = maxL

    for i in range(n - 2,-1,-1):
        maxR = max(maxR,arr[i])
        GR[i] = maxR

    trappedWater = 0
    for i in range(n):
        temp = min(GR[i],GL[i]) - arr[i]
        if temp > 0:
            trappedWater += temp
    return trappedWater


"""
sol - 2
def trappingWater(input_list, length):
    biggest = maximum = input_list[0]
    nMax = [0 for x in range(length)]
    nMax[length-1] = input_list[length-1]
    tempMax = input_list[length-1]
    for i in range(length-2, -1, -1):
        tempMax = max(input_list[i], tempMax)
        nMax[i] = tempMax
    totalWater = 0
    water = 0
    for i in range(0, length):
        x = input_list[i]
        if i < length - 1:
            maximum = nMax[i+1]

        if x <= biggest <= maximum:
            water = biggest - x
            totalWater += water
        else:
            if maximum >= x:
                biggest = x
            else:
                biggest = maximum
    return totalWater
 
"""