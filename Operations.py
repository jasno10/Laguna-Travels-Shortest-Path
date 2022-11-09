import sys, os
from heapq import heapify, heappop, heappush
from Data import Vertices

def displayCities(vertices):
    os.system('cls')
    print("Cities of Laguna\n")
    for x in vertices:
        print(x.upper())

    pressKey = input("\nPress key to continue...")

def dijkstra(graph,src,dest,name):
    os.system('cls')
    print('Find the shortest path\n')
    inf = sys.maxsize
    node_data = {
        'SAN PEDRO':{'distance':inf,'pred':[]},
        'BINAN':{'distance':inf,'pred':[]},
        'STA ROSA':{'distance':inf,'pred':[]},
        'CABUYAO':{'distance':inf,'pred':[]},
        'CALAMBA':{'distance':inf,'pred':[]},
        'LOS BANOS':{'distance':inf,'pred':[]},
        'BAY':{'distance':inf,'pred':[]},
        'ALAMINOS':{'distance':inf,'pred':[]},
        'CALAUAN':{'distance':inf,'pred':[]},
        'SAN PABLO':{'distance':inf,'pred':[]},
        'RIZAL':{'distance':inf,'pred':[]},
        'VICTORIA':{'distance':inf,'pred':[]},
        'NAGCARLAN':{'distance':inf,'pred':[]},
        'PILA':{'distance':inf,'pred':[]},
        'LILIW':{'distance':inf,'pred':[]},
        'STA CRUZ':{'distance':inf,'pred':[]},
        'MAGDALENA':{'distance':inf,'pred':[]},
        'MAJAYJAY':{'distance':inf,'pred':[]},
        'PAGSANJAN':{'distance':inf,'pred':[]},
        'LUISIANA':{'distance':inf,'pred':[]},
        'LUMBAN':{'distance':inf,'pred':[]},
        'CAVINTI':{'distance':inf,'pred':[]},
        'KALAYAAN':{'distance':inf,'pred':[]},
        'PAETE':{'distance':inf,'pred':[]},
        'PAKIL':{'distance':inf,'pred':[]},
        'PANGIL':{'distance':inf,'pred':[]},
        'SINILOAN':{'distance':inf,'pred':[]},
        'FAMY':{'distance':inf,'pred':[]},
        'MABITAC':{'distance':inf,'pred':[]},
        'STA MARIA':{'distance':inf,'pred':[]},
        }

    node_data[src]['distance'] = 0
    visited=[]
    temp=src
    shortest_path = [src]
    for i in range(29):
        if temp not in visited:
            visited.append(temp)
            min_heap=[]
            for j in graph[temp]:
                if j not in visited:
                    distance = node_data[temp]['distance'] + graph[temp][j]
                    if distance < node_data[j]['distance']:
                        node_data[j]['distance'] = distance
                        node_data[j]['pred'] = node_data[temp]['pred'] + [temp]
                        shortest_path.append(j)
                    heappush(min_heap,(node_data[j]['distance'], j))
        heapify(min_heap)

        #Check dead ends, 
        if min_heap:
            temp = min_heap[0][1]
        else:
            for i in shortest_path:
                if i != dest:
                    continue
                else:
                    #print(dest,end="")
                    break

            break

    print("Shortest Distance: " + str(node_data[dest]['distance'])+"km")
    print("Shortest Path: ",end="")


    choice = input("\n\nDo you want to book a ride? [Y/N]: ")

    if choice.upper() == "Y":
        totaldistance =  str(node_data[dest]['distance'])
        bookRide(totaldistance,src,dest,name)

    if choice.upper() == "N":
        main()


def bookRide(distance,src,dest,name):
    os.system('cls')
    print("Book a ride\n\n")
    ticketnum = getNumLines("Tickets.txt")
    name = input("Enter your name: ").upper()
    number = str(input("Enter your number: "))
    distanceConvert = float(distance)
    rideFare = distanceConvert*3.25 #3.25 pesos per km
    format_rideFare = '{0:.2f}'.format(rideFare)

    print("Ticket made")

    ticket = open("Tickets.txt","a")
    ticket.writelines("{}|{}|{}|{}|{}|{}|{}\n".format(ticketnum,name,number,src,dest,distance,format_rideFare))
    ticket.close()

def displayTickets():
    with open(r"Tickets.txt",'r') as tickets:
        print ("{:<15} {:<15} {:<15} {:<12} {:<13} {:<10} {:<10}".format("Ticket Number","Name","Phone Number","Origin","Destination","Distance","Fare"))
        for line in tickets:
            data = line.strip().split('|')
            if name == data[2]:
                print ("{:<15} {:<15} {:<15} {:<12} {:<13} {:<10} {:<10}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))


def getNumLines(file):
    with open(r"{}".format(file), 'r') as file:
        number = len(file.readlines())

    number = number+1

    number = "{0:03}".format(number)
    return number
    
    
