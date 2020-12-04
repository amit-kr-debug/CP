"""
Given a array of N strings, find the longest common prefix among all strings present in the array.

Input:
The first line of the input contains an integer T which denotes the number of test cases to follow. Each test case contains an integer N. Next line has space separated N strings.

Output:
Print the longest common prefix as a string in the given array. If no such prefix exists print "-1"(without quotes).

Constraints:
1 <= T <= 103
1 <= N <= 103
1 <= |S| <= 103

Example:
Input:
2
4
geeksforgeeks geeks geek geezer
3
apple ape april

Output:
gee
ap

Explanation:
Testcase 1: Longest common prefix in all the given string is gee.
"""


# code
def match(str1,str2):
    index = 0
    aux = ""
    while index < len(str1) and index < len(str2):
        if str1[index] == str2[index]:
            aux += str1[index]
            index += 1
        else:
            break

    return aux


for _ in range(int(input())):
    n = int(input())
    arr = list(map(str,input().split()))
    if n == 1:
        print(arr[0])

    else:
        flag = 1
        ans = match(arr[0],arr[1])
        for i in range(2,n):
            ans = match(ans,arr[i])
            if ans == "":
                flag = 0
                break
        if flag:
            print(ans)
        else:
            print(-1)

