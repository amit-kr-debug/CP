"""
Given a singly linked list of N nodes. The task is to find the middle of the linked list. For example, if given linked
list is 1->2->3->4->5 then the output should be 3.
If there are even nodes, then there would be two middle nodes, we need to print the second middle element. For example,
if given linked list is 1->2->3->4->5->6 then the output should be 4.

Example 1:

Input:
LinkedList: 1->2->3->4->5
Output: 3
Explanation:
Middle of linked list is 3.
Example 2:

Input:
LinkedList: 2->4->6->7->5->1
Output: 7
Explanation:
Middle of linked list is 7.
Your Task:
The task is to complete the function getMiddle() which takes a head reference as the only argument and should return the
data at the middle node of the linked list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 5000
"""

# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''


# function should return index to the any valid peak element
def findMid(head):
    # Code here
    # return the value stored in the middle node
    slow = head
    fast = head
    while fast is not None:
        fast = fast.next
        if fast is not None:
            fast = fast.next
            slow = slow.next
    return slow.data


# {
#  Driver Code Starts
# Node Class
class node:
    def __init__(self,val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = self.tail.next


def createList(arr,n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        head = createList(arr,n)
        print(findMid(head))

# } Driver Code Ends