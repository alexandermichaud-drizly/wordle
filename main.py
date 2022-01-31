from game import Game
from player import Player
from word_bank import WORD_BANK

if __name__ == "__main__":
    game = Game(WORD_BANK)
    player = Player(WORD_BANK)
    player.play()
    