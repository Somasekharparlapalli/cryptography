import hashlib

# Step 1: Hashing function using SHA-256
def sha256_hash(message):
    sha_signature = hashlib.sha256(message.encode('utf-8')).hexdigest()
    return sha_signature

# Get input from user
message = input("Enter a message to hash with SHA-256: ")

# Generate SHA-256 hash
hashed_message = sha256_hash(message)

# Output the hashed message
print(f"SHA-256 hash of the message is: {hashed_message}")
