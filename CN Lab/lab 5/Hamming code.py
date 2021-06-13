import random

pos = []


def calcRedundantBits(m):
    for i in range(m):
        if 2 ** i >= m + i + 1:
            return i


def posRedundantBits(data,r):
    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r + 1):
        if i == 2 ** j:
            res = res + '0'
            j += 1
            pos.append(i)
        else:
            res = res + data[-1 * k]
            k += 1
    return res[::-1]


def calcParityBits(arr, r):
    n = len(arr)
    # For finding rth parity bit, iterate over
    # 0 to r - 1
    for i in range(r):
        val = 0
        for j in range(1,n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-1 * j])

        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr


def detectError(arr, nr):
    n = len(arr)
    res = 0
    # Calculate parity bits again
    for i in range(nr):
        val = 0
        for j in range(1,n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-1 * j])
        res = res + val * (10 ** i)
    # Convert binary to decimal
    return int(str(res),2)


# Enter the data to be transmitted
data = input('Enter data: ')

# Calculate the no of Redundant Bits Required
m = len(data)
r = calcRedundantBits(m)

# Determine the positions of Redundant Bits
ar = posRedundantBits(data,r)

# Determine the parity bits
arr = calcParityBits(ar,r)

print("Redundant bits and values:")
for i in pos:
    print("R",i,"=",end = '')
    print(arr[i * -1])

# Data to be transferred
print("Data transferred is " + arr)
arr = list(arr)
a = random.randint(0,len(arr))

if arr[a] == 0:
    arr[a] = 1
else:
    arr[a] = 0

print("Error Data is ",*arr)
correction = detectError(arr,r)
print("The position of error is " + str(correction))
print("Program by Amit Kumar -- 4NI18IS009")
