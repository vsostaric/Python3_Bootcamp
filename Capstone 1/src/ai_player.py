import random

from constants import all_positions


def get_next_move(ai_positions, opponent_positions, brain):
    possible_moves = _get_possible_moves(ai_positions, opponent_positions)
    if possible_moves.__len__() == 0:
        return

    return _calculate_next_move(possible_moves, ai_positions, opponent_positions, brain)


def learn(moves, outcome, brain):
    return brain


def _get_possible_moves(ai_positions, opponent_positions):
    possible_moves = set()
    for i in all_positions:
        if not ai_positions.__contains__(i) and not opponent_positions.__contains__(i):
            possible_moves.add(i)
    return possible_moves


def _calculate_next_move(possible_moves, ai_positions, opponent_positions, brain):
    return random.sample(possible_moves, 1)[0]
