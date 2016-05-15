
from heroes_graph import G, all_heroes

#
# Vertices: Heroes, Edges: counter/synergy weights
#

class HoTS_Drafter:
    def __init__(self, allied_heroes, enemy_heroes, owned_heroes):
        self.allied_hero_selections = allied_heroes
        self.enemy_hero_selections = enemy_heroes
        self.user_owned_heroes = owned_heroes
        # self.user_hero_preferences = {}

        self.calculator = OptimalSelectionCalculator(self)

class OptimalSelectionCalculator:
    def __init__(self, drafter):
        self.drafter = drafter

        self.advantages = {}

        self.findOptimalSelections()

    def findOptimalSelections(self):
        for a_hero in all_heroes:
            for an_enemy_hero in self.drafter.enemy_hero_selections:
                if a_hero != an_enemy_hero:
                    if not (a_hero in self.advantages):
                        self.advantages[a_hero] = 0
                    else:
                        counter_adv = G.edge[a_hero][an_enemy_hero]["counter_adv"]
                        self.advantages[a_hero] = self.advantages[a_hero] + counter_adv

            for an_allied_hero in self.drafter.allied_hero_selections:
                if a_hero != an_allied_hero:
                    if not (a_hero in self.advantages):
                        self.advantages[a_hero] = 0
                    else:
                        synergy_adv = G.edge[a_hero][an_allied_hero]["synergy_adv"]
                        self.advantages[a_hero] = self.advantages[a_hero] + synergy_adv


def main():
    allies = ["uther", "zagara", "the-butcher"]
    enemies = ["kaelthas", "thrall", "illidan"]
    owned_heroes = ["johanna", "kaelthas", "kerrigan", "kharazim", "leoric", "li-ming",
    "lili", "lt-morales", "lunara", "malfurion", "muradin", "murky", "nazeebo",
    "nova", "raynor", "rehgar", "rexxar", "sgt-hammer", "sonya"]

    drafter = HoTS_Drafter(allies, enemies, owned_heroes)

    for a_hero_name in all_heroes:
        print("{} has a {} % advantage in this situation.".format(a_hero_name, drafter.calculator.advantages[a_hero_name]))

main()
