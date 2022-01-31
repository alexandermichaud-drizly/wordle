from game import Game

class Player:
    def __init__(self, word_bank: list, config: dict = {}) -> None:
        self.config = config
        self.word_bank = word_bank
        self.guesses = []

    def play(self, game: Game) -> None:
        game_won = False
        while not game_won or game.guesses < 6:
            outcome = self.guess(game)
            self.guesses.append(outcome)
            if all(list(map(lambda k,v: v == Game.CORRECT_LETTER, outcome))):
                game_won = True

    def guess(self, game) -> dict:
        guess = self.__think()
        guess_evaluated = game.submit_guess(guess)
        return [{ x: guess_evaluated[i]} for i, x in enumerate(guess)]

    def __think(self):
        return 'think'