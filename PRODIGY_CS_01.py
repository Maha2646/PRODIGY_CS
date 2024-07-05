def encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            new_char = char
        encrypted_text.append(new_char)
    return ''.join(encrypted_text)

def decrypt(text, shift):
    decrypted_text = []
    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            new_char = char
        decrypted_text.append(new_char)
    return ''.join(decrypted_text)

while True:
    choice = input("Enter your choice: 1) encrypt (e) 2) decrypt (d) 3) quit: ").lower()
    if choice == 'e':
        text = input("Name: ")
        shift = int(input("Shift value: "))
        print("Encrypted:", encrypt(text, shift))
    elif choice == 'd':
        text = input("Name: ")
        shift = int(input("Shift value: "))
        print("Decrypted:", decrypt(text, shift))
    elif choice == '3' or choice == 'quit':
        print("Quit......")
        break
    else:
        print("Invalid choice, please try again.")