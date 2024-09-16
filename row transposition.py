# Function to encrypt using row transposition
def encrypt(plaintext, key):
    columns = [''] * key
    for i, char in enumerate(plaintext):
        columns[i % key] += char
    
    # Join columns to get encrypted text
    ciphertext = ''.join(columns)
    return ciphertext

# Function to decrypt using row transposition
def decrypt(ciphertext, key):
    num_full_columns = len(ciphertext) // key
    remainder = len(ciphertext) % key
    
    columns = [''] * key
    index = 0
    
    # Fill each column for decryption
    for i in range(key):
        length = num_full_columns + (1 if i < remainder else 0)
        columns[i] = ciphertext[index:index + length]
        index += length
    
    # Recreate the original message
    plaintext = ''
    for i in range(num_full_columns + 1):
        for col in columns:
            if i < len(col):
                plaintext += col[i]
    
    return plaintext

# Get user input
plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key (number of columns): "))

# Encrypt the plaintext
ciphertext = encrypt(plaintext, key)
print("Encrypted Text:", ciphertext)

# Decrypt the ciphertext
decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)
