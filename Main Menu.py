import os, sys, Operations, Validation
from Data import Vertices, Laguna


def Main():

    mainMenu = {
        1:"Display all cities",
        2:"Find the shortest path to a city",
        3:"Book a ride",
        4:"Display tickets",
        5:"Ticket sales report",
        6:"Exit",
        }

    choice = ""
    while choice != "6":
        os.system('cls')
        print("Welcome to Laguna Travels!\n\nMain Menu\n")
        for key in mainMenu:
            print(key,'-',mainMenu[key])
        choice = input("\nEnter your choice: ")

        if choice == "1":
            Operations.displayCities(Vertices)
        if choice == "2":
            os.system('cls')
            print("Find the shortest path\n")
            source = Validation.cityValidation("From: ")
            destination = Validation.cityValidation("To: ")
            totaldistance, shortest_path= Operations.dijkstra(Laguna,source,destination)
            #print(totaldistance,"km")
            #print(shortest_path)
            Operations.displaydijkstra(totaldistance,shortest_path)
        if choice == "3":
            os.system('cls')
            print("Book a ride\n")
            source = Validation.cityValidation("From: ")
            destination = Validation.cityValidation("To: ")
            totaldistance,shortest_path = Operations.dijkstra(Laguna,source,destination)
            Operations.bookRide(source,destination,totaldistance)
        if choice == "4":
            Operations.displayTickets()
        if choice == "5":
            Operations.ticketReports()


Main()

