ans = []

def isBalanced():
    for word in arr:
        tempDict = {}
        for letter in word:
            if letter in tempDict:
                tempDict.pop(letter)
            else:
                tempDict[letter] = 1
        if len(tempDict) == 0:
            ans.append(word)



str1 = input()
arr = [str1[i: j] for i in range(len(str1))
           for j in range(i + 1, len(str1) + 1)]
isBalanced()

ans.sort(key = lambda item: (len(item), item))
for i in ans:
    print(i, end=" ")