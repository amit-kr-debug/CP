def insertArr(arr1, ele):
    if len(arr1) == 0 or arr[len(arr1)-1] <= ele:
        arr1.append(ele)
        return
    temp = arr1.pop()
    insertArr(arr1, ele)
    arr1.append(temp)


def sortArr(arr1):
    if len(arr1) == 0:
        return
    temp = arr1.pop()
    sortArr(arr1)
    insertArr(arr1, temp)


arr = [1, 8, 7, 10, 0, 4, 8]
n = len(arr)
sortArr(arr)
print(arr)