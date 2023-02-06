
from phrase import Phrase
import random
import string

class Game():
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"""Number missed: {self.missed}
            """)
            self.active_phrase.display(self.guesses)
            self.user_guess = self.get_guess().lower()
            self.guesses.append(self.user_guess)
            if not self.active_phrase.check_guess(self.user_guess):
                while True:
                    try:
                        if self.user_guess not in list(string.ascii_lowercase):
                            print("Oops! Make sure to enter a single letter only!")
                    except ValueError:
                        self.user_guess = input("Guess again!  ")
                    else:
                        break
                self.missed += 1
            else:
                continue
        self.game_over()
            
            

    def welcome(self):
        print('''
        
        ====================================================================================\n
        Hey there heeyyy movie buff! Are you ready to guess some epic cinematic quotes?!\n
        ====================================================================================
        
        
        ''')

    def create_phrases(self): 
        phrases = [Phrase("Riddles in the dark"), Phrase("The wand chooses the wizard"), 
                    Phrase("The bog of eternal stench"), Phrase("Anybody want a peanut"), 
                    Phrase("Resistance is futile")]
        return phrases
    
    def get_random_phrase(self):
        random_phrase = random.choice(self.phrases)
        return random_phrase

    def get_guess(self):
        return input("""
        
Be our guest and take a guess! Enter a letter: """)

    def game_over(self):
        if self.missed == 5:
            print("Too bad! You coulda been a contender!")
        else:
            print('You won!!! "Heroes get remembered but legends never die."') 
        while True:  
            play_again = input("Would you like to guess another movie quote? (Enter 'yes' or 'no')  ").lower()

            if play_again == "yes": 
                self.play_again()
                self.start()    
                break
            elif play_again =="no": 
                print("Thanks for playing! See you on the flip side!") 
                break
            else:
                print("Please type 'yes' or 'no' only.")

    def play_again(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
                

     
            

    

