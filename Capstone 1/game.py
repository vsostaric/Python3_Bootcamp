import sys

from ai_player import get_next_move
from check_victory_condition import check_draw_condition
from check_victory_condition import check_player_victory
from constants import all_positions
from constants import draw
from constants import player_1_loss
from constants import player_1_victory
from draw_layout import write_out_layout
from draw_layout import write_out_layout_legend
from get_player_input import get_player_input
from input_sign import input_sign

free_positions = all_positions


def game():
    while True:
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

    def play_turn(player_fields, opponent_fields, make_move):
        player_fields.add(make_move(player_fields, opponent_fields))
        if check_player_victory(player_fields):
            return 1
        return 0

    def print_message_and_layout(message):
        print(message)
        write_out_layout(player_1_fields, player_1_sign, player_2_fields, player_2_sign)

    print('Position layout: ')
    write_out_layout_legend()

    while True:
        write_out_layout(player_1_fields, player_1_sign, player_2_fields, player_2_sign)

        turn_outcome = play_turn(player_1_fields, player_2_fields, get_player_input)
        if turn_outcome == 1:
            print_message_and_layout(message=player_1_victory)
            return

        turn_outcome = play_turn(player_2_fields, player_1_fields, get_next_move)
        if turn_outcome == 1:
            print_message_and_layout(message=player_1_loss)
            return

        if check_draw_condition(player_1_fields, player_2_fields):
            print_message_and_layout(message=draw)
            return


def main(args):
    game()


if __name__ == '__main__':
    main(sys.argv)
