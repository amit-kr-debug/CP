"""
Given a binary tree, find its height.

​​Example 1:

Input:
      1
    /  \
   2    3
Output: 2
Example 2:

Input:
  2
   \
    1
   /
 3
Output: 3
Your Task:
You don't need to read input or print anything. Your task is to complete the function height() that takes root Node of
the Tree as input and returns the Height of the Tree. If the Tree is empty, return 0.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105
"""

"""
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""


# return the Height of the given Binary Tree
def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return 1 + max(left, right)



