from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Step 1: AES Encryption using CFB mode
def encrypt_cfb(key, plaintext, iv):
    # Create a cipher object using AES in CFB mode
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Perform the encryption
    ciphertext = encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()
    return ciphertext

# Step 2: AES Decryption using CFB mode
def decrypt_cfb(key, ciphertext, iv):
    # Create a cipher object for decryption
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Perform the decryption
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode('utf-8')

# Get input from user
plaintext = input("Enter a message to encrypt: ")

# Step 3: Generate a random key and IV (Initialization Vector)
key = os.urandom(32)  # AES-256, 32 bytes key
iv = os.urandom(16)   # AES block size is 16 bytes

# Step 4: Encrypt the message
ciphertext = encrypt_cfb(key, plaintext, iv)
print(f"Encrypted message (in bytes): {ciphertext}")

# Step 5: Decrypt the message
decrypted_message = decrypt_cfb(key, ciphertext, iv)
print(f"Decrypted message: {decrypted_message}")
