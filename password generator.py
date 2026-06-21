
##------ PASSWORD GENERATOR PYTHON PROJECT
import random
import string
print("Welcome to our Password Generator")

def my_function():
    length = int(input("Enter The Length of Password you want:"))
    lowerdata = string.ascii_lowercase
    upperdata = string.ascii_uppercase
    digitdata = string.digits
    symbolsdata = string.punctuation
    combine = lowerdata + upperdata + digitdata + symbolsdata

    x = random.sample(combine,length)
    password = "".join(x)
    print(password)
    my_function()
my_function()
