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
        print(f"please enter a number {human_choice}")
        self.chosen_guesture = self.list_of_guestures[human_choice]
        print(f'{self.chosen_guesture} was selected by the human')

        
    

    def choose_player_mode(self):
        pass  