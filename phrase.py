# Create your Phrase class logic here.
class Phrase():
    
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def __str__(self):
        return self.phrase

    def display(self, guesses):
            for letter in self.phrase:
                if letter in guesses:
                    print(f'{letter}', end=" ")
                else:
                    print(f'_', end=" ")