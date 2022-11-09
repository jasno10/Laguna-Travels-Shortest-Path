def nameValidation():
    name = ""
    while name == "":
        name = input("Enter passenger's name: ")
        if name == "":
            print("Please enter a valid name")
        else:
            return name.upper()

def phoneValidation():
    number = ""
    while number == "":
        number = input("Enter passenger's phone number: ")
        if len(number)!= 11:
            print("Please enter a valid phone number")
        else:
            return number

