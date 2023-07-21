import random
import string


def generate_password(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for _ in range(length))
  return password


# Ask the user for the desired password length
try:
  password_length = int(input("Enter the desired password length: "))
  if password_length <= 0:
    print("The length must be greater than zero.")
  else:
    generated_password = generate_password(password_length)
    print(f"Generated password: {generated_password}")
except ValueError:
  print("Error. Please enter a valid integer.")
