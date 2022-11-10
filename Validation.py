from Data import Vertices
import os
def cityValidation(message):
    os.system('cls')
    city = ""
    while city == "":
        city = input(message)
        if city not in Vertices:
            presskey = input("Please enter a valid city, press any key to try again...")
            cityValidation(message)
        else:
            return city.upper()

def nameValidation():
    os.system('cls')
    name = ""
    while name == "":
        name = input("Enter passenger's name: ")
        if name == "":
            presskey = input("Please enter a valid name, press any key to try again...")
            nameValidation()
        else:
            return name.upper()

def phoneValidation():
    os.system('cls')
    number = ""
    while number == "":
        number = input("Enter passenger's phone number: ")
        if len(number)!= 11:
            presskey = input("Please enter a valid phone number, press any key to try again...")
            phoneValidation()
        else:
            return number

