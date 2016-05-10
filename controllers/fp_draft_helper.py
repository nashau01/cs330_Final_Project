


# Keys are hero names as a string
# Values are a list of dictionaries
    # 1) With
        # Keys are
all_heroes = {}

#
# - or -  Is this fundamentally a graph theory application? Vertices: Heroes, Edges: counter/synergy weights
#


class DraftInput:
    def __init__(self):
        self.allied_hero_selections = []
        self.enemy_hero_selections = []
        self.user_hero_preferences = {}


class OptimalSelectionCalculator:
    def __init__(self, draft_input):
        self.draft_input = draft_input

        # A dictionary :
        self.counter_weights = {}
        self.synergy_weights = {}

    def findOptimalSelections(self):
        self.counter_weights = findCounterAdvantages()

        self.synergy_weights = findSynergyAdvantages()

    def findCounterWeights(self):
        for a_hero in all_heroes:
            for an_enemy_hero in self.draft_input.enemy_hero_selections:
                self.counter_weights[a_hero.name] = all





