import random
import string

def generate_password(length):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue

            password = generate_password(length)
            print(f"Generated Password: {password}")

            another = input("Generate another password? (yes/no): ").lower()
            if another != "yes":
                print("Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
