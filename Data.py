from collections import defaultdict

Vertices =("SAN PEDRO","BINAN","STA ROSA","CABUYAO","CALAMBA","LOS BANOS","BAY","ALAMINOS","CALAUAN","SAN PABLO",
            "RIZAL","VICTORIA","NAGCARLAN","PILA","LILIW","STA CRUZ","MAGDALENA","MAJAYJAY","PAGSANJAN","LUISIANA",
            "LUMBAN","CAVINTI","KALAYAAN","PAETE","PAKIL","PANGIL","SINILOAN","FAMY","MABITAC","STA MARIA")

class Graph():
    def __init__(self):

        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

Laguna = Graph()

edges = [
    ("SAN PEDRO", "BINAN", 10),
    ("BINAN", "STA ROSA", 11.5),
    ("STA ROSA", "CABUYAO", 10.4),
    ("CABUYAO", "CALAMBA", 12.6),
    ("CALAMBA","LOS BANOS", 13.2),
    ("LOS BANOS","BAY",7.8),
    ("LOS BANOS","CALAUAN",11.8),
    ("LOS BANOS","VICTORIA",16.8),
    ("BAY","SAN PABLO",18.8),
    ("BAY","ALAMINOS",23.3),
    ("CALAUAN","NAGCARLAN",15),
    ("CALAUAN","RIZAL",25.8),
    ("CALAUAN","VICTORIA",13),
    ("VICTORIA","PILA",6.6),
    ("PILA","LILIW",18.2),
    ("PILA","STA CRUZ",6.7),
    ("STA CRUZ","MAGDALENA",10.5),
    ("LILIW","MAGDALENA",9.1),
    ("MAGDALENA","MAJAYJAY",130.9),
    ("MAJAYJAY","LUISIANA",23),
    ("LUISIANA","PAGSANJAN",20),
    ("PAGSANJAN","CAVINTI",16),
    ("PAGSANJAN","LUMBAN",11.8),
    ("LUMBAN","KALAYAAN",22.6),
    ("KALAYAAN","PAETE",9.3),
    ("PAETE","PAKIL",21.1),
    ("PAKIL","PANGIL",9.6),
    ("PANGIL","MABITAC",17.5),
    ("PANGIL","SINILOAN",10),
    ("PANGIL","FAMY",16.5),
    ("SINILOAN","STA MARIA", 20.7),
    ("MABITAC","STA MARIA",13.6),
    ("STA MARIA","FAMY",18.9)

    ]

for edge in edges:
    Laguna.add_edge(*edge)


