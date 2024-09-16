def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key = key.upper()  # Convert the key to uppercase for consistency
    key_length = len(key)
    
    for i, char in enumerate(plain_text):
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = ord(key[i % key_length]) - ord("A")
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def main():
    try:
        plaintext = input("Enter the text you want to encrypt: ")
        key = input("Enter the encryption key (keyword or phrase): ")
        encrypted_text = vigenere_encrypt(plaintext, key)
        print(f"Encrypted text: {encrypted_text}")
    except KeyboardInterrupt:
        print("\nOperation aborted by user.")

if __name__ == "__main__":
    main()
