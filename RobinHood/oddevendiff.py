def oddevendiff(arr):
    even = 0
    odd = 0
    for i in arr:
        if i%2 ==0:
            even+=i
        else:
            odd+=i
    return odd -even

