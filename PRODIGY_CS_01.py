# Function to encrypt the text using a Caesar cipher shift
def encrypt(text, shift):
    encrypted_text = ""  # Initialize an empty string for the encrypted message
    for char in text:  # Loop through each character in the input text
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')  # Determine ASCII base for uppercase or lowercase
            encrypted_text += chr((ord(char) + shift - shift_base) % 26 + shift_base)  # Apply shift while maintaining case
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text  # Return the encrypted text

# Function to decrypt text by shifting in the opposite direction
def decrypt(text, shift):
    return encrypt(text, -shift)  # Decrypting is just encrypting with a negative shift

# Main function to handle user input and interaction
def main():
    # Ask user whether they want to encrypt or decrypt
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().upper()
    message = input("Enter your message: ")  # Get the text to be processed
    shift = int(input("Enter the shift value (1-25): "))  # Get the shift value (must be between 1 and 25)

    if choice == 'E':  # If the user chooses encryption
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'D':  # If the user chooses decryption
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice. Please select either 'E' for encrypt or 'D' for decrypt.")  # Handle invalid input

# Ensure the script runs only if executed directly (not imported as a module)
if __name__ == "__main__":
    main()
