import networkx as nx
G = nx.Graph()

heroes = ["Uther", "Zagara", "Muradin", "Valla"]

def getCounterAdvFor(hero1, hero2):
    pass

def getSynergyAdvFor(hero1, hero2):
    pass

for hero1 in heroes:
#    if hero1 not in G.nodes():
    G.add_node(hero1)

    for hero2 in heroes:
        if hero1 != hero2:
            adv_dict = {
                "CA": getCounterAdvFor(hero1, hero2),
                "SA": getSynergyAdvFor(hero1, hero2)
            }
            G.add_edge(hero1, hero2, adv_dict)

print(G.edges())





