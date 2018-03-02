import sys
from constants import all_positions
from constants import player_1_victory
from constants import player_1_loss
from constants import draw
from input_sign import input_sign
from draw_layout import write_out_layout
from draw_layout import write_out_layout_legend
from get_player_input import get_player_input
from ai_player import get_next_move
from check_victory_condition import check_player_victory
from check_victory_condition import check_draw_condition
free_positions = all_positions

def game():
    while(True):
        answer = input('Do you want to play a game? (Yes/No) ')
        if answer.lower() == 'no' or answer.lower() == 'n':
            print('Ok, bye then')
            return
        elif answer.lower() == 'yes' or answer.lower() == 'y':
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

        player_1_fields.add(get_player_input(player_1_fields, player_2_fields))
        if(check_player_victory(player_1_fields)):
            print(player_1_victory)
            write_out_layout(player_1_fields, player_1_sign, player_2_fields, player_2_sign)
            return

        player_2_fields.add(get_next_move(player_2_fields, player_1_fields))
        if(check_player_victory(player_2_fields)):
            print(player_1_loss)
            write_out_layout(player_1_fields, player_1_sign, player_2_fields, player_2_sign)
            return

        if(check_draw_condition(player_1_fields, player_2_fields)):
            print(draw)
            write_out_layout(player_1_fields, player_1_sign, player_2_fields, player_2_sign)
            return

def main(args):
    game()

if __name__ == '__main__':
    main(sys.argv)
