str = "this is a string"

dict = {}
for i in range (len(str)):
    if str[i] in dict:
        dict[str[i]] += 1
    else:
        dict.update({str[i]: 1})

print(dict)
