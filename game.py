from typing_extensions import Self
from player import Player
from ai import Ai

class Game:

    def __init__(self):
        self.player = Player()
        self.Ai = Ai()


    def run_game(self):
        self.welcome_player()
        self.rules_of_game()
        self.choose_player_mode()
        
    
    def welcome_player(self):
        print("Welcome to the game, the rules are as stated before you. Please enjoy the game")
    
    def rules_of_game (self):
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard. Best 2 out of 3 wins the game!")

    def choose_player_mode(mode):
        
        mode = input("Press 1 for single player. Press 2 for multiplayer")
        if mode == '1':
            self.Ai = Ai()

            

        

    
    
    def display_winner(self):
        print("Congratulations {} You have won the game!")
