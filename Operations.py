import sys, os, Validation
from Data import Vertices

def displayCities(vertices):
    os.system('cls')
    print("Cities of Laguna\n")
    for x in vertices:
        print(x.upper())

    pressKey = input("\nPress key to continue...")

def dijkstra(graph, initial, end):

    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"

        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
        
    
    

    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node

    path = path[::-1]

    return weight, path

def displaydijkstra(weight,path):
    os.system('cls')
    print("Find the shortest path\n")
    #weight = "{:.2f}".format(weight)
    print("{}{}km".format("Shortest Distance: ",weight))
    print("Shortest Path: ",end='')
    for i in path:
        print(i,"",end='')

    presskey = input("\n\nPress any key to continue...")



def bookRide(src,dest,totaldistance):
    ticketnum = getNumLines("Tickets.txt")
    name = Validation.nameValidation()
    number = Validation.phoneValidation()
    distanceConvert = float(totaldistance)
    rideFare = distanceConvert*3.25 #3.25 pesos per km
    format_rideFare = '{0:.2f}'.format(rideFare)

    ticket = open("Tickets.txt","a")
    ticket.writelines("{}|{}|{}|{}|{}|{}|{}\n".format(ticketnum,name,number,src,dest,totaldistance,format_rideFare))
    ticket.close()

    presskey = input("\nTicket succsefuly made\n\nPress any key to continue...")

def displayTickets():
    os.system('cls')
    with open(r"Tickets.txt",'r') as tickets:
        print ("{:<15} {:<15} {:<15} {:<12} {:<13} {:<10} {:<10}\n".format("Ticket Number","Name","Phone Number","Origin","Destination","Distance","Fare"))
        for line in tickets:
            data = line.strip().split('|')
            print ("{:<15} {:<15} {:<15} {:<12} {:<13} {:<10} {:<10}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))

    presskey = input("\nPress any key to continue...")

def ticketReports():
    os.system('cls')
    print("Ticket Sales Report\n")

    file = open("Tickets.txt",'r')
    lines = file.readlines()

    totalTicketSold = len(lines)
    totalTicketRevenue = 0
    for i in Vertices:
        for line in lines:
            data = line.split('|')
            if i == data[3]:
                totalTicketRevenue = float(data[6])+ totalTicketRevenue
    print("Total tickets sold: {}\nTotal ticket sales: ₱{:.2f}".format(totalTicketSold,totalTicketRevenue))
    
    presskey = input("\nPress any key to continue...")


def getNumLines(file):
    with open(r"{}".format(file), 'r') as file:
        number = len(file.readlines())

    number = number+1

    number = "{0:03}".format(number)
    return number

def getUserName(file):
    with open(r"{}".format(file), 'r') as file:
        for line in file:
            data = line.strip().split('|')
            name = data[3]
    return name
    
    
