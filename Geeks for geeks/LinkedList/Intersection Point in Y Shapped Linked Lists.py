"""
Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.



Example 1:

Input:
LinkList1 = 3->6->9->common
LinkList2 = 10->common
common = 15->30->NULL
Output: 15
Explanation:
Y ShapedLinked List
Example 2:

Input:
Linked List 1 = 4->1->common
Linked List 2 = 5->6->1->common
common = 8->4->5->NULL
Output: 8
Explanation:

4              5
|              |
1              6
 \             /
  8   -----  1
   |
   4
   |
  5
  |
  NULL
Your Task:
You don't need to read input or print anything. The task is to complete the function intersetPoint() which takes the pointer to the head of linklist1(head1) and linklist2(head2) as input parameters and returns data value of a node where two linked lists intersect. If linked list do not merge at any point, then it should return -1.
Challenge : Try to solve the problem without using any extra space.



Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)



Constraints:
1 ≤ N + M ≤ 2*105
-1000 ≤ value ≤ 1000
"""

# User function Template for python3
'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.

	Function Arguments: head_a, head_b (heads of both the lists)

	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''


# Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    # code here
    cpy1 = head1
    cpy2 = head2
    while head1 != head2:
        if head1:
            head1 = head1.next
        else:
            head1 = cpy2
        if head2:
            head2 = head2.next
        else:
            head2 = cpy1
    return head1.data


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:
    def __init__(self,data):  # data -> value stored in node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        temp = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self,new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        x,y,z = map(int,input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int,input().strip().split()))
        nodes_b = list(map(int,input().strip().split()))
        nodes_common = list(map(int,input().strip().split()))

        for x in nodes_a:
            node = Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node = Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node = Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i == 0:
                b.append(node)  # add to the end of the list b, only the intersection

        print(intersetPoint(a.head,b.head))

# } Driver Code Ends