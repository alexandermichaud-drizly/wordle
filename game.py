import random

INCORRECT_LETTER = 0
CORRECT_LETTER_WRONG_PLACE = 1
CORRECT_LETTER_CORRECT_PLACE = 2

class Game:
    def __init__(self, word_bank: list) -> None:
        self.answer = random.choice(word_bank)
        self.guessed_words = [None] * 6
        self.guesses = 0

    def submit_guess(self, guess: str):
        self.guesses += 1
        self.guessed_words.append(guess)
        game_won = self.answer == guess
        if game_won or self.guesses == 6:
            self.__save_game()
        return [CORRECT_LETTER_CORRECT_PLACE] * 5 if game_won else self.__evaluate_guess(guess)

    def __evaluate_guess(self, guess: str) -> list:
        output = []
        for i, letter in enumerate(guess):
            if self.answer[0] == letter:
                output.append(CORRECT_LETTER_CORRECT_PLACE)
            elif letter in self.answer:
                output.append(CORRECT_LETTER_WRONG_PLACE)
            else:
                output.append(INCORRECT_LETTER)
        return output

    def __save_game(self):
        return