#PasswordGenerator

#import string module which contains letters and digits 
#import random module to generate random numbers and selecting random items

import string
import random

#defining a func called generate_password() which has 1 parameter "length" which is interger(int) and it's length is 18
def generate_password(length : int = 18):

    #It will create a alphabet string which contains a-z, A-Z, 0-9 and punctuations for our password
    alphabet = string.ascii_letters + string.digits + string.punctuation

#This will create a random password picking up a random character
#It will run a loop according tothe password's length and converts all this into a single string using join
    password = ''.join(random.choice(alphabet)for i in range (length))

#This is used to return the func back to the user
    return password

#This will generate a password and store it into the password variable
password = generate_password()

#Prints the generated password stored in the password variable
print(f"Generated Password: {password}")
