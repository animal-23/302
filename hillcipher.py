import numpy as np 

def create_matrix_from_key(key, n): 
    key_matrix = [] 
    key = key.replace(" ", "") 
    for i in range(n): 
        key_matrix.append([ord(key[i * n + j]) % 65 for j in range(n)]) 
    return np.array(key_matrix) 

def encrypt_message(message, key_matrix, n): 
    message_vector = [] 
    for i in range(n): 
        message_vector.append(ord(message[i]) % 65) 
    message_vector = np.array(message_vector).reshape(n, 1) 
    cipher_matrix = np.dot(key_matrix, message_vector) % 26 
    cipher_text = ''.join([chr(cipher_matrix[i][0] + 65) for i in range(n)]) 
    return cipher_text 

def decrypt_message(cipher_text, key_matrix, n): 
    cipher_vector = [] 
    for i in range(n): 
        cipher_vector.append(ord(cipher_text[i]) % 65) 
    cipher_vector = np.array(cipher_vector).reshape(n, 1) 
    key_matrix_inv = np.linalg.inv(key_matrix) 
    adj_key_matrix = np.round(np.linalg.det(key_matrix) * key_matrix_inv).astype(int) % 26 
    det = round(np.linalg.det(key_matrix)) 
    inv_det = pow(det, -1, 26) 
    key_matrix_inv = (inv_det * adj_key_matrix) % 26 
    message_matrix = np.dot(key_matrix_inv, cipher_vector) % 26 
    return message_matrix 

def hill_cipher(): 
    message = input("Enter the message (only uppercase letters): ").replace(" ", "") 
    key = input("Enter the key (only uppercase letters): ").replace(" ", "") 
    n = int(len(message) ** 0.5) 
    if len(message) != len(key): 
        print("Error: Message length and key length should be the same.") 
        return 

    key_matrix = create_matrix_from_key(key, n) 
    cipher_text = encrypt_message(message, key_matrix, n) 
    print("Encrypted Message:", cipher_text) 
    decrypted_matrix = decrypt_message(cipher_text, key_matrix, n) 
    decrypted_text = ''.join([chr(int(decrypted_matrix[i][0]) + 65) for i in range(n)]) 
    print("Decrypted Message:", decrypted_text) 

if __name__ == "__main__":
    hill_cipher()
