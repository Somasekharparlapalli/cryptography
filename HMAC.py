import hmac
import hashlib

def get_user_input():
    # Get key and message from user
    key = input("Enter the key (in hex format, e.g., 'key123'): ")
    message = input("Enter the message: ")
    
    # Convert the hex key to bytes
    key_bytes = bytes.fromhex(key)
    # Convert the message to bytes
    message_bytes = message.encode()
    
    return key_bytes, message_bytes

def compute_hmac(key_bytes, message_bytes):
    # Create a new HMAC object using the key and message
    hmac_obj = hmac.new(key_bytes, message_bytes, hashlib.sha256)
    # Compute the HMAC digest
    hmac_digest = hmac_obj.hexdigest()
    return hmac_digest

def main():
    key_bytes, message_bytes = get_user_input()
    hmac_digest = compute_hmac(key_bytes, message_bytes)
    print(f"HMAC: {hmac_digest}")

if __name__ == "__main__":
    main()
