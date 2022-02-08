from human import Human
from ai import Ai

# class Game:    old code

#     def __init__(self):
#         self.player = Player()
#         self.Ai = Ai()
class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        super().__init__()


    def run_game(self):
        self.welcome_player()
        self.rules_of_game()
        self.choose_player_mode()
        
    
    def welcome_player(self):
        print("Welcome to the game, the rules are as stated before you. Please enjoy the game")
    
    def rules_of_game (self):
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard. Best 2 out of 3 wins the game!")

    def choose_player_mode(self):
        game_mode = input('Press 1 for singleplayer. Press 2 for multiplayer')
        if game_mode == '1':
            self.player_two = Ai()
        elif game_mode == '2':
            self.player_two = Human()
        print(self.player_two)  
        
        # mode = input("Press 1 for single player. Press 2 for multiplayer")
        # if mode == '1':
        #     self.Ai = Ai()
        # elif mode == '2':
        #     pass
           
            

        

    
    
    def display_winner(self):
        print("Congratulations {} You have won the game!")
