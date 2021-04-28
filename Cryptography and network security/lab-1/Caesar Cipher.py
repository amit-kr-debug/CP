"""
1. Encrypt and decrypt a file with composite data using the following Traditional symmetric key Ciphers:
a) Caesar Cipher The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials. Thus to cipher a given text we need an integer value, known as shift which indicates the number of position each letter of the text has been moved down. The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,…, Z = 25. Encryption of a letter by a shift n can be described mathematically as. (Encryption Phase with shift n) (Decryption Phase with shift n) Algorithm for Caesar Cipher: Input: 1. A String of lower case letters, called Text. 2. An Integer between 0-25 denoting the required shift. Procedure: • Traverse the given text one character at a time . • For each character, transform the given character as per the rule, depending on whether we’re encrypting or decrypting the text. • Return the new string generated. Examples:
Text : ABCDEFGHIJKLMNOPQRSTUVWXYZ
Shift: 23
Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW
Text : ATTACKATONCE
Shift: 4
Cipher: EXXEGOEXSRGI

Decryption We can either write another function decrypt similar to encrypt, that’ll apply the given shift in the opposite direction to decrypt the original text. However we can use the cyclic property of the cipher under modulo , hence we can simply observe
Cipher(n) = De-cipher(26-n) Hence, we can use the same function to decrypt, instead we’ll modify the shift value such that shift = 26-shift.
Cryptanalysis: Hacking of Caesar Cipher Algorithm
The cipher text can be hacked with various possibilities. One of such possibility is Brute Force Technique, which involves trying every possible decryption key. This technique does not demand much effort and is relatively simple for a hacker.
"""


def encrypt(text: str, shift: int):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


def decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        # accessing each char from the text
        char = text[i]
        if char == " ":
            result += " "

        else:
            # decrypt lowercase
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            # decrypt lowercase
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)
    return result


def cryptanalysis(text):
    results = []
    for shift in range(0,27):
        results.append(decrypt(text, shift))
    return results

if __name__ == "__main__":
    text = input("Enter the text to be encrypted: ")
    shift = int(input("Enter no. of Shift: "))
    print(f"Text: {text}")
    print(f"Shift: {shift}")
    encrypted = encrypt(text, shift)
    print(f"Cipher: {encrypted}")
    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted: {decrypted}")
    key = 0
    for hack in cryptanalysis(encrypted):
        print(f"Shift: {key}, text: {hack}")
        key += 1


