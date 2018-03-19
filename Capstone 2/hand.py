class Hand:
    def __init__(self):
        self.cards = []

    def getCardValue(self):
        valueSum = 0
        aces = 0
        for card in self.cards:
            value = getValue(card.face)
            if value == 1:
                aces += 1
            else:
                valueSum += value
        for i in range(0, aces):
            if valueSum < 21 and (valueSum + 11) < 21:
                valueSum += 11
            else:
                valueSum += 1
        return valueSum

    def addCard(self, card):
        self.cards.append(card)

    def printOutHand(self):
        for p in self.cards: print(p)

def getValue(face):
    if face == 'A':
        return 1
    try:
        value = int(face)
        return value
    except ValueError:
        return 10
