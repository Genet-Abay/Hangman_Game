import re
class Hangman:
    '''
    A class defines a hangman game. The class contains all the attribute and functions to play the game
    '''
    def __init__(self, possible_word_index):
        '''
        class constructure holds and initializes all the attributes
        '''
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = self.possible_words[possible_word_index]
        self.len_possible_words = len(self.word_to_find)

        
        self.well_guessed_letters = ['_']*self.len_possible_words
        self.bad_guessed_letters = []
        self.turn_count =0
        self.error_count =0
        self.lives = self.len_possible_words

    def play(self):
        '''
        function which holds the main process to play the game. it is iteratevly called by the start function antil the game is alive
        '''
        self.turn_count+=1
        letter_guessed = input("guess a letter: ")
        if len(letter_guessed) == 1 and letter_guessed.isalpha():
            if letter_guessed in self.word_to_find:
                indexes = [x.start() for x in re.finditer(letter_guessed, self.word_to_find)]
                for i in indexes:
                    self.well_guessed_letters[i] = letter_guessed
            else:
                self.bad_guessed_letters.append(letter_guessed)
                self.error_count+=1
                self.lives-=1
        else:
            if letter_guessed == "exit":
                print("You quite the game.")
                quit()
            else:
                print("Input sould be a single alphabet")

    def game_over(self):
        '''
        called when the game is endded, that means when the life is reached 0.
        '''
        print("Game Over! ")
        quit()

    
    def well_played(self):
        '''
        only called when the player get all letters in the given word.
        '''
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!.")

    def start_game(self):
        '''
        this functions starts the game and controlls the result gained by the player and quit the game if life is 0.
        '''        
        while self.lives > 0 and self.turn_count < self.len_possible_words:
            self.play()           

        if len(self.well_guessed_letters) == len(self.word_to_find):
            self.well_played()
        
        print(f"well_guessed_letters: {self.well_guessed_letters} , Bad guessed letters: {self.bad_guessed_letters}, \n lif: {self.lives}, Error count: {self.error_count}, Turn: {self.turn_count}")

        self.game_over()
        

