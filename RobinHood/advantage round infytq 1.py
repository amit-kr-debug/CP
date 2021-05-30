def mergeSlide(arr:list):
    arr.sort()
    print(arr)
    countSequence = 0
    tempSequence = 0
    countRepeat = 0
    tempRepeat = 0
    flagRepeat = True
    flagSequence = True
    for i in range(1, len(arr)):
        if arr[i-1] + 1 == arr[i]:
            if flagRepeat:
                tempRepeat = 0
                flagRepeat = False
                tempSequence += 1
            tempSequence += 1
            flagSequence = True
            # print("s", arr[i], tempSequence)
            if tempSequence >= 3:
                countSequence += 1
        if arr[i-1] == arr[i]:
            if flagSequence:
                tempSequence = 0
                flagSequence = False
                tempRepeat += 1
            tempRepeat += 1
            flagRepeat = True
            # print("r", arr[i], tempRepeat)
            if tempRepeat >= 3:
                countRepeat += 1
    return countRepeat+countSequence
print(mergeSlide([1,1,1,1,1,2,2,2,3,4,5]))