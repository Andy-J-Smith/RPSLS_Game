import random
from player import Player


class Ai(Player):

    def __init__(self):
        self.name = ("")
        # super().__init__()


    def choose_guesture(self):
        cpu_gest = random.choice(self.list_of_guestures)
        return super().choose_guesture()
        

