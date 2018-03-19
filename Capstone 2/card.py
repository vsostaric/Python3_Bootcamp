class Card:
    def __init__(self, face, suite) -> None:
        self.face = face
        self.suite = suite

    def __str__(self) -> str:
        return "" + str(self.face) + " " + str(self.suite)
