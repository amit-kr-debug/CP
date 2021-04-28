"""
b) Playfair Cipher The Playfair cipher was the first practical digraph substitution cipher. The scheme was invented in 1854 by Charles Wheatstone but was named after Lord Playfair who promoted the use of the cipher. In playfair cipher unlike traditional cipher we encrypt a pair of alphabets(digraphs) instead of a single alphabet. It was used for tactical purposes by British forces in the Second Boer War and in World War I and for the same purpose by the Australians during World War II. This was because Playfair is reasonably fast to use and requires no special equipment. Encryption Technique For the encryption process let us consider the following example: The Playfair Cipher Encryption Algorithm: The Algorithm consists of 2 steps: 1. Generate the key Square(5×5): • The key square is a 5×5 grid of alphabets that acts as the key for encrypting the plaintext. Each of the 25 alphabets must be unique and one letter of the alphabet (usually J) is omitted from the table (as the table can hold only 25 alphabets). If the plaintext contains J, then it is replaced by I. • The initial alphabets in the key square are the unique alphabets of the key in the order in which they appear followed by the remaining letters of the alphabet in order.
For example: The key is "monarchy" Thus the initial entires are 'm', 'o', 'n', 'a', 'r', 'c', 'h', 'y' followed by remaining characters of a-z(except 'j') in that order. 2. Algorithm to encrypt the plain text: The plaintext is split into pairs of two letters (digraphs). If there is an odd number of letters, a Z is added to the last letter. For example: PlainText: "instruments" After Split: 'in' 'st' 'ru' 'me' 'nt' 'sz' Rules for Encryption: • If both the letters are in the same column: Take the letter below each one (going back to the top if at the bottom). For example: Diagraph: "me" Encrypted Text: cl Encryption: m -> c e -> l • If both the letters are in the same row: Take the letter to the right of each one (going back to the leftmost if at the rightmost position). For example: Diagraph: "st" Encrypted Text: tl Encryption: s -> t t -> l
• If neither of the above rules is true: Form a rectangle with the two letters and take the letters on the horizontal opposite corner of the rectangle. For example: Diagraph: "nt" Encrypted Text: rq Encryption: n -> r t -> q For example:
Plain Text: "instrumentsz"
Encrypted Text: gatlmzclrqtx
Encryption:
i -> g
n -> a
s -> t
t -> l
r -> m
u -> z
m -> c
e -> l
n -> r
t -> q
s -> t
z -> x
Output:
Key text: Monarchy
Plain text: instruments
Cipher text: gatlmzclrqtx Decryption Technique Decrypting the Playfair cipher is as simple as doing the same process in reverse. The receiver has the same key and can create the same key table, and then decrypt any messages made using that key. The Playfair Cipher Decryption Algorithm: The Algorithm consistes of 2 steps: 1. Generate the key Square(5×5) at the receiver’s end: • The key square is a 5×5 grid of alphabets that acts as the key for encrypting the plaintext. Each of the 25 alphabets must be unique and one letter of the alphabet (usually J) is omitted from the table (as the table can hold only 25 alphabets). If the plaintext contains J, then it is replaced by I. • The initial alphabets in the key square are the unique alphabets of the key in the order in which they appear followed by the remaining letters of the alphabet in order. Note: For both encryption and decryption, the same key is to be used. For example: The key is "monarchy" Thus the initial entires are 'm', 'o', 'n', 'a', 'r', 'c', 'h', 'y' followed by remaining characters of a-z(except 'j') in that order. 2. Algorithm to decrypt the ciphertext: The ciphertext is split into pairs of two letters (digraphs). Note: The ciphertext always have even number of characters. For example: CipherText: "gatlmzclrqtx" After Split: 'ga' 'tl' 'mz' 'cl' 'rq' 'tx' Rules for Decryption: • If both the letters are in the same column: Take the letter above each one (going back to the bottom if at the top).
For example: Diagraph: "cl" Decrypted Text: me Decryption: c -> m l -> e • If both the letters are in the same row: Take the letter to the left of each one (going back to the rightmost if at the leftmost position). For example: Diagraph: "tl" Decrypted Text: st Decryption: t -> s l -> t • If neither of the above rules is true: Form a rectangle with the two letters and take the letters on the horizontal opposite corner of the rectangle. For example: Diagraph: "rq" Decrypted Text: nt Decryption: r -> n q -> t For example:
Plain Text: "gatlmzclrqtx"
Decrypted Text: instrumentsz
Decryption:
(red)-> (green)
ga -> in
tl -> st
mz -> ru
cl -> me
rq -> nt
tx -> sz Advantages and Disadvantages • Advantages: 1. It is significantly harder to break since the frequency analysis technique used to break simple substitution ciphers is difficult but still can be used on (25*25) = 625 digraphs rather than 25 monographs which is difficult. 2. Frequency analysis thus requires more cipher text to crack the encryption. • Disadvantages: 1. An interesting weakness is the fact that a digraph in the ciphertext (AB) and it’s reverse (BA) will have corresponding plaintexts like UR and RU (and also ciphertext UR and RU will correspond to plaintext AB and BA, i.e. the substitution is self-inverse). That can easily be exploited with the aid of frequency analysis, if the language of the plaintext is known. 2. Another disadvantage is that playfair cipher is a symmetric cipher thus same key is used for both encryption and decryption.
c)
"""


