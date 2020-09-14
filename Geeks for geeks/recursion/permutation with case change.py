"""
Permute a string by changing case
Last Updated: 17-10-2019
Print all permutations of a string keeping the sequence but changing cases.

Examples:

Input : ab
Output : AB Ab ab aB

Input : ABC
Output : abc Abc aBc ABc abC AbC aBC ABC
"""


def caseChange(op, index):
    if index == len(arr):
        ans.append(op)
        return
    op1 = op + arr[index].upper()
    op2 = op + arr[index]
    index += 1
    caseChange(op2, index)
    caseChange(op1, index)


s = input()
s.lower()
arr = []
ans = []
arr[:0] = s
caseChange("", 0)
# print(ans)
for i in ans:
    print(i, end=" ")
print()