"""
Reverse a Stack without using recursion and extra space. Even the functional Stack is not allowed.

Examples:

Input : 1->2->3->4
Output : 4->3->2->1

Input :  6->5->4
Output : 4->5->6
"""


def insert(arr, ele):
    if len(arr) == 0:
        arr.append(ele)
        return
    temp = arr.pop()
    insert(arr, ele)
    arr.append(temp)


def reverse(arr):
    if len(arr) == 1:
        return
    temp = arr.pop()
    reverse(arr)
    insert(arr, temp)


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 89, 56, 2, 90, 100]
reverse(arr1)
reverse(arr2)
print(arr1)
print(arr2)
