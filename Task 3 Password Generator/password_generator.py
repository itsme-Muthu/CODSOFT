import random

# generate password
# password contains atleast one char, one number and one special character and has a minimum length of 8 
# [as a strong password is required]

# generates required password
def passwordGenerator(length):
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num  = "1234567890"
    specialChar = "!@#$%^&*()-[]{'};:<,>.?+_/|"
    generator = char+num+specialChar
    password = [random.choice(char),random.choice(num),random.choice(specialChar)]
    password = password + random.sample(generator,length-3)
    random.shuffle(password)
    return "".join(password)

# gets input for the length of the password (atleast of 8 characters)
def password():
    while True:
        len = int(input("Enter the length of the password (atleast 8): "))
        if len < 8:
            print("Length of the password should atleast be 8!")
            continue
        break
    
    result = passwordGenerator(len)
    print("Output: ",result)

password()
