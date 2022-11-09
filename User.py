import os, Operations

def loginUser():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(r"Users.txt",'r') as users:
        for line in users:
            data = line.strip().split('|')
            if username == data[1] and username == data[2]:
                homepage()

def createUser(userNum):
    print("Create a new user")
    username = input("Enter new username: ")
    password = input("Enter password: ")

    user = open("Users.txt","a")
    user.writelines("{}|{}|{}\n".format(userNum,username,password))
    user.close()

def getUserInfo():
    print("Get user info")

def fileExist():
    from os.path import exists
    file_exist = exists("Users.txt")
    if file_exist == False:
        file = open("Users.txt", 'w+')
        userNum = Operations.getNumLines("User.txt")
        createUser(userNum)
        file.close()
    else:
        loginUser()