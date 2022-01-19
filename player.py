import math
import random

class Player:
    def _init_(self, letter):
        #letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def _init_(self, letter):
        return super()._init_(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square, try again (0-8')
        return val