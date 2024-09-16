import random
from math import gcd

# Step 1: Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Step 2: Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Step 3: RSA key generation
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be the same.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.choice([i for i in range(2, phi) if gcd(i, phi) == 1])

    # Calculate d such that (e * d) % phi = 1
    d = mod_inverse(e, phi)

    # Public key (e, n) and Private key (d, n)
    return ((e, n), (d, n))

# Step 4: Encryption
def encrypt(public_key, plaintext):
    e, n = public_key
    return [(ord(char) ** e) % n for char in plaintext]

# Step 5: Decryption
def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr((char ** d) % n) for char in ciphertext])

# User input
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))
plaintext = input("Enter a message to encrypt: ")

# Generate RSA keys
public_key, private_key = generate_keypair(p, q)
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Encrypt and Decrypt
ciphertext = encrypt(public_key, plaintext)
print(f"Encrypted message: {ciphertext}")

decrypted_message = decrypt(private_key, ciphertext)
print(f"Decrypted message: {decrypted_message}")
