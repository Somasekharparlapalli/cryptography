# Function to prepare the text (removes spaces, handles 'J' as 'I')
def prepare_text(text):
    text = text.upper().replace('J', 'I').replace(' ', '')
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            result += 'X'
        if i + 1 < len(text):
            result += text[i + 1]
        i += 2
    if len(result) % 2 != 0:
        result += 'X'
    return result

# Create the Playfair cipher square (5x5)
def create_square(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = "".join(sorted(set(key.upper().replace('J', 'I')), key=lambda x: key.index(x)))
    square = ''.join([c for c in key if c in alphabet] + [c for c in alphabet if c not in key])
    return [list(square[i:i + 5]) for i in range(0, 25, 5)]

# Find position of a letter in the square
def find_position(letter, square):
    for row in range(5):
        if letter in square[row]:
            return row, square[row].index(letter)
    return None

# Encrypt a digraph (pair of letters)
def encrypt_digraph(digraph, square):
    row1, col1 = find_position(digraph[0], square)
    row2, col2 = find_position(digraph[1], square)

    if row1 == row2:
        return square[row1][(col1 + 1) % 5] + square[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return square[(row1 + 1) % 5][col1] + square[(row2 + 1) % 5][col2]
    else:
        return square[row1][col2] + square[row2][col1]

# Playfair cipher encryption
def playfair_encrypt(plaintext, key):
    square = create_square(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        ciphertext += encrypt_digraph(plaintext[i:i + 2], square)
    return ciphertext

# Main program
key = input("Enter the key: ")
plaintext = input("Enter the plaintext: ")
ciphertext = playfair_encrypt(plaintext, key)
print("Encrypted message:", ciphertext)
