"""
level 3 foobar
"""


def find_max_sum(arr) :
    incl = 0
    excl = 0

    for i in arr :
        # Current max excluding i (No ternary in
        # Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

        # return max of incl and excl
    return (excl if excl > incl else incl)


arr = list(map(int, input().split()))
print(find_max_sum(arr))