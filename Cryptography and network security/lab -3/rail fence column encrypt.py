def encrypt(matrix, key):
    cipher_text = ""
    for i in range(key):
        for j in range(len(matrix)):
            if matrix[j][i] != -1:
                cipher_text += matrix[j][i]
    return cipher_text


if __name__ == "__main__":
    plain_text2 = list(input("Enter the plain text:"))

    key = int(input("Enter the Key:"))
    matrix = []
    len_text = len(plain_text2)
    count1 = 0
    count2 = key
    print(plain_text2)
    while len_text - count2 >= 0:
        temp = plain_text2[count1:count2]
        count1 = count2
        count2 += key
        matrix.append(temp)
    if len_text - count2 < 0:
        temp = plain_text2[count1:len_text]
        for i in range(len_text, count2):
            temp.append(-1)
        matrix.append(temp)

    print(matrix)
    print(encrypt(matrix, key))