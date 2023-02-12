import random

# CLASS #
class Hangman:
    guesses = set()
    
    def __init__(self, words, attempts):
        self.words = words
        self.attempts = attempts
        self.ans = random.choice(words)
        
    def start(self):
        print(f'H A N G M A N  # {self.attempts} attempts', end='\n\n')
        
        while self.attempts:
            hidden = ''.join(let if let in self.guesses else '-' for let in self.ans)
            print(hidden)
            
            guess = input(f'Input a letter: ')
            if guess not in self.ans:
                print("That letter doesn't appear in the word.")
                
            self.guesses.add(guess)
            self.attempts -= 1
            print(f'  # {self.attempts} attempts', end='\n\n')
        
        print('Thanks for playing!')
            
        
# MAIN #
config = {
    'words': ['python', 'java', 'swift', 'javascript'],
    'attempts': 8
}
game = Hangman(**config)
game.start()