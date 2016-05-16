import networkx as nx
G = nx.Graph()
import random

all_heroes = ["abathur", "anubarak", "artanis", "arthas", "azmodan", "brightwing", "chen",
    "chogall", "chromie", "dehaka", "diablo", "etc", "falstad", "gazlowe", "greymane", "illidan",
    "jaina", "johanna", "kaelthas", "kerrigan", "kharazim", "leoric", "li-ming",
    "lili", "lt-morales", "lunara", "malfurion", "muradin", "murky", "nazeebo",
    "nova", "raynor", "rehgar", "rexxar", "sgt-hammer", "sonya", "stitches", "sylvanas",
    "tassadar", "the-butcher", "the-lost-vikings", "thrall", "tracer", "tychus",
    "tyrael", "tyrande", "uther", "valla", "xul", "zagara", "zeratul"]

def getCounterAdvFor(hero1, hero2):
    # G.get_edge_data(hero1, hero2).counterAdv()

    return random.randrange(-800, 800)

def getSynergyAdvFor(hero1, hero2):
    # G.get_edge_data(hero1, hero2).counterAdv()
    return random.randrange(-800, 800)

for hero1 in all_heroes:
#    if hero1 not in G.nodes():
    G.add_node(hero1)

    for hero2 in all_heroes:
        if hero1 != hero2:
            counter_adv_var = getCounterAdvFor(hero1, hero2)
            synergy_adv_var = getSynergyAdvFor(hero1, hero2)

            G.add_edge(hero1, hero2, counter_adv = counter_adv_var, synergy_adv = synergy_adv_var)

# for an_edge in G.edges():
def main():
    print(G.edge['artanis']['arthas'])

main()

