import hashlib

# Step 1: Hashing Function
def hash_message(message, algorithm):
    # Select the algorithm
    if algorithm == 'sha256':
        hasher = hashlib.sha256()
    elif algorithm == 'md5':
        hasher = hashlib.md5()
    else:
        raise ValueError("Unsupported algorithm. Use 'sha256' or 'md5'.")

    # Encode the message and update the hasher
    hasher.update(message.encode('utf-8'))
    return hasher.hexdigest()

# Get input from user
message = input("Enter a message to hash: ")
algorithm = input("Choose hashing algorithm ('sha256' or 'md5'): ")

# Generate hash
hashed_message = hash_message(message, algorithm)
print(f"Hashed message using {algorithm}: {hashed_message}")
