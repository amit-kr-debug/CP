q = input("Enter the cipher text: ")
c = 0
m = 0
index = 0

h = ""
for g in range(len(q)):
    if q[index] != 'x':
        h = h + q[index]
    index = index + 1

l = len(h)

for m in range(l):
    c = c + 1
    rows = int(l / c)
    rows = rows + 1
    index = 0
    crypt = []
    for i in range(c):
        a = []
        for j in range(rows):
            if (index < len(q)):
                a.append(q[index])
                # print(index,s[index])
                index = index + 1
            else:
                a.append('x')

        crypt.append(a)

    for i in range(c):
        for j in range(rows):
            print(crypt[i][j],end = " ")
        print()
    print("key =",c)
    t = ""
    for i in range(rows):
        for j in range(c):
            p = crypt[j][i]
            # print(p,end="")
            t = t + p
    print(t)