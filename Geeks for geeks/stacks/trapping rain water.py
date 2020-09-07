"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.
Examples:

Input: arr[]   = {2, 0, 2}
Output: 2
"""

tCases = int(input())
for t in range(0, tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    # finding the next biggest element in right
    rMax = [0 for x in range(n)]
    rMax[n - 1] = arr[n - 1]
    tempMax = arr[n - 1]
    for i in range(n - 2, -1, -1):
        tempMax = max(arr[i], tempMax)
        rMax[i] = tempMax
    # finding the next biggest element in left
    lMax = [0 for x in range(n)]
    lMax[0] = arr[0]
    tempMax = arr[0]
    for i in range(0, n):
        tempMax = max(arr[i], tempMax)
        lMax[i] = tempMax
    water = 0
    for i in range(0, n-1):
        water += min(rMax[i], lMax[i]) - arr[i]
    print(water)


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