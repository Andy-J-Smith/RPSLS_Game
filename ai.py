import random
from player import Player


class Ai(Player):

    def __init__(self):
        super().__init__()
        self.name = "Robot"


    def choose_guesture(self):
        cpu_gest = random.choice(self.list_of_guestures)
        self.chosen_guesture = cpu_gest
        print(f'{self.name} has picked {self.chosen_guesture}')
        

