possible_moves = {1, 2}
move_legend = '1 - Hit; 2 - Stay'


def get_player_move(value, opponent_value):
    while (True):
        print(move_legend)
        player_input = input('Chose move: ')
        if (is_number(player_input) and possible_moves.__contains__(int(player_input))):
            return int(player_input)
        print('Invalid move')


def is_number(input):
    try:
        int(input)
        return True
    except ValueError:
        return False
