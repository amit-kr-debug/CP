s = input()
t = input()
s1 = 1
t1 = 1
for i in range(len(s)):
    s1 *= (ord(s[i])-64)
for i in range(len(t)):
    t1 *= (ord(t[i])-64)

if t1%47 == s1%47:
    print("CHOSEN")
else:
    print("NOT CHOSEN")