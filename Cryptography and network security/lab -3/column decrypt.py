import math
def decrypt(matrix,key):
    plain_text = ""
    for i in range(len(matrix)):
        for j in range(key):
            if matrix[i][j] != -1:
                plain_text += matrix[i][j]
    return plain_text


if __name__ == "__main__":
    cipher_text = list(input("Enter the cipher text:"))
    key = int(input("Enter key value:"))
    k = 0
    len_cip = len(cipher_text)
    count = len_cip % key
    matrix = [[-1 for i in range(key)]for j in range(math.ceil(len_cip/key))]
    if count > 0:
        for i in range(count):
            for j in range(len(matrix)):
                matrix[j][i] = cipher_text[k]
                k += 1
        for i in range(count,key):
            for j in range(len(matrix)-1):
                matrix[j][i] = cipher_text[k]
                k += 1
    else:
        for i in range(count,key):
            for j in range(len(matrix)):
                matrix[j][i] = cipher_text[k]
                k += 1
    print(matrix)
    print(decrypt(matrix,key))