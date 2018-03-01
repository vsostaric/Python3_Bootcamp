from constants import all_positions
from constants import no_victor
from input_sign import input_sign
from draw_layout import write_out_layout
from draw_layout import write_out_layout_legend
from get_player_input import get_player_input
from ai_player import get_next_move
from check_victory_condition import check_victory_condition
free_positions = all_positions

def game():
    while(True):
        answer = input('Do you want to play a game? (Yes/No) ')
        if answer.lower() == 'no':
            print('Ok, bye then')
            return
        elif answer.lower() == 'yes':
            print('Great, let\'s play!')
            play_game()
        else:
            print('Didn\'t catch that :(')

def play_game():
    player_1_sign, player_2_sign = input_sign()
    player_1_fields = set()
    player_2_fields = set()

    print('Position layout: ')
    write_out_layout_legend()

    while(True):
        write_out_layout(player_1_fields, player_1_sign, player_2_fields, player_2_sign)
        player_1_fields.add(get_player_input())
        player_2_fields.add(get_next_move(player_2_fields, player_1_fields))

        check_state = check_victory_condition(player_1_fields, player_2_fields)
        if(check_state != no_victor):
            print(check_state)
            return
game()
