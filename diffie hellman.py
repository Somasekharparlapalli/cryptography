import random

# Step 1: Diffie-Hellman Key Exchange
def diffie_hellman(p, g, private_key):
    # Compute public key
    public_key = pow(g, private_key, p)
    return public_key

# Step 2: Compute the shared secret
def compute_shared_secret(public_key, private_key, p):
    # Compute the shared secret
    shared_secret = pow(public_key, private_key, p)
    return shared_secret

# Get input from user
p = int(input("Enter a large prime number (p): "))
g = int(input("Enter a generator (g): "))

# Private keys (chosen randomly by both parties)
private_key_A = random.randint(1, p - 1)
private_key_B = random.randint(1, p - 1)

# Step 3: Compute public keys for both parties
public_key_A = diffie_hellman(p, g, private_key_A)
public_key_B = diffie_hellman(p, g, private_key_B)

print(f"Public key of Party A: {public_key_A}")
print(f"Public key of Party B: {public_key_B}")

# Step 4: Compute the shared secret for both parties
shared_secret_A = compute_shared_secret(public_key_B, private_key_A, p)
shared_secret_B = compute_shared_secret(public_key_A, private_key_B, p)

# Step 5: Display the shared secrets
print(f"Shared secret (computed by Party A): {shared_secret_A}")
print(f"Shared secret (computed by Party B): {shared_secret_B}")

# Check if the shared secrets match
if shared_secret_A == shared_secret_B:
    print("Shared secret successfully established!")
else:
    print("Shared secret mismatch.")
