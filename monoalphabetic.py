def create_monoalphabetic_cipher():
    # Define the substitution mapping (you can customize this)
    monoalpha_cipher = {
        'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c',
        'f': 'x', 'g': 'z', 'h': 'a', 'i': 's', 'j': 'd',
        'k': 'f', 'l': 'g', 'm': 'h', 'n': 'j', 'o': 'k',
        'p': 'l', 'q': 'p', 'r': 'o', 's': 'i', 't': 'u',
        'u': 'y', 'v': 't', 'w': 'r', 'x': 'e', 'y': 'w',
        'z': 'q', ' ': ' ',  # Space remains unchanged
    }
    return monoalpha_cipher

def encrypt_with_monoalphabetic(message, monoalpha_cipher):
    encrypted_message = []
    for char in message.lower():  # Convert to lowercase for consistency
        encrypted_char = monoalpha_cipher.get(char, char)
        encrypted_message.append(encrypted_char)
    return ''.join(encrypted_message)

def main():
    try:
        plaintext = input("Enter the text you want to encrypt: ")
        monoalpha_cipher = create_monoalphabetic_cipher()
        encrypted_text = encrypt_with_monoalphabetic(plaintext, monoalpha_cipher)
        print(f"Encrypted text: {encrypted_text}")
    except KeyboardInterrupt:
        print("\nOperation aborted by user.")

if __name__ == "__main__":
    main()
