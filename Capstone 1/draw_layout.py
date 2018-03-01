from constants import all_positions
from constants import layout

def write_out_layout(player_1_fields, player_1_sign, player_2_fields, player_2_sign):
    signs = list(map(lambda position:determine_sign(position, player_1_fields, player_1_sign, player_2_fields, player_2_sign), all_positions))
    print(layout.format(d=signs));

def write_out_layout_legend():
    print(layout.format(d=all_positions));

def determine_sign(position, player_1_fields, player_1_sign, player_2_fields, player_2_sign):
    if(player_1_fields.__contains__(position)):
        return player_1_sign
    elif(player_2_fields.__contains__(position)):
        return player_2_sign
    return ' '
