import os, User, sys, Operations
from Data import Vertices, Laguna


def Main():

    mainMenu = {
        1:"Display all cities",
        2:"Find the shortest path to a city",
        3:"Book a ride",
        4:"Display tickets",
        5:"Exit",
        }

    choice = ""
    while choice != "5":
        os.system('cls')
        print("Welcome to San Pedro Travels!\n\nMain Menu\n")
        for key in mainMenu:
            print(key,'-',mainMenu[key])
        choice = input("\nEnter your choice: ")

        if choice == "1":
            Operations.displayCities(Vertices)
        if choice == "2":
            os.system('cls')
            print("Find the shortest path\n")
            source = "SAN PEDRO" #San Pedro
            destination = input("From: SAN PEDRO\nTo: ").upper()
            totaldistance = Operations.dijkstra(Laguna,source,destination)
            Operations.displaydijkstra(source,destination,totaldistance)
        if choice == "3":
            os.system('cls')
            print("Book a ride\n")
            source = "SAN PEDRO"
            destination = input("From: SAN PEDRO\nTo: ").upper()
            totaldistance = Operations.dijkstra(Laguna,source,destination)
            Operations.bookRide(source,destination,totaldistance)
        if choice == "4":
            Operations.displayTickets()


Main()

