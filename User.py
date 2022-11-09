import os, Operations

def loginUser():
    username = input("Enter username: ").upper()
    password = input("Enter password: ").upper()

    with open(r"Users.txt",'r') as users:
        for line in users:
            data = line.strip().split('|')

            if username == data[1] and password == data[2]:
                name = data[3]
                return name
            else:
                print("User not found")
                loginUser()


def createUser():
    print("Create a new user")
    userNum = Operations.getNumLines("Users.txt")

    username = input("Enter new username: ").upper()
    name = input("Enter full name: ").upper()
    password = input("Enter password: ").upper()

    user = open("Users.txt","a")
    user.writelines("{}|{}|{}|{}\n".format(userNum,username,password,name))
    user.close()

def getUserInfo():
    print("Get user info")

def fileExist():
    from os.path import exists
    file_exist = exists("Users.txt")
    if file_exist == False:
        file = open("Users.txt", 'w')
        userNum = Operations.getNumLines("Users.txt")
        createUser()
        file.close()
    else:
        print("1 - Login\n2 - Create Account")
        choice = input("Enter your choice: ")
        if choice == "1":
            loginUser()
        elif choice == "2":
            createUser()
