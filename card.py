class Card:
    def __init__(self, points: int, suit: int, value: int):
        self.points = points    # Points of the card
        self.suit = suit        # 1=Clubs, 2=Spades, 3=Hearts, 4=Diamonds
        self.value = value      # 7-14 (Ace=14, King=13, Queen=12, Jack=11)
        self.legal = True       # Placeholder for legality check

    def __repr__(self):
        suit_names = {1: "Clubs", 2: "Spades", 3: "Hearts", 4: "Diamonds"}
        value_names = {13: "Jack", 14: "Queen", 10: "King",11: "Ten", 12: "Ace"}
        name = value_names.get(self.value, str(self.value))
        return f"{name} of {suit_names[self.suit]} (Points: {self.points})"