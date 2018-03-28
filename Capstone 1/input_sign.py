def input_sign():
    while (True):
        player_sign = input('What sign do you choose? (X/O) ')
        if player_sign.lower() == 'x':
            print('Ok, you\'re X')
            return ('X', 'O')
        elif player_sign.lower() == 'o':
            print('Ok, you\'re O')
            return ('O', 'X')
        else:
            print('Didn\'t catch that :(')
