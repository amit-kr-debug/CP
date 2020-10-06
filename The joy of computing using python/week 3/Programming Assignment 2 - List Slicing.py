"""
You have seen in videos how list slicing is performed in python. If not please refer to this link List Slicing.


In this program, create a list of numbers from 1 to 50 named list_1. The numbers should be present in the increasing order: Ex list_1 = [1,2,3,4,5,....,50]

i.e. index zero should be 1, index one should be 2, index two should be 3 and so on.


Given an input of two numbers, let's say a and b, you have to print the numbers returned by the following command

list_1[a:b]


Input:

The first line of input contains two numbers a and b separated by a space.


NOTE: You can take two inputs in a single line using the following command:

a, b = input().split()


Make sure you convert the strings in a and b into integers using the int() command


Output:

Print the numbers in new line


Example :


Input:
2 6

Output:

3

4

5

6


Explanation: In this example, a is 2 and b is 6. The list_1 contains numbers from 1 to 50. When you perform the operation list_1[a:b] which in this case is, list_1[2:6], it returns a list of following numbers [3, 4, 5, 6]. Print the elements of this list with each element in a new line.
"""

list_1 = [x for x in range(1, 51)]
a, b = map(int, input().split())
list_1 = list_1[a:b]
for i in list_1[:len(list_1)-1]:
    print(i)
print(list_1[len(list_1)-1], end="")