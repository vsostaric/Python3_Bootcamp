from constants import all_positions

def get_player_input():
    print('Valid positions: ' + str(all_positions))
    while(True):
        player_input = input('Enter position: ')
        if(is_number(player_input) and all_positions.__contains__(int(player_input))):
            print('Position entered')
            return int(player_input)
        print('Invalid position, enter ' + str(all_positions))

def is_number(input):
    try:
        int(input)
        return True
    except ValueError:
        return False
