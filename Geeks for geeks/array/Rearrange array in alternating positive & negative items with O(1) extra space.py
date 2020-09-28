"""

Rearrange array in alternating positive & negative items with O(1) extra space

Input :
arr[] = {-2, 3, 4, -1}
Output :
arr[] = {-2, 3, -1, 4} OR {-1, 3, -2, 4} OR ..

Input :
arr[] = {-5, 3, 4, 5, -6, -2, 8, 9, -1, -4}
Output :
arr[] = {-5, 3, -2, 5, -6, 4, -4, 9, -1, 8}

Input :
arr[] = {-2, 3, 1}
Output :
arr[] = {-2, 3, 1} OR {-2, 1, 3}

"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    j = n-1
    while i < j:
        while arr[i] > 0:
            i += 1
            if i == n-1:
                break
        while arr[j] < 0:
            j -= 1
            if j == 0:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    index = 0
    while index < n and i < n:
        arr[index], arr[i] = arr[i], arr[index]
        i += 1
        index += 2
    print(arr)