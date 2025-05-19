# Example file for Advanced Python by Joe Marini
# Using the built-in string constants

import string


# built-in constants for a variety of needs
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)

print("*"*50)

# Define a test string
testStr = "The quick brown fox jumps OVER the lazy dog."

# use an iterator to see if a string contains any punctuation 
print(f"Has punctuation:", any(c in string.punctuation for c in testStr))
print("*"*50)

# generate a secure random password
import secrets
alphabet = string.ascii_letters + string.digits + string.punctuation
pass_length = 8

new_passwd = ''.join(secrets.choice(alphabet) for i in range(pass_length))
print(f"Your new password is:",new_passwd)

print("*"*50)

# Check the strength of a password
def check_password_strength(testPass):
  if len(testPass) >= 10 and any(c in string.ascii_letters[:26] for c in testPass) and \
    any(c in string.ascii_letters[26:] for c in testPass) and \
    any(c in string.punctuation for c in testPass) and any(c in string.digits for c in testPass):
    return f"{testPass} is a string password"
  return f"{testPass} is a weak password"

print(check_password_strength("MyTestPa$$123!"))
print(check_password_strength("password"))
print(check_password_strength("pa$$w0rd!"))
print(check_password_strength("Power.TG!"))
