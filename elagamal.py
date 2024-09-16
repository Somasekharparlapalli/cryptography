import random

# Step 1: Modular exponentiation (fast computation of (base^exp) % mod)
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd
            result = (result * base) % mod
        exp = exp >> 1    # exp = exp // 2
        base = (base * base) % mod
    return result

# Step 2: Function to find modular inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Step 3: ElGamal Key Generation
def generate_keys(p, g):
    x = random.randint(1, p - 2)  # Private key x (1 < x < p-1)
    y = mod_exp(g, x, p)          # Public key y = g^x mod p
    return (p, g, y), x

# Step 4: ElGamal Signature Generation
def sign(message, private_key, p, g):
    x = private_key
    k = random.randint(1, p - 2)
    while gcd(k, p - 1) != 1:
        k = random.randint(1, p - 2)
    
    r = mod_exp(g, k, p)
    k_inv = mod_inverse(k, p - 1)
    s = (k_inv * (message - x * r)) % (p - 1)
    return r, s

# Step 5: ElGamal Signature Verification
def verify(message, signature, public_key):
    p, g, y = public_key
    r, s = signature
    if not (0 < r < p):
        return False
    v1 = mod_exp(g, message, p)
    v2 = (mod_exp(y, r, p) * mod_exp(r, s, p)) % p
    return v1 == v2

# Step 6: GCD Function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Get input from user
p = int(input("Enter a large prime number (p): "))
g = int(input("Enter a generator (g): "))
message = int(input("Enter a message as an integer: "))

# Key Generation
public_key, private_key = generate_keys(p, g)
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Signature Generation
signature = sign(message, private_key, p, g)
print(f"Signature: {signature}")

# Signature Verification
verification = verify(message, signature, public_key)
print(f"Signature valid: {verification}")
