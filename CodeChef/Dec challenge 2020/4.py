import math

for k in range (int (input ())):
    n,x = map (int,input ().split ())
    a = list (map (int,input ().split ()))
    if n <101:
        i = 0
        while x > 0 and i < n - 1:
            flag = 0

            p = int (math.log2 (a[i]) // math.log2 (2))
            # print(p,"L")
            r = 2 ** p
            a[i] ^= r
            for j in range (i + 1,n):
                if a[j] ^ r < a[j]:
                    a[j] ^= r
                    flag = 1
                    break
            if flag == 0:
                a[n - 1] ^= r

            while i < n and a[i] == 0:
                i += 1
            z = x + 1
            x -= 1

        if z > 0:
            if n < 3 and (z % 2 > 0):
                a[n - 2] = a[n - 2] ^ 1
                a[n - 1] = a[n - 1] ^ 1

        print (*a)
    else:
        i = 0
        while x > 0 and i < n - 1:
            flag = 0

            p = int (math.log2 (a[i]) // math.log2 (2))
            # print(p,"L")
            r = 1 << p
            a[i] ^= r
            for j in range (i + 1,n):
                if a[j] ^ r < a[j]:
                    a[j] ^= r
                    flag = 1
                    break
            if flag == 0:
                a[n - 1] ^= r

            while i < n and a[i] == 0:
                i += 1
            z = x + 1
            x -= 1

        if z > 0:
            if n < 3 and (z % 2 > 0):
                a[n - 2] = a[n - 2] ^ 1
                a[n - 1] = a[n - 1] ^ 1

        print (*a)