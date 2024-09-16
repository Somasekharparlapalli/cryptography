from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Step 1: AES Encryption using CBC mode
def encrypt_cbc(key, plaintext, iv):
    # Padding the plaintext to be a multiple of the block size (AES block size is 128 bits)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()

    # Create a cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Perform the encryption
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

# Step 2: AES Decryption using CBC mode
def decrypt_cbc(key, ciphertext, iv):
    # Create a cipher object for decryption
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Perform the decryption
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpadding the plaintext
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode('utf-8')

# Get input from user
plaintext = input("Enter a message to encrypt: ")

# Step 3: Generate a random key and IV (Initialization Vector)
key = os.urandom(32)  # AES-256, 32 bytes key
iv = os.urandom(16)   # AES block size is 16 bytes

# Step 4: Encrypt the message
ciphertext = encrypt_cbc(key, plaintext, iv)
print(f"Encrypted message (in bytes): {ciphertext}")

# Step 5: Decrypt the message
decrypted_message = decrypt_cbc(key, ciphertext, iv)
print(f"Decrypted message: {decrypted_message}")
