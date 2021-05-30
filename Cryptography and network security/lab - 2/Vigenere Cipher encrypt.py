def encrypt(plain_text,  key):
    cipher_text = ""
    # Encrypting plain text
    for i in range(len(plain_text)):
        cipher_text += chr(((ord(plain_text[i]) + ord(key[i]) - 130) % 26) + 65)
    return cipher_text


if __name__ == "__main__":
    # Taking key as input
    key = input("Enter the key:")
    # Taking plain text as input
    plain_text = input("Enter the plain text:")
    count = 0
    key_updated = ""
    # Updating Key
    for _ in plain_text:
        if count == len(key):
            count = 0
        key_updated += key[count]
        count += 1
    print("Cipher text:",end = "")
    print(encrypt(plain_text.upper(),key_updated.upper()))
