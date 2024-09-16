def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether it's an uppercase or lowercase letter
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result

def main():
    try:
        plaintext = input("Enter the text you want to encrypt: ")
        shift_amount = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
        encrypted_text = caesar_cipher(plaintext, shift_amount)
        print(f"Encrypted text: {encrypted_text}")
    except ValueError:
        print("Invalid input. Please enter a valid shift value (an integer).")

if __name__ == "__main__":
    main()
