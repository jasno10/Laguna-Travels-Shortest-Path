Vertices = ["SAN PEDRO","BINAN","STA ROSA","CABUYAO","CALAMBA","LOS BANOS","BAY","ALAMINOS","CALAUAN","SAN PABLO",
            "RIZAL","VICTORIA","NAGCARLAN","PILA","LILIW","STA CRUZ","MAGDALENA","MAJAYJAY","PAGSANJAN","LUISIANA",
            "LUMBAN","CAVINTI","KALAYAAN","PAETE","PAKIL","PANGIL","SINILOAN","FAMY","MABITAC","STA MARIA"]

Laguna = {
    'SAN PEDRO':{'BINAN':10},
    'BINAN':{'SAN PEDRO':10,'STA ROSA':11.5},
    'STA ROSA':{'BINAN':11.5,'CABUYAO':10.4},
    'CABUYAO':{'STA ROSA':10.4,'CALAMBA':12.6},
    'CALAMBA':{'CABUYAO':12.6,'LOS BANOS':13.2},
    'LOS BANOS':{'CALAMBA':13.2,'BAY':7.8,'CALAUAN':11.8,'VICTORIA':16.8},
    'BAY':{'LOS BANOS':7.8,'SAN PABLO': 18.8,'ALAMINOS':23.3},
    'ALAMINOS':{'BAY':23.3},
    'ALAMINOS':{'BAY':23.3},
    'CALAUAN':{'LOS BANOS': 11.8,'SAN PABLO': 11.7,'NAGCARLAN':15,'RIZAL':25.8},
    'SAN PABLO':{'CALAUAN':11.7,'BAY':18.8},
    'RIZAL':{'CALAUAN': 25.8 },
    'VICTORIA':{'LOS BANOS': 16.8, 'CALAUAN': 13, 'PILA': 6.6},
    'NAGCARLAN':{'CALAUAN': 15},
    'PILA':{'VICTORIA': 6.6 , 'LILIW': 18.2, 'STA CRUZ': 6.7},
    'LILIW':{'PILA': 18.2 , 'MAGDALENA': 9.1 },
    'STA CRUZ':{'PILA': 6.7 ,'MAGDALENA': 10.5},
    'MAGDALENA':{'LILIW': 9.1, 'STA CRUZ': 10.5, 'MAJAYJAY': 10.9, 'PAGSANJAN': 11.3},
    'MAJAYJAY':{'MAGDALENA': 10.9, 'LUISIANA': 23.3},
    'PAGSANJAN':{'MAGDALENA': 11.3, 'LUISIANA': 20, 'LUMBAN': 11.8, 'CAVINTI': 16},
    'LUISIANA':{'MAJAYJAY': 23.3, 'PAGSANJAN': 20},
    'LUMBAN': {'PAGSANJAN':11.8, 'KALAYAAN':22.6},
    'CAVINTI': {'PAGSANJAN':16},
    'KALAYAAN': {'LUMBAN':11.8, 'PAETE':9.3},
    'PAETE': {'KALAYAAN':9.3, 'PAKIL':21.1},
    'PAKIL': {'PAETE':21.1, 'PANGIL':9.6},
    'PANGIL': {'SINILOAN':10, 'MABITAC':17.5, 'FAMY':16.5},
    'SINILOAN': {'PANGIL':10, 'STA MARIA':20.7},
    'FAMY': {'STA MARIA':18.9, 'PANGIL':16.5 },
    'MABITAC': {'PANGIL':17.5, 'STA MARIA':13.6},
    'STA MARIA': {'MABITAC':13.6, 'FAMY':18.9, 'SINILOAN':20.7},
    }

