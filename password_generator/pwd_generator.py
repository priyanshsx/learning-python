import string 
import secrets 

# ask the user for input on desired password length and what all they would want in the pwd 
# generator 

length = int(input("Desired password length: ").strip())
numbers = input("Would you like numbers? (y/n): ").strip().lower()
casing = input("Would you like uppercase letters? (y/n): ").strip().lower()
characters = input("Would you like special characters? (y/n): ").strip().lower()

char_pool = string.ascii_lowercase

# checking for users' inputs and outputting the password accordingly 

if numbers == 'y':
    char_pool += string.digits

if casing == 'y': 
    char_pool += string.ascii_uppercase

if characters == 'y':
    char_pool = string.punctuation

# generating the password 

password_list = []

# creating a loop to generate the password 

for _ in range(length):
    random_char = secrets.choice(char_pool)
    password_list.append(random_char)

# display the password 

final_password = ''.join(password_list)
print(f"Your desired password is: {final_password}")
