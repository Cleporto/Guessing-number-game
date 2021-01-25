import time as t
from game_core import *

Game.difficulty_selector(Game)
t.sleep(1)

while Game.active == True:
    Game.clue_maker(Game)
    Game.user_answer(Game, int(input('Please write the answer!\n')))
