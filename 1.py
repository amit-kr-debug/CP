"""
1. Treasure hunt
Harry is participating in a treasure hunt contest. The treasure is hidden in a house marked with zero, amidst a row of
houses each marked with different numbers (numbers can repeat but are all positive). Harry is given the house from where
he is supposed to start the hunt. However he is told he can move from one house to another only to the extent of the
number of the house i.e. if the current house is marked 4, then he can move to the fourth house either to the left or
to the right of the current house. If there are less than 4 houses in one direction, then he can only move in the other
direction. Moving in this way, he has to reach the treasure.



Write a program to help Harry determine if he can reach the treasure or not.



Read the input from STDIN and print the output to STDOUT. Do not write arbitrary strings anywhere in the program, as
these contribute to the standard output and testcases will fail.



Constraints:

1 <= the number of treasure hunts < 10

1 <= the number of houses <= 100



Input format:

The first line contains the number of treasure hunts t.

The next 3t lines contain details of each treasure hunt.

For each treasure hunt, the first line has the number of houses, the second line has the house number markings in
sequence, and the last line has the house from which Harry has to start the hunt.



Output format:

Print the result of each treasure hunt in a new line. Print 'Yes' if Harry can reach the treasure, and 'No' if he
cannot.



Sample input1:

2

7

2 1 0 1 2 1 6

6

5

4 2 0 2 3

4



Sample Output1:

Yes

No



Explanation:

First number in input is 2 which determines the number of treasure hunts, followed by details of the two treasure hunts.



Treasure hunt 1:

Harry starts from the sixth house, which is marked with 1. He can move one house in either direction. He moves to the
fifth house, which is marked 2. Next he moves 2 houses to the third house, which is the house marked with 0. Hence
print 'Yes'.



Treasure Hunt 2:

Harry starts from the fourth house, which is marked with 2. He cannot move to the right as there is only one house in
that direction. So he moves 2 houses to the left, to another house also marked with 2. Now he cannot move 2 houses
further to the left as there is only one house in that direction. So he moves 2 houses to the right, reaching his
starting point. He is thus stuck in a cycle and will never reach the treasure. Hence print 'No'.



Sample Input2:

3

5

1 2 0 4 5

3

4

11 12 0 14

2

6

10 20 30 40 0 50

4



Sample Output2:

Yes

No

No
"""


def possiblerotation(n, arr, s) :  # n is the number of houses, arr contains the house number markings,
    # s is the house number from which Harry starts the hunt.

    # WRITE YOUR CODE HERE

    # return 1 if hunt is possible and 0 if not possible

    return -1


def printPossiblerotation(n, arr, s) :
    if (possiblerotation(n, arr, s) == 1) :
        print("Yes")
    elif (possiblerotation(n, arr, s) == 0) :
        print("No")


def main() :
    nTest = int(input())  # nTest is the number of treasure hunts.
    for i in range(nTest) :
        len = int(input())
        arr = list(map(int, input().split()))
        s = int(input())
        printPossiblerotation(len, arr, s)


main()