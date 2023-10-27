import random
import string

def generate_password(length=12):
    # Define a pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# You can specify the desired length of the password
password_length = int(input("Enter the desired password length: "))
if password_length < 1:
    print("Password length must be at least 1.")
else:
    password = generate_password(password_length)
    print("Generated password:", password)
