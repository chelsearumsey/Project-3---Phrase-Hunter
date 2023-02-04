# Create your Game class logic in here.
from phrase import Phrase
import random

class Game():
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = None
        self.guesses = [" "]

    def create_phrases(self):
        random_phrase = [Phrase("Riddles in the dark"), Phrase("The wand chooses the wizard"), 
                        Phrase("The bog of eternal stench"), Phrase("Anybody want a peanut"), 
                        Phrase("You will be assimilated resistance is futile")]
        phrase = random.choice(random_phrase)
        return phrase

    

