def decrypt_text(cipher_text,inv_matrix):
    count = 0
    plain_text = ""
    # Appending lower case into matrix
    len_text = len(cipher_text)
    while count < len_text:
        a = []
        for i in range(int(pow(key_len, 1/2))):
            # Appending lower case into matrix
            if 97 <= ord(cipher_text[count]) <= 122 :
                a.append(ord(cipher_text[count]) - 97)
             # Appending upper case into matrix
            elif 65 <= ord(cipher_text[count]) <= 90:
                a.append(ord(cipher_text[count]) - 65)
            count += 1
        for i in range(int(pow(key_len, 1/2))):
            temp = 0
            #Decrypting the cipher text
            for j in range(int(pow(key_len, 1/2))):
                temp += (inv_matrix[i][j] * a[j])
            temp = temp % 26
            plain_text += chr(temp + 65)
    return plain_text

def transposeMatrix(m):
    return list(map(list,zip(*m)))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = (cofactors[r][c]/determinant) % 26
    return cofactors


if __name__ == '__main__':
    #Taking key as input
    key = input("Enter the key:")
    key_matrix = []
    key_len = len(key)
    count = 0
    for i in range(int(pow(key_len, 1/2))):
        a = []
        for j in range(int(pow(key_len, 1/2))):
            # Appending lower case into matrix
            if 97 <= ord(key[count]) <= 122 :
                a.append(ord(key[count]) - 97)
            elif 65 <= ord(key[count]) <= 90:
            #Appending Upper case into matrix
                a.append(ord(key[count]) - 65)
            count += 1
        key_matrix.append(a)
    print("key_matrix:")
    print(key_matrix)
    inv_matrix = getMatrixInverse(key_matrix)
    inv_matrix = [[8,5,10],[21,8,21],[21,12,8]]
    print("Inverse key matrix:")
    print(inv_matrix)
    # Taking cipher text as input
    cipher_text = input("Enter the cipher text:")
    print(decrypt_text(cipher_text, inv_matrix))