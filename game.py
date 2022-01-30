import random

INCORRECT_LETTER = 0
INCORRECT_PLACEMENT = 1
CORRECT_LETTER = 2

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
        return [CORRECT_LETTER] * 5 if game_won else self.__evaluate_guess(guess)

    def __evaluate_guess(self, guess: str) -> list:
        ans = self.answer
        result = [None] * 5

        for i, letter in enumerate(guess):
            if ans[i] == letter:
                result[i] = CORRECT_LETTER
                guess = guess[:i] + '_' + guess[i+1:]
                ans = ans[:i] + '_' + ans[i+1:]

        for i, letter in enumerate(guess):
            if letter != '_' and letter in ans:
                result[i] = INCORRECT_PLACEMENT 
                guess = guess[:i] + '_' + guess[i+1:]
                ans[ans.find(letter)] = '_'
                
        if not all(result):
            return list(map(lambda x: INCORRECT_LETTER if x is None else x, result))

    def __save_game(self):
        # TODO Save to DB
        return
