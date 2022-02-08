from player import Player


class Human(Player):

    def __init__(self):
        super().__init__()


    def choose_guesture(self):
        print("Select a guesture ")
        count = 0
        for move in self.list_of_guestures:
            print(f'Press {count} to select {move}')
            count += 1
        human_choice = int(input())
        valid = [0,1,2,3,4]
        game_mode = human_choice
        while game_mode not in valid:
            game_mode = input('INVALID RESPONSE! Please select from {human_choice}')
        print(f"please enter a number {human_choice}")
        self.chosen_guesture = self.list_of_guestures[human_choice]
        print(f'{self.chosen_guesture} was selected by the human')

        
    

  

    