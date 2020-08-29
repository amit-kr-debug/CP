def bin_search(arr, low, high, key):
    high = len(arr)-1
    mid = (high + low)//2
    while low >= high:
        print(mid)
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            low = mid+1
            mid = (high + low)//2
        else:
            high = mid-1
            mid = (high + low)//2
    return -1


if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        x=int(input())
        print (bin_search(arr, 0, 0, x))
