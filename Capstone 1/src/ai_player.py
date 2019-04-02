import random

from constants import all_positions
from game_utils import add_non_played_rounds

def get_next_move(ai_positions, opponent_positions, moves, brain):
    possible_moves = _get_possible_moves(ai_positions, opponent_positions)
    if possible_moves.__len__() == 0:
        return

    return _calculate_next_move(possible_moves, moves, brain)


def learn(moves, outcome, brain):
    return brain


def _get_possible_moves(ai_positions, opponent_positions):
    possible_moves = set()
    for i in all_positions:
        if not ai_positions.__contains__(i) and not opponent_positions.__contains__(i):
            possible_moves.add(i)
    return possible_moves


def _calculate_next_move(possible_moves, moves, brain):

    next_move = -1
    next_move_prediction = -1

    for move in possible_moves:
        possible_play = moves
        possible_play.append(move)
        possible_play = add_non_played_rounds(possible_play)

        predictPlay = brain.neural_network.predict(possible_play)
        if next_move_prediction < predictPlay:
            next_move = move

    return next_move
