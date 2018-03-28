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
    deckPosition = 0

    playerHand = Hand()
    cardValues = playerHand.getCardValue()

    while (True):
        playerHand.printOutHand()
        print("Hand value: " + str(cardValues))
        playerMove = get_player_move()
        if (playerMove == 2):
            break
        if (playerMove == 1):
            card = deck[deckPosition]
            deckPosition += 1
            playerHand.addCard(card)

        cardValues = playerHand.getCardValue()

        if cardValues > 21:
            playerHand.printOutHand()
            print("Hand value: " + str(cardValues))
            print("Bust! You lose!")
            return

    print("Dealer's turn")

    dealerHand = Hand()
    dealerCardValues = dealerHand.getCardValue()

    while (True):
        dealerHand.printOutHand()
        print("Hand value: " + str(dealerCardValues))

        card = deck[deckPosition]
        deckPosition += 1
        dealerHand.addCard(card)

        dealerCardValues = dealerHand.getCardValue()

        if dealerCardValues > 21:
            dealerHand.printOutHand()
            print("Hand value: " + str(dealerCardValues))
            print("Dealer Busts! You win!")
            return

        if dealerCardValues > cardValues:
            dealerHand.printOutHand()
            print("Hand value: " + str(dealerCardValues))
            print("Dealer wins!")
            return

    return


def main(args):
    game()


if __name__ == '__main__':
    main(sys.argv)
