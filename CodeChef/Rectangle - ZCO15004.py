"""
We have a rectangular region that is 100000 units along the X-axis and 500 units along the Y-axis.

We assume that the origin (0,0) is at the bottom-left corner of this region, so that the top-left corner is at (0,500), the bottom-right at (100000,0) and the top-right corner at (100000,500). We are also given the coordinates of a set of N points inside this region. The points have only integer coordinates and do not appear along the X-axis or Y-axis.

We would like to draw a rectangle, with its base on the X-axis, of maximum area within the region such that it does not contain any of the N points in its interior. More specifically, the points may appear on the boundary but cannot be properly inside the rectangle.

For example, if there are 5 points : (1,4),(2,3),(3,2),(5,1) and (5,2). Then the rectangle whose bottom-left and top-right corners are given by (0,0) and (2,3) is a possibility and its area is 6. Another possibility is the rectangle with bottom-left and top-right corners at (3,0) and (5,500) with area 1000. The rectangle with bottom-left at (2,3) and top-right at (100000,500) is not valid since its base does not lie on the X-axis. The largest rectangle that meets the requirements in this case is the one with its bottom-left corner at (5,0) and top-right at (100000,500) with area 49997500.

Your program should take a description of the N points and output the size of the maximum rectangle satisfying the above property that can be drawn within the 100000×500 region.

Input format
The first line contains a single integer N, giving the number of points marked in the region.

This is followed by N lines, each containing two integers separated by a space describing the coordinates of one point.

Output format
Output a single integer giving the area of the largest rectangle that may be drawn with its base on the X-axis and which does not contain any of the given N points in its interior.

Test data
In both subtasks, the X-coordinate of each of the N points is in the range 1 to 99999 inclusive, and the Y-coordinate of each of the N points is in the range 1 to 499 inclusive.

Subtask 1 (40 marks) :1≤N≤5000
Subtask 2 (60 marks) :1≤N≤100000
Sample Input
5
1 4
2 3
3 2
5 1
5 2
Sample Output
49997500
"""

n = int(input())
pos = {}
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    pos.update({x: y})
X.append(100000)
pos.update({100000: 500})
X.sort()
Y.sort()
diff = -1
index = -1
for i in range(n):
    tempDiff = X[i+1] - X[i]
    # print(tempDiff)
    if tempDiff > diff:
        diff = tempDiff
        index = X[i]
print(max(diff*500, Y[0]*100000))