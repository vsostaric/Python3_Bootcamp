from constants import all_positions


def get_player_input(player_positions, opponent_positions):
    possible_moves = list(filter(
        lambda position: not player_positions.__contains__(position) and not opponent_positions.__contains__(position),
        all_positions))
    print('Valid positions: ' + str(possible_moves))
    while (True):
        player_input = input('Enter position: ')
        if (is_number(player_input) and possible_moves.__contains__(int(player_input))):
            print('Position entered')
            return int(player_input)
        print('Invalid position, enter ' + str(possible_moves))


def is_number(input):
    try:
        int(input)
        return True
    except ValueError:
        return False
