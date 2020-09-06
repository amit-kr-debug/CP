"""

"""
tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [-1 for x in range(n)]
    stack = [0]
    top = 0
    for i in range(n):
        while top >= 0 and arr[i] < arr[stack[top]]:
            ans[stack.pop()] = arr[i]
            top -= 1
        stack.append(i)
        top += 1
    for i in ans:
        print(i, end=" ")
