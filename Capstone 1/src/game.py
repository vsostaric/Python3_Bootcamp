import sys

from ai_player import get_next_move
from ai_player import learn
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
from input_who_plays_first import does_human_play_first

from brain import Brain

free_positions = all_positions


def game():

    brain = Brain()

    while True:
        answer = input('Do you want to play a game? (Yes/No) ')
        if answer.lower() == 'no' or answer.lower() == 'n':
            print('Ok, bye then')
            return
        elif answer.lower() == 'yes' or answer.lower() == 'y':
            print('Great, let\'s play!')
            play_game(brain)
        else:
            print('Didn\'t catch that :(')


def play_game(brain):
    player_1_sign, player_2_sign = input_sign()
    player_1_first = does_human_play_first()

    player_1_fields = set()
    player_2_fields = set()

    def play_turn(make_move, player_fields, *args):
        move = make_move(*args)
        player_fields.add(move)
        if check_player_victory(player_fields):
            return 1, move
        return 0, move

    def print_message_and_layout(message):
        print(message)
        write_out_layout(player_1_fields, player_1_sign, player_2_fields, player_2_sign)

    print('Position layout: ')
    write_out_layout_legend()

    moves = []
    if (player_1_first):
        moves.append(-1)
    else:
        moves.append(1)

    while True:

        if (player_1_first):
            write_out_layout(player_1_fields, player_1_sign, player_2_fields, player_2_sign)

            turn_outcome, move = play_turn(get_player_input, player_1_fields, player_1_fields, player_2_fields)
            moves.append(move)

            if turn_outcome == 1:
                print_message_and_layout(message=player_1_victory)
                brain = learn(moves, -1, brain)
                return

            turn_outcome, move = play_turn(get_next_move, player_2_fields, player_2_fields, player_1_fields, brain)
            moves.append(move)

            if turn_outcome == 1:
                print_message_and_layout(message=player_1_loss)
                brain = learn(moves, 1, brain)
                return
        else:
            turn_outcome, move = play_turn(get_next_move, player_2_fields, player_2_fields, player_1_fields, brain)
            moves.append(move)

            if turn_outcome == 1:
                print_message_and_layout(message=player_1_loss)
                brain = learn(moves, 1, brain)
                return

            write_out_layout(player_1_fields, player_1_sign, player_2_fields, player_2_sign)

            turn_outcome, move = play_turn(get_player_input, player_1_fields, player_1_fields, player_2_fields)
            moves.append(move)

            if turn_outcome == 1:
                print_message_and_layout(message=player_1_victory)
                brain = learn(moves, -1, brain)
                return

        if check_draw_condition(player_1_fields, player_2_fields):
            print_message_and_layout(message=draw)
            brain = learn(moves, 0, brain)
            return


def main(args):
    game()


if __name__ == '__main__':
    main(sys.argv)
