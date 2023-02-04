# Create your Phrase class logic here.
class Phrase():
    
    def __init__(self, phrase):
        self.phrase = phrase

    def __str__(self):
        return self.phrase.lower()