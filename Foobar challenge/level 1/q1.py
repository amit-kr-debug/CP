# 1st sol prisoners
def solution(x, y):

    # Your code here
    freq = {}
    for i in x:
        if i in freq:
            freq[i] += 1
        else:
            freq.update({i: 1})
    for i in y:
        if i in freq:
            if freq[i] == 1:
                freq.pop(i)
            else:
                freq[i] -= 1
        else:
            freq.update({i: 1})
    for key, values in freq.items():
        uni = key
    return uni