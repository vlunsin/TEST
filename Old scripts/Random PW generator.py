# Based on user preferences, collect 
# length
# should contain upper cases
# should contain special characters
# should contain numbers

# randomly select characters in the list of the preferences
# create all available characters from the preferences
# then pick one by one until desired length
# ensure we have at least each character type
# ensure length is valid

import random
# give access to all characters
import string

def generate_password():
    # int make the result an integer
    length = int(input("Entire desired PW length: ").strip())
    include_uppercase = input("Include upper case letters? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    # make the length of four minimum
    if length < 4:
        print("PW must be at least 4 characters")
        return
    
    # get all characters
    lower = string.ascii_lowercase  # give all characters lowercase
    # inline if statement
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    # concatenate all characters
    all_characters = lower + uppercase + special + digits

    print(all_characters)

    # List to append new characters easily
    # faster to add an element in a list
    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters  

    # _ place holder, if variable for looping isn't important
    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    # shuffle the list
    random.shuffle(password)

   
    
    # convert to string
    # .join will take the list and combine with the characters before the join. 
    # in this case empty, so will join with empty character
    # can join with , . / etc...
    str_password = "".join(password)

    print(password)

generate_password()