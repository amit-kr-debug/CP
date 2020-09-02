tCases = int(input())
for _ in range(tCases):
    k = int(input())
    n = int(input())
    arr = list(map(int, input().split()))
    if n > 1:
        if arr[0] >= arr[1] and arr[0] > k:
            arr[0] -= k
        else:
            arr[0] += k
        for i in range(1, n):
            if arr[i] >= arr[i-1] and arr[i] > k:
                arr[i] -= k
            else:
                arr[i] += k
    low = min(arr)
    high = max(arr)
    print(arr)
    print(high-low)