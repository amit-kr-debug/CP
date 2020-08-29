"""
Chef is on an adventure to find the tastiest exotic spices. Everyone knows that the best spices are guarded by several
ancient dragons that dwell within mountains.

The mountain range can be modeled by a polyline in the 2D xz plane that passes through N points p1=(1,h1),p2=(2,h2),…,
pN=(N,hN), in this order, where hi is a positive integer for each valid i. This polyline divides the set of points
{(x,z):1≤x≤N} into two regions. The "solid" part of the mountain range is the "bottom" region, i.e. the region that
contains the x-axis (the x-axis is the line z=0).

A dragon's den is located at each of the N points. For each valid i, the den at the point pi initially contains a pile
of spices with tastiness ai. With a technique he learned from dragons, Chef can glide from den to den, tasting all of
the spices along the way. The tastiness of an entire journey is the summed up tastiness of spices over all dens visited
during the journey. However, there are some restrictions:

Chef can only glide from a higher den to a strictly lower den, i.e. if he glides from a den at pi to a den at pj, then
hi>hj must hold.
Chef can only glide in one direction and never look back, i.e. if he starts travelling in the direction of decreasing x,
 he must keep travelling in that direction until the end of the journey, and if he starts travelling in the direction of
  increasing x, he must keep travelling in that direction until the end of the journey too.
Chef cannot travel through solid mountain, i.e. he can only glide from a den at pi to a den at pj if the line segment
connecting the points pi and pj does not intersect the "solid" part of the mountain range. However, it may touch the
border of the mountain range, i.e. the polyline itself.
Note that gliding is the only way for Chef to travel between dens. It is valid for a journey to begin and end at the
same den, in which case Chef tastes the spices at the den and nothing else.

See the explanation of the sample test case for a concrete example.

With that in mind, Chef needs you to process Q queries. There are two types of queries:

1 b k: Chef changes his mind and decides that the tastiness of the spices in the den at the point pb should be changed
to k instead.
2 b c: Chef wants to start a journey at the den located at pb and end it at the den located at pc. Find the maximum
possible tastiness of such a journey or determine that no such journey exists.
Input
The first line of the input contains two space-separated integers N and Q.
The second line contains N space-separated integers h1,h2,…,hN.
The third line contains N space-separated integers a1,a2,…,aN.
Then, Q lines follow. Each of these lines contains three space-separated integers describing a query in the above
format.
Output
For each query of the second type, print a single line containing one integer ― the maximum tastiness of a journey or
−1 if no valid journey exists.

Constraints
1≤N,Q≤2⋅105
1≤hi≤109 for each valid i
1≤ai≤109 for each valid i
1≤b,c≤N
1≤k≤109
Subtasks
Subtask 1 (10 points): N,Q≤1,000
Subtask 2 (35 points): there are no queries of the first type

Subtask 3 (55 points): original constraints

Example Input
5 4
3 1 4 1 5
1 2 4 8 16
2 5 2
1 3 5
2 3 4
2 1 4
Example Output
22
13
-1
Explanation
Here is an illustration of the mountain range described in the first sample test case.

Query 1: Starting at p5 (height 5), Chef can glide to p3 (height 4) and then to p2 (height 1). The total tastiness of
this journey is a5+a3+a2=16+4+2=22.


Query 2: The value of a3 is set to 5.
Query 3: Chef glides from p3 to p4. The tastiness is a3+a4=5+8=13.
Query 4: It is impossible to get from p1 to p4. Even if h1>h4, to reach p4, Chef would need to fly either upwards or
through the mountain, both of which are impossible.

"""

"""
dens, query = map(int, input().split())
p = list(map(int, input().split()))
taste = list(map(int, input().split()))
for _ in range(query):
    q = list(map(int, input().split()))
    if q[0] == 1:
        taste[q[1]-1] = q[2]
    else:
        if p[q[1]-1] >= p[q[2]-1]:
            if q[1] < q[2]: #a is smaller index
                a = q[1]-1
                b = q[2]-1
            else:
                a = q[2]-1
                b = q[1]-1
            if p[a] < p[b]: #a1 contains index having is smaller peak
                a1 = a
                b1 = b
            else:
                a1 = b
                b1 = a
            if p[a] != p[b]:
                peak = p[b1]
                highPeak = 0
                if (b-a) > 1:
                    highPeak = max(p[a+1:b])
                # print(peak, highPeak)
                if peak > highPeak:
                    tempList = [a1]
                    if a1 == a:
                        for i in range(b-a):
                            temp = tempList.pop()
                            if p[a1+i+1] > p[temp]:
                                tempList.append(temp)
                                tempList.append(a1+i+1)
                            else:
                                tempList.append(temp)
                    else:
                        for i in range(b - a):
                            temp = tempList.pop()
                            if p[a1 - i - 1] > p[temp]:
                                tempList.append(temp)
                                tempList.append(a1 - i - 1)
                            else:
                                tempList.append(temp)
                    # print(tempList)
                    tt = 0
                    for i in tempList:
                        tt += taste[i]
                    print(tt)
                else:
                    print(-1)
            elif a == b:
                print(taste[a])
            else:
                print(-1)
        else:
            print(-1)
"""

from sys import maxsize

INT_MIN = -maxsize


def findTaste(start, end):
    q = [0, start+1, end+1]
    # print(start, end)
    if p[q[1] - 1] <= p[q[2] - 1]:
        if q[1] < q[2]:  # a is smaller index
            a = q[1] - 1
            b = q[2] - 1
        else:
            a = q[2] - 1
            b = q[1] - 1
        if p[a] < p[b]:  # a1 contains index having is smaller peak
            a1 = a
            b1 = b
        else:
            a1 = b
            b1 = a
        if p[a] != p[b]:
            peak = p[b1]
            highPeak = 0
            if (b - a) > 1:
                highPeak = max(p[a + 1:b])
            # print(peak, highPeak)
            if peak > highPeak:
                tempList = [a1]
                if a1 == a:
                    for i in range(b - a):
                        temp = tempList.pop()
                        if p[a1 + i + 1] > p[temp]:
                            tempList.append(temp)
                            tempList.append(a1 + i + 1)
                        else:
                            tempList.append(temp)
                else:
                    for i in range(b - a):
                        temp = tempList.pop()
                        if p[a1 - i - 1] > p[temp]:
                            tempList.append(temp)
                            tempList.append(a1 - i - 1)
                        else:
                            tempList.append(temp)
                tt = 0
                for i in tempList:
                    tt += taste[i]
                return tt
            else:
                return -1
        elif a == b:
            return taste[a]
        else:
            return -1
    else:
        return -1


def find_sum(i, sl, sr, l, r):
    if l <= sl and r >= sr:
        if sl == l:
            print(i, sl, sr, segTree[i])
            return segTree[i]
        elif p[sl] >= p[l]:
            print(sl, sr, segTree[i])
            return segTree[i]
        elif sl == sr:
            return 0
        else:
            print("a", l, r)
            return find_sum(2*i, sl, (sr+sl)//2, nextBigIndex[l], r)+find_sum(2*i+1, (sr+sl)//2+1, sr, nextBigIndex[l], r)
    elif sr < l or sl > r:
        return 0
    print("b", l, r)
    return find_sum(2 * i, sl, (sr + sl) // 2, l, r) + find_sum(2 * i + 1, (sr + sl) // 2 + 1, sr, l, r)


def segment_tree(i, start, end):
    global segTree
    if start == end:
        return
    segTree[i*2] = findTaste(start, (start+end)//2)
    # print(segTree[i*2], i*2)
    segTree[i*2+1] = findTaste((start+end)//2+1, end)
    # print(segTree[i * 2+1], i*2+1)
    segment_tree(i*2, start, (start+end)//2)
    segment_tree(i*2+1, (start+end)//2+1, end)


def construct_segment_tree(a: list, n: int):
    global segtree
    for i in range(n):
        segtree[n + i] = a[i]
    for i in range(n - 1, 0, -1):
        segtree[i] = max(segtree[2 * i], segtree[2 * i + 1])


def range_query(left: int, right: int, n: int) -> int:
    global segtree
    ma = INT_MIN
    left += n
    right += n


    while left < right:
        if left & 1:
            ma = max(ma, segtree[left])
            left += 1
        if right & 1:
            right -= 1
            ma = max(ma, segtree[right])
        left //= 2
        right //= 2
    return ma


def find_max_index(m: int, start: int, end: int):
    low = 0
    arr = iDict[m]
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2
        if arr[mid] < start:
            low = mid + 1
        elif arr[mid] > end:
            high = mid - 1
        else:
            high = mid
            possibleIndex = -1
            while low <= high:
                # print('c')
                mid = (low + high) // 2
                if arr[mid] == start:
                    # print('b')
                    return arr[mid]

                elif arr[mid] > start:
                    # print('c')
                    possibleIndex = arr[mid]
                    high = mid - 1

                else:
                    low = mid + 1
            return possibleIndex
    return -1


dens, query = map(int, input().split())
p = list(map(int, input().split()))
taste = list(map(int, input().split()))
iDict = {}
nextBigIndex = [-1]*dens
count = 0
for i in p:
    if i in iDict:
        iDict[i].append(count)
    else:
        iDict.update({i: [count]})
    count += 1
# print(iDict)
temp = [0]
index = 0
for i in range(1, dens):
    if p[i] <= p[temp[index]]:
        temp.append(i)
        index += 1
    else:
        while index >= 0 and p[i] > p[temp[index]]:
            nextBigIndex[temp[index]] = i
            temp.pop()
            index -= 1
        temp.append(i)
        index += 1

segtree = [0]*(3*dens)
construct_segment_tree(p, dens)
segTree = [0] * (3 * dens)
segTree[1] = findTaste(0, dens-1)
segment_tree(1, 0, dens-1)
# print(segTree)
print(find_sum(1, 0, 4, 1, 4))
for _ in range(query):
    q1 = list(map(int, input().split()))
    if q1[0] == 1:
        taste[q1[1]-1] = q1[2]
    else:
        if p[q1[1]-1] > p[q1[2]-1]:
            a = q1[1]-1
            b = q1[2]-1
            if a > b:
                ma = range_query(a+1, b, dens)
                if ma > p[a]:
                    print(-1)
                else:
                    print(find_sum(1, 0, dens-1, b, a))
        elif q1[1]-1 == q1[2]-1:
            print(taste[q1[1]-1])
        else:
            print(-1)




"""
# def create_taste(start, end, dens1):
#     if start == end:
#         t[start] += taste[start]
#         return
#     m = range_query(start, end, dens1)
#     iList = iDict[m]
#     index = 0
#     for k in iList:
#         if start <= k <= end:
#             index = k
#             break
#     for k in range(start, index+1):
#         t[k] += taste[index]
#     if index == start:
#         create_taste(index + 1, end, dens1)
#     elif index == end:
#         create_taste(start, index - 1, dens1)
#     else:
#         create_taste(start, index-1, dens1)
#         create_taste(index+1, end, dens1)
"""

