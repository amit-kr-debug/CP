def encrypt_text(plain_text,key_matrix):
    count = 0
    cipher_text = ""
    len_text = len(plain_text)
    while count < len_text:
        a = []
        for i in range(int(pow(key_len, 1/2))):
            # Appending lower case into matrix
            if 97 <= ord(plain_text[count]) <= 122 :
                a.append(ord(plain_text[count]) - 97)
            #Appending Upper case into matrix
            elif 65 <= ord(plain_text[count]) <= 90:
                a.append(ord(plain_text[count]) - 65)
            count += 1
        for i in range(int(pow(key_len, 1/2))):
            temp = 0
            #Encrypting the plain text
            for j in range(int(pow(key_len, 1/2))):
                temp += (key_matrix[i][j] * a[j])
            temp = temp % 26
            cipher_text += chr(temp + 65)
    return cipher_text


if __name__ == '__main__':
    #Taking key as input
    key = input("Enter the key:")
    key_matrix = []
    key_len = len(key)
    count = 0
    # Converting key into matrix
    for i in range(int(pow(key_len, 1/2))):
        a = []
        for j in range(int(pow(key_len, 1/2))):
            if 97 <= ord(key[count]) <= 122 :
                a.append(ord(key[count]) - 97)
            elif 65 <= ord(key[count]) <= 90:
                a.append(ord(key[count]) - 65)
            count += 1
        key_matrix.append(a)
    print(key_matrix)
    # Taking plain text as input
    plain_text = input("Enter the plain text:")
    print(encrypt_text(plain_text, key_matrix))