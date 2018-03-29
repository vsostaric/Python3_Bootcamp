import sys
from initialize_game import createDeck
from initialize_game import shuffleDeck
from card import Card
from hand import Hand
from get_player_move import get_player_move


def game():
    while (True):
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
    deck = shuffleDeck(createDeck())
    deck_position = 0

    def play(p_opponent_value, p_deck_position, get_move):
        hand = Hand()
        card_values = hand.getCardValue()
        while True:
            hand.printOutHand()
            move = get_move(card_values, p_opponent_value)
            if move == 2:
                return p_deck_position, 0, card_values
            if move == 1:
                card = deck[p_deck_position]
                p_deck_position += 1
                hand.addCard(card)

            card_values = hand.getCardValue()

            if card_values > 21:
                hand.printOutHand()
                return p_deck_position, -1, card_values

            if 21 > card_values > p_opponent_value:
                hand.printOutHand()

                return p_deck_position, 1, card_values

    deck_position, result, values = play(1000, deck_position, get_player_move)

    print("Hand value: " + str(values))
    if result == -1:
        print("Bust! You lose!")
        return

    print("Dealer's turn")

    def get_dealer_move(value, opponent_value):
        if 21 >= value >= opponent_value:
            return 2
        return 1

    deck_position, result, values = play(values, deck_position, get_dealer_move)

    print("Hand value: " + str(values))
    if result == -1:
        print("Dealer Busts! You win!")
    elif result == 1:
        print("Dealer wins!")
    elif result == 0:
        print("Push!")


def main(args):
    game()


if __name__ == '__main__':
    main(sys.argv)