def matrix(key):
    matrix = []
    for e in key.upper():
        if e not in matrix:
            matrix.append(e)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for e in alphabet:
        if e not in matrix:
            matrix.append(e)

    matrix_group = []
    for e in range(5):
        matrix_group.append('')

    # Break it into 5*5
    matrix_group[0] = matrix[0:5]
    matrix_group[1] = matrix[5:10]
    matrix_group[2] = matrix[10:15]
    matrix_group[3] = matrix[15:20]
    matrix_group[4] = matrix[20:25]
    return matrix_group


def message_to_digraphs(message_original):
    # Change it to Array. Because I want used insert() method
    message = []
    for e in message_original:
        message.append(e)

    # Delet space
    for unused in range(len(message)):
        if " " in message:
            message.remove(" ")

    # If both letters are the same, add an "X" after the first letter.
    i = 0
    for e in range(len(message) // 2):
        if message[i] == message[i + 1]:
            message.insert(i + 1, 'X')
        i = i + 2

    # If it is odd digit, add an "X" at the end
    if len(message) % 2 == 1:
        message.append("X")
    # Grouping
    i = 0
    new = []
    for x in range(1, len(message) // 2 + 1):
        new.append(message[i:i + 2])
        i = i + 2
    return new


def find_position(key_matrix, letter):
    x = y = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                x = i
                y = j

    return x, y


def cipher_to_digraphs(cipher):
    i = 0
    new = []
    for x in range(len(cipher) // 2):
        new.append(cipher[i:i + 2])
        i = i + 2
    return new


def encrypt(message):
    message = message_to_digraphs(message)
    key_matrix = matrix(key)
    cipher = []
    for e in message:
        p1, q1 = find_position(key_matrix, e[0])
        p2, q2 = find_position(key_matrix, e[1])
        if p1 == p2:
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            cipher.append(key_matrix[p1][q1 + 1])
            cipher.append(key_matrix[p1][q2 + 1])
        elif q1 == q2:
            if p1 == 4:
                p1 = -1;
            if p2 == 4:
                p2 = -1;
            cipher.append(key_matrix[p1 + 1][q1])
            cipher.append(key_matrix[p2 + 1][q2])
        else:
            cipher.append(key_matrix[p1][q2])
            cipher.append(key_matrix[p2][q1])
    return cipher


def decrypt(cipher):
    cipher = cipher_to_digraphs(cipher)
    key_matrix = matrix(key)
    plaintext = []
    for e in cipher:
        p1,q1 = find_position(key_matrix,e[0])
        p2,q2 = find_position(key_matrix,e[1])
        if p1 == p2:
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            plaintext.append(key_matrix[p1][q1 - 1])
            plaintext.append(key_matrix[p1][q2 - 1])
        elif q1 == q2:
            if p1 == 4:
                p1 = -1
            if p2 == 4:
                p2 = -1
            plaintext.append(key_matrix[p1 - 1][q1])
            plaintext.append(key_matrix[p2 - 1][q2])
        else:
            plaintext.append(key_matrix[p1][q2])
            plaintext.append(key_matrix[p2][q1])

    for unused in range(len(plaintext)):
        if "X" in plaintext:
            plaintext.remove("X")

    output = ""
    for e in plaintext:
        output += e
    return output


print("Playfair Cipher")
message = input("Enter the message : ")
key = input("Enter the key : ")
print(f"Encrypting: \n Message: {message}")
print("Break the message into digraphs: ")
print(message_to_digraphs(message))
print("Matrix: ")
print(matrix(key))
encrypted = encrypt(message)
print(f"Cipher: {encrypted}")

print(f"Decrypting: \n Cipher: {encrypted}")
print(f"Plaintext: {decrypt(encrypted)}")

