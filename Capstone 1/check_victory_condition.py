from constants import player_1_victory
from constants import player_1_loss
from constants import draw
from constants import all_positions

num_of_positions = all_positions.__len__()


def check_player_victory(player_fields):
    if (player_fields.__len__() < 3):
        return False;
    elif ({1, 2, 3}.issubset(player_fields)):
        return True
    elif ({4, 5, 6}.issubset(player_fields)):
        return True
    elif ({7, 8, 9}.issubset(player_fields)):
        return True
    elif ({1, 4, 7}.issubset(player_fields)):
        return True
    elif ({2, 5, 8}.issubset(player_fields)):
        return True
    elif ({3, 6, 9}.issubset(player_fields)):
        return True
    elif ({1, 5, 9}.issubset(player_fields)):
        return True
    elif ({3, 5, 7}.issubset(player_fields)):
        return True
    return False


def check_draw_condition(player_1_fields, player_2_fields):
    if ((player_1_fields.__len__() + player_2_fields.__len__()) >= num_of_positions):
        return True
    return False
