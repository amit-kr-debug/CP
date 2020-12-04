"""
    1
   2 1 2
  3 2 1 2 3
 4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
"""

rows = 5
for i in range(rows):
    # for printing spaces that will be 1 less than rows - ith
    for j in range(rows-i-1):
        print(" ", end="")
    # for printing the palindromic sequence
    for j in range(2*i+1):
        # printing the first half up to 1 in reverse order, the number will be i-j+1
        if j <= i:
            print(i-j+1, end=" ")
        # printing rest in ascending order after 1.
        else:
            print(j-i+1, end=" ")
    print()
