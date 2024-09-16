# Function to encrypt using Rail Fence Cipher
def encrypt_rail_fence(text, key):
    fence = [''] * key
    rail = 0
    direction = 1  # 1 means moving down, -1 means moving up

    for char in text:
        fence[rail] += char
        rail += direction

        if rail == 0 or rail == key - 1:
            direction *= -1

    return ''.join(fence)

# Function to decrypt using Rail Fence Cipher
def decrypt_rail_fence(cipher, key):
    fence = [['\n'] * len(cipher) for _ in range(key)]
    rail = 0
    direction = 1
    idx = 0

    # Mark the positions to fill the characters
    for char in cipher:
        fence[rail][idx] = '*'
        idx += 1
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1

    # Fill the rail fence with cipher text
    idx = 0
    for i in range(key):
        for j in range(len(cipher)):
            if fence[i][j] == '*':
                fence[i][j] = cipher[idx]
                idx += 1

    # Read the decrypted message
    result = []
    rail = 0
    direction = 1
    for i in range(len(cipher)):
        result.append(fence[rail][i])
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1

    return ''.join(result)

# Get input from the user
text = input("Enter the text: ")
key = int(input("Enter the key (number of rails): "))

# Encrypt the text
cipher_text = encrypt_rail_fence(text, key)
print("Encrypted Text:", cipher_text)

# Decrypt the text
decrypted_text = decrypt_rail_fence(cipher_text, key)
print("Decrypted Text:", decrypted_text)
