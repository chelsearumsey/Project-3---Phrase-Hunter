# Create your Game class logic in here.
from phrase import Phrase
import random

class Game():
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def start(self):
        self.welcome()
        while self.missed < 5:
            print(f"""Number missed: {self.missed}
            """)
            self.active_phrase.display(self.guesses)
            self.user_guess = self.get_guess()
            self.guesses.append(self.user_guess)
            if not self.active_phrase.check_guess(self.user_guess):
                self.missed += 1
            else:
                continue
            

    def welcome(self):
        print('''
        
        ====================================================================================\n
          Hey there heeyyy movie buff! Are you ready to guess some epic cinematic quotes?!\n
        ====================================================================================
        
        
        ''')

    def create_phrases(self): 
        phrases = [Phrase("Riddles in the dark"), Phrase("The wand chooses the wizard"), 
                        Phrase("The bog of eternal stench"), Phrase("Anybody want a peanut"), 
                        Phrase("You will be assimilated resistance is futile")]
        return phrases
    
    def get_random_phrase(self):
        random_phrase = random.choice(self.phrases)
        return random_phrase

    def get_guess(self):
        return input("""
        
Be our guest and take a guess! Enter a letter: """)
    

