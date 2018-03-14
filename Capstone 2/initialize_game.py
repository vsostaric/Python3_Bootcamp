from card import Card

suites = {"D", "C", "H", "S"}
faces = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}


def getValue(face):
    try:
        value = int(face)
        return value
    except ValueError:
        return 10


def createDeck():
    cards = []
    for suite in suites:
        for face in faces:
            cards.append(Card(face, suite, getValue(face)))
    return cards
