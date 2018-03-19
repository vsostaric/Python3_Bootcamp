import random
from constants import suites
from constants import faces
from card import Card


def createDeck():
    deck = []
    for suite in suites:
        for face in faces:
            deck.append(Card(face, suite))
    return deck


def shuffleDeck(deck):
    random_list = random.sample(range(len(deck)), len(deck))
    shuffled_deck = []
    for i in random_list:
        shuffled_deck.append(deck[i])
    return shuffled_deck
