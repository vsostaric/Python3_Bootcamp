class Hand:
    def __init__(self):
        self.cards = []

    def get_card_value(self):
        value_sum = 0
        aces = 0
        for card in self.cards:
            value = get_card_value(card.face)
            if value == 1:
                aces += 1
            else:
                value_sum += value
        for i in range(0, aces):
            if value_sum < 21 and (value_sum + 11) <= 21:
                value_sum += 11
            else:
                value_sum += 1
        return value_sum

    def add_card(self, card):
        self.cards.append(card)

    def print_out_hand(self):
        print("Hand: ")
        for p in self.cards: print(p)


def get_card_value(face):
    if face == 'A':
        return 1
    try:
        value = int(face)
        return value
    except ValueError:
        return 10
