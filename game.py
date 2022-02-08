from human import Human
from ai import Ai

# test to make sure human can make choice 
# start writing the endt of turn check to see who won

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
        self.player_one.choose_guesture()
        self.player_two.choose_guesture()
        self.play_round()
    
    def welcome_player(self):
        print("Welcome to the game, the rules are as stated before you. Please enjoy the game")
    
    def rules_of_game (self):
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard. Best 2 out of 3 wins the game!")

    def choose_player_mode(self):
        valid = ('1','2')
        game_mode = input('Press 1 for singleplayer. Press 2 for multiplayer')
        while game_mode not in valid:
            game_mode = input('INVALID RESPONSE! Press 1 for singleplayer. Press 2 for multiplayer')
        if game_mode == '1':
            self.player_two = Ai()
        elif game_mode == '2':
            self.player_two = Human()
        print(self.player_two.name)  
        
        # mode = input("Press 1 for single player. Press 2 for multiplayer")
        # if mode == '1':
        #     self.Ai = Ai()
        # elif mode == '2':
        #     pass
           
    def play_round(self):     # check if tie, check if player one wins else player 2 wins
        
        self.player_one.choose_guesture()
        self.player_two.choose_guesture()
        if self.player_one.chosen_guesture == self.player_two.chosen_guesture:
            print("its a a tie")
        elif self.player_one.chosen_guesture == "Rock" and self.player_two.chosen_guesture == "Scissors" or self.player_two.chosen_guesture == "Lizard":
            print(f'{self.player_one.name} player one wins round')
            self.player_one.wins += 1
        elif self.player_one.chosen_guesture == "Scissors" and self.player_two.chosen_guesture == "Paper" or self.player_two.chosen_guesture == "Lizard":
            print(f'{self.player_one.name} player one wins round')
            self.player_one.wins += 1
        elif self.player_one.chosen_guesture == "Paper" and self.player_two.chosen_guesture == "Rock" or self.player_two.chosen_guesture == "Spock":
            print(f'{self.player_one.name} player one wins round')
            self.player_one.wins += 1
        elif self.player_one.chosen_guesture == "Lizard" and self.player_two.chosen_guesture == "Spock" or self.player_two.chosen_guesture == "Paper":
            print(f'{self.player_one.name} player one wins round')
            self.player_one.wins += 1
        elif self.player_one.chosen_guesture == "Spock" and self.player_two.chosen_guesture == "Scissors" or self.player_two.chosen_guesture == "Rock":
            print(f'{self.player_one.name} player one wins round')
            self.player_one.wins += 1
        else:
            print(f'{self.player_two.name} player two wins round')
            self.player_two.wins += 1
        print("starting new round")
    
    
    def display_winner(self):
        print("Congratulations {} You have won the game!")
        pass
