"""
Given a linked list of N nodes. The task is to reverse this list.

Example 1:

Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list,
elements are 6->5->4->3->2->1.
Example 2:

Input:
LinkedList: 2->7->8->9->10
Output: 10 9 8 7 2
Explanation: After reversing the list,
elements are 10->9->8->7->2.
Your Task:
The task is to complete the function reverseList() with head reference as the only argument and should return new head
after reversing the list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 104
"""

# function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""


class Solution:
    # Function to reverse a linked list.
    def reverseList(self,head):
        # Code here
        prev = None
        current = head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head


# {
#  Driver Code Starts
# Node Class
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data,end = ' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().reverseList(lis.head)
        printList(newHead)

# } Driver Code Ends