"""
refer to problem statement of Nearest greatest to right
"""

tCases = int(input())
for _ in range(tCases):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [-1 for x in range(n)]
    stack = [n-1]
    top = 0
    for i in range(n-2, -1, -1):
        while top >= 0 and arr[i] > arr[stack[top]]:
            ans[stack.pop()] = arr[i]
            top -= 1
        stack.append(i)
        top += 1
    print(ans)