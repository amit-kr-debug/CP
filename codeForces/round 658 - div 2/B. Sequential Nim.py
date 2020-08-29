tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    player = 1
    flag = False
    for i in range(n):
        if arr[i] > 1:
            flag = True
            if i % 2 == 0:
                player = 1
            else:
                player = 2
            break
    if flag:
        if player == 1:
            print("First")
        elif player == 2:
            print("Second")
    else:
        if n % 2 == 0:
            print("Second")
        else:
            print("First")