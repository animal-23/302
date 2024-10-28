def generate_playfair_matrix(key):
    # Remove duplicate letters from the key and create the Playfair matrix
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is usually omitted
    key = ''.join(sorted(set(key), key=key.index)).upper().replace("J", "I")
    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def format_message(message):
    # Format the message into digraphs, replacing J with I
    message = message.upper().replace(" ", "").replace("J", "I")
    formatted_message = []
    i = 0
    while i < len(message):
        a = message[i]
        if i + 1 < len(message):
            b = message[i + 1]
            if a != b:
                formatted_message.append(a + b)
                i += 2
            else:
                formatted_message.append(a + "X")
                i += 1
        else:
            formatted_message.append(a + "X")
            i += 1
    return formatted_message

def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j
    return None

def encrypt_digraph(digraph, matrix):
    a, b = digraph[0], digraph[1]
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    if row_a == row_b:
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

def decrypt_digraph(digraph, matrix):
    a, b = digraph[0], digraph[1]
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    if row_a == row_b:
        return matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

def playfair_cipher():
    key = input("Enter the key (only uppercase letters): ").upper().replace("J", "I")
    choice = input("Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message: ").lower()
    message = input("Enter the message (only uppercase letters): ").upper().replace("J", "I")

    matrix = generate_playfair_matrix(key)
    if choice == 'encrypt':
        digraphs = format_message(message)
        cipher_text = ''.join([encrypt_digraph(digraph, matrix) for digraph in digraphs])
        print("Encrypted Message:", cipher_text)
    elif choice == 'decrypt':
        digraphs = [message[i:i+2] for i in range(0, len(message), 2)]
        plain_text = ''.join([decrypt_digraph(digraph, matrix) for digraph in digraphs])
        print("Decrypted Message:", plain_text)
    else:
        print("Invalid choice! Please type 'encrypt' or 'decrypt'.")

playfair_cipher()
