import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    # Define the character sets based on user preferences
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    # Generate password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt user for password complexity options
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"
    
    # Prompt user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))
    
    # Generate password
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
