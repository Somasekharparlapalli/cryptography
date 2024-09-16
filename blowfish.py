from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import base64

def get_user_input():
    key = input("Enter the key (in hex format, e.g., '0123456789abcdef'): ")
    plaintext = input("Enter the plaintext message: ")

    # Convert the hex key to bytes
    key_bytes = bytes.fromhex(key)
    # Ensure the key length is appropriate for Blowfish (up to 56 bytes)
    if len(key_bytes) > 56:
        raise ValueError("Key length should be between 1 and 56 bytes.")
    
    return key_bytes, plaintext.encode()

def encrypt_message(key_bytes, plaintext_bytes):
    cipher = Blowfish.new(key_bytes, Blowfish.MODE_CBC)
    # Pad plaintext to be a multiple of block size (8 bytes for Blowfish)
    padded_plaintext = pad(plaintext_bytes, Blowfish.block_size)
    ciphertext_bytes = cipher.encrypt(padded_plaintext)
    # Encode the result as base64 to make it easy to display
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ciphertext = base64.b64encode(ciphertext_bytes).decode('utf-8')
    return iv, ciphertext

def decrypt_message(key_bytes, iv, ciphertext):
    cipher = Blowfish.new(key_bytes, Blowfish.MODE_CBC, iv=base64.b64decode(iv))
    ciphertext_bytes = base64.b64decode(ciphertext)
    padded_plaintext = cipher.decrypt(ciphertext_bytes)
    # Unpad plaintext
    plaintext_bytes = unpad(padded_plaintext, Blowfish.block_size)
    return plaintext_bytes.decode()

def main():
    key_bytes, plaintext_bytes = get_user_input()
    
    # Encrypt the message
    iv, ciphertext = encrypt_message(key_bytes, plaintext_bytes)
    print(f"IV (Base64): {iv}")
    print(f"Ciphertext (Base64): {ciphertext}")
    
    # Decrypt the message
    decrypted_message = decrypt_message(key_bytes, iv, ciphertext)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
