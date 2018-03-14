class Card:
    def __init__(self, face, suite, value) -> None:
        self.face = face
        self.suite = suite
        self.value = value

    def __str__(self) -> str:
        return "" + str(self.face) + " " + str(self.suite) + " " + str(self.value)
