from constants import all_positions
import random

def get_next_move(ai_positions, opponent_positions):

    possible_moves = set()
    for i in all_positions:
        if not ai_positions.__contains__(i) and not opponent_positions.__contains__(i):
            possible_moves.add(i)
    if(possible_moves.__len__() == 0):
        return
    return random.sample(possible_moves, 1)[0]
