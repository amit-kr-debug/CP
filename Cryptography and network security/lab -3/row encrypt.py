def encrypt(plain_text):
    cipher_text = ""
    i = 0
    while i < len(plain_text):
        cipher_text += plain_text[i]
        i += 2
    i = 1
    while i < len(plain_text):
        cipher_text += plain_text[i]
        i += 2
    return cipher_text


if __name__ == "__main__":
    msg = input("Enter the plain text:").replace(" ", "")
    print(encrypt(msg.upper()))