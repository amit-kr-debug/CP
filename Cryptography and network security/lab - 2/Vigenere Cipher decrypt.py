def decrypt(cipher_text,key):
    plain_text = ""
    # Decrypting plain text
    for i in range(len(cipher_text)):
        plain_text += chr(((ord(cipher_text[i]) - ord(key[i])) % 26) + 65)
    return plain_text


if __name__ == "__main__":
    # Taking key as input
    key = input("Enter the key:")
    # Taking plain text as input
    cipher_text = input("Enter the cipher text:")
    count = 0
    key_updated = ""
    # Updating Key
    for _ in cipher_text:
        if count == len(key):
            count = 0
        key_updated += key[count]
        count += 1
    print(decrypt(cipher_text.upper(),key_updated.upper()))
