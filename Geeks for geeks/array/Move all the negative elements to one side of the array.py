"""
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative
numbers appear before all positive numbers.
Examples :

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
"""

arr = list(map(int, input().split()))
l = 0
h = len(arr)-1

while h>l:
    while arr[l]>0:
        l+=1
    while arr[h]<0:
        h-=1
    arr[l],arr[h] = arr[h],arr[l]

arr[l],arr[h] = arr[h],arr[l]
print(arr)