
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

    def check_guess(self, guess):
        self.guess = guess
        if guess in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses):
        for letter in self.phrase:
            while letter not in guesses:
                return False
            continue

            

