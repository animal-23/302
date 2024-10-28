from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_message = pad(message.encode('utf-8'), AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message

def aes_decrypt(encrypted_message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message)
    original_message = unpad(decrypted_message, AES.block_size)
    return original_message.decode('utf-8')

def main():
    key = input("Enter a key (16, 24, or 32 characters for 128, 192, or 256-bit encryption): ").encode('utf-8')
    if len(key) not in [16, 24, 32]:
        print("Error: Key must be 16, 24, or 32 characters long.")
        return

    choice = input("Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message: ").lower()
    if choice == 'encrypt':
        message = input("Enter the message to encrypt: ")
        encrypted_message = aes_encrypt(message, key)
        print("Encrypted Message (hex):", encrypted_message.hex())
    elif choice == 'decrypt':
        encrypted_message_hex = input("Enter the message to decrypt (in hexadecimal): ")
        encrypted_message = bytes.fromhex(encrypted_message_hex)
        decrypted_message = aes_decrypt(encrypted_message, key)
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid choice! Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
