
from game.actor import Actor


class Director:
    
    def __init__(self):
        self.state=True
        self.identification_player=""
        self.randome=Actor()
        self.choice=""
        self.lifes=3
        
        
    
    def ask_user_input(self):
        """ Ask the user choose one: Rock, Paper or Scissors"""
        r_p_s=input("Rock, Paper or Scissors?: ").lower()
        self.identification_player=r_p_s
        self.choice=self.randome.random_rps()

    def rock_paper_sissor(self):
        """ Check who is winning"""   

        if self.identification_player== "scissors" and self.choice == "rock":
            self.lifes -= 1
        elif self.identification_player== "rock" and self.choice == "paper":
            self.lifes -= 1
        elif self.identification_player== "paper" and self.choice == "scissors":
            self.lifes -= 1

    def is_alive(self):
        """ Check if the users is alive, if lost the 3 lives the game end"""
        if self.lifes == 0:
            self.state=False
            print("You lost all your lifes, you lost the game")


    def show_outputs(self):
            """Show the outputs """
            print("")
            print(f"You choose {self.identification_player}")
            print(f"The machine choose {self.choice}")
            print(f"Your lifes are {self.lifes}")
            print("")

        
    def start_game(self):
        """Stay the game running """
        while self.state:
            self.ask_user_input()
            self.rock_paper_sissor()
            self.is_alive()
            self.show_outputs()

            
        




            

