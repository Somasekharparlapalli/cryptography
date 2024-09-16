import numpy as np

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def hill_cipher(text, key_matrix, mode='encrypt'):
    text = text.lower().replace(" ", "")
    n = len(key_matrix)
    padded_text = text + 'x' * (n - len(text) % n)
    result = ''

    for i in range(0, len(padded_text), n):
        vector = [ord(c) - ord('a') for c in padded_text[i:i+n]]
        if mode == 'decrypt':
            determinant = int(np.round(np.linalg.det(key_matrix)))
            inverse_matrix = mod_inverse(determinant % 26, 26) * np.round(determinant * np.linalg.inv(key_matrix)).astype(int) % 26
            key_matrix = inverse_matrix

        transformed_vector = np.dot(key_matrix, vector) % 26
        result += ''.join(chr(int(num) + ord('a')) for num in transformed_vector)

    return result

# Example usage
text = input("Enter a string: ")
key_matrix = np.array([[3, 3], [2, 5]])

encrypted_text = hill_cipher(text, key_matrix)
decrypted_text = hill_cipher(encrypted_text, key_matrix, mode='decrypt')

print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
