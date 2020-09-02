"""
Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B.
It may be assumed that there is no common character between A and B
"""

A = input()
B = input()
C = input()
lenC = len(C)
lenA = len(A)
lenB = len(B)
if lenA + lenB != lenC:
    print(0)
else:
    i = 0
    j = 0
    for k in range(lenC):
        if i < lenA and A[i] == C[k]:
            i += 1
        elif j < lenB and B[j] == C[k]:
            j += 1
        else:
            print(0)
            break
    print(1)