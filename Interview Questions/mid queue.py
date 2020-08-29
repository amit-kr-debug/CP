n = int(input())
ans = []
for i in range(n):
    ans.insert((i+1)//2, chr(97+i))
for i in ans:
    print(i, end=" ")