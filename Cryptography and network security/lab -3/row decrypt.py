import math
def decrypt(cipher_text):
    plain_text = ""
    i = 0
    j = i + math.ceil(len(cipher_text)/2)
    while i < math.ceil(len(cipher_text)/2) and j < len(cipher_text):
        plain_text += cipher_text[i]
        i += 1
        plain_text += cipher_text[j]
        j += 1
    if i <= math.ceil(len(plain_text)/2):
        plain_text += cipher_text[i]
    return plain_text


if __name__ == "__main__":
    cipher_text = input("Enter the cipher text:")
    print(decrypt(cipher_text.upper()))