

from random import random


class Player:

    def __init__(self):
        self.name = ''
        self.wins = 0
        self.chose_guesture = ''
        self.list_of_guestures = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]


    def choose_guesture(self):
        self.list_of_guestures = self.list_of_guestures

    def choose_player_mode(self):
        pass