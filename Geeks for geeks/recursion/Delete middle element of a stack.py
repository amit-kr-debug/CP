"""
Given a stack with push(), pop(), empty() operations, delete the middle of it without using any additional data
structure.
Middle: ceil(size_of_stack/2.0)


Example 1:

Input:
5
1 2 3 4 5

Output:
1 2 4 5

Explanation:
As the number of elements is 5 ,
hence the middle element will be the 3rd
element which is deleted
Example 2:

Input:
4
1 2 3 4

Output:
1 3 4

Explanation:
As the number of elements is 4 ,
hence the middle element will be the 2nd
​element which is deleted


Your Task:
This is a function problem. The input is already taken by the driver code. You only need to complete the function
deleteMid() which takes 3 arguments(stack, size of the stack, and current index - initially 0) and returns the modified
stack.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= sizeOfStack <= 100

Note: The output on the console is printed in reverse order of elements in the modified stack.
"""

# User function Template for python3
import math


##Complete this function
def delmid(s, midEl):
    if midEl == 1:
        s.pop()
        return
    temp = s.pop()
    delmid(s, midEl - 1)
    s.append(temp)


def deleteMid(s, sizeOfStack, current):
    ##Your code here
    delmid(s, math.floor(sizeOfStack / 2) + 1)
    return s


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    testcases = int(input())
    while (testcases > 0):

        sizeOfStack = int(input())

        myStack = [int(x) for x in input().strip().split()]

        if (sizeOfStack == 1):
            print(myStack[0])
        else:
            modified = deleteMid(myStack, sizeOfStack, 0)

            while (len(modified) > 0):
                print(modified[-1], end=" ")
                modified.pop()
            print()

        testcases -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends