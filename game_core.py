import random as r
import time as t

class Game:
    difficulty = False # 1-3
    max_range = False
    secret_number = False
    active = True
    score = 100

    @staticmethod
    def user_answer(cls, answer):
        if answer == cls.secret_number:
            print(f'\nYou won with {Game.score} points!')
            Game.replay(Game)

        else:
            Game.score -= 10*cls.difficulty
            print(f'\nWrong! You have now {Game.score} points.')

            if Game.score < 1:
                print('You lost!')
                Game.replay(Game)

    @staticmethod
    def replay(cls):
        while True:
            answer = input('\nWould you like to play again? [Y/N]\n')
            if answer == 'Y':
                print('\nNew game starting...\n')
                cls.score = 100

                t.sleep(1)
                break

            elif answer == 'N':
                print('\nThanks for playing!\n')
                Game.active = False
                break

            else:
                print('Please give a valid answer!\n')

    @staticmethod
    def clue_maker(cls):
        clue_option = r.randint(1, 4)

        if clue_option == 1:
            clue_number = r.randint(1, cls.max_range)
            print(f'\nThe number divided by {clue_number} is equal to {cls.secret_number/clue_number}')

        elif clue_option == 2:
            clue_number = r.randint(1, cls.max_range)
            print(f'\nThe number multiplied by {clue_number} is equal to {cls.secret_number*clue_number}')

        elif clue_option == 3:
            clue_number = r.randint(1, cls.max_range)
            print(f'\nThe number added to {clue_number} is equal to {cls.secret_number + clue_number}')

        elif clue_option == 4:
            clue_number = r.randint(1, cls.max_range)
            print(f'\nThe number subtracted by {clue_number} is equal to {cls.secret_number - clue_number}')

    @staticmethod
    def difficulty_selector(cls):
        print('Please, choose the difficulty:')
        while True:
            cls.difficulty = int(input('1 -> Easy\n2 -> Medium\n3 -> Dificult\n'))
            if cls.difficulty == 1:
                Game.easy_config(Game, 10)
                break

            elif cls.difficulty == 2:
                Game.easy_config(Game, 50)
                break

            elif cls.difficulty == 3:
                Game.easy_config(Game, 100)
                break

            else:
                print('Please select a valid difficulty level!\n')

    @staticmethod
    def easy_config(cls, number):
        cls.max_range = number
        cls.secret_number = r.randint(1, cls.max_range)
