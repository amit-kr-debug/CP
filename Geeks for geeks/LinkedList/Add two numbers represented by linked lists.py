"""
Add two numbers represented by linked lists
Easy Accuracy: 30.12% Submissions: 91880 Points: 2
Given two numbers represented by two linked lists of size N and M. The task is to return a sum list.
The sum list is a linked list representation of the addition of two input numbers from the last.

Example 1:

Input:
N = 2
valueN[] = {4,5}
M = 3
valueM[] = {3,4,5}
Output: 3 9 0
Explanation: For the given two linked
list (4 5) and (3 4 5), after adding
the two linked list resultant linked
list will be (3 9 0).
Example 2:

Input:
N = 2
valueN[] = {6,3}
M = 1
valueM[] = {7}
Output: 7 0
Explanation: For the given two linked
list (6 3) and (7), after adding the
two linked list resultant linked list
will be (7 0).
Your Task:
The task is to complete the function addTwoLists() which has node reference of both the linked lists and returns the
head of the new list.

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(Max(N,M))

Constraints:
1 <= N, M <= 5000
"""

# User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    # Function to add two numbers represented by linked list.
    def addTwoLists(self,first,second):
        # code here
        # return head of sum list
        c = 0
        res = LinkedList()
        num1 = ""
        num2 = ""
        while first:
            num1 += str(first.data)
            first = first.next
        while second:
            num2 += str(second.data)
            second = second.next
        sum_nums = str(int(num1) + int(num2))

        for num in sum_nums:
            res.insert(int(num))
        return res.head


# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end = ' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        n = int(input())
        arr1 = (int(x) for x in input().split())
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)

        m = int(input())
        arr2 = (int(x) for x in input().split())
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)

        res = Solution().addTwoLists(LL1.head,LL2.head)
        printList(res)
# } Driver Code Ends