def does_human_play_first():
    while (True):
        player_choice = input('Do you want to play first? (Yes/No)')
        if player_choice.lower() == 'no' or player_choice.lower() == 'n':
            print('Ok, I\'ll play first')
            return False
        if player_choice.lower() == 'yes' or player_choice.lower() == 'y':
            print('Ok, you\'ll play first')
            return True
        else:
            print('Didn\'t catch that :(')
