"""
sample input : a1b2
sample output : a1b2 a1B2 A1b2 A1B2
"""


def caseChange(op, index):
    if index == len(arr):
        ans.append(op)
        return

    while index < len(arr) and arr[index].isnumeric():
        op += arr[index]
        index += 1
        if index == len(arr):
            ans.append(op)
            return
    op1 = op
    op2 = op
    if index < len(arr):
        op1 += arr[index].upper()
        op2 += arr[index]
        index += 1
        caseChange(op2, index)
        caseChange(op1, index)


s = input()
s.lower()
ans = []
arr = []
arr[:0] = s
caseChange("", 0)
for i in ans:
    print(i, end=" ")
print()