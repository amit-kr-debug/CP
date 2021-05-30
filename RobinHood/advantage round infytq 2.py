def getNum(num, i, digit):
    num = num[:i]+str(digit)+num[i+1:]
    return num


def findMax(num: str, arr: list):
    pos_ans = []
    flag = False
    for i in range(len(num)):
        # print(pos_ans)
        if flag:
            temp = pos_ans[-1]
            temp = getNum(temp, i, arr[int(num[i])-1])
            if int(temp) > int(pos_ans[-1]):
                flag = True
                pos_ans.pop()
                pos_ans.append(temp)
            else:
                flag = False

        else:
            temp = num
            temp = getNum(temp, i, arr[int(num[i])-1])
            if int(temp) > int(num):
                flag = True
                pos_ans.append(temp)
            else:
                flag = False
    if len(pos_ans) > 0:
        return max(pos_ans)
    else:
        return -1


print(findMax("72312347", [9,1,5,2,3,2,8,3]))
