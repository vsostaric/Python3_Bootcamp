from constants import player_1_victory
from constants import player_1_loss
from constants import no_victor

def check_victory_condition(player_1_fields, player_2_fields):
    if(check_player_victory(player_1_fields)):
        return player_1_victory
    elif(check_player_victory(player_2_fields)):
        return player_1_loss
    return no_victor

def check_player_victory(player_fields):
    if(player_fields.__len__() < 3):
        return False;
    elif(player_fields.issubset({1,2,3})):
        return True
    elif(player_fields.issubset({4,5,6})):
        return True
    elif(player_fields.issubset({7,8,9})):
        return True
    elif(player_fields.issubset({1,4,7})):
        return True
    elif(player_fields.issubset({2,5,8})):
        return True
    elif(player_fields.issubset({3,6,9})):
        return True
    elif(player_fields.issubset({1,5,9})):
        return True
    elif(player_fields.issubset({3,5,7})):
        return True
    return False
