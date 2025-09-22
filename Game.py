import random
from card import Card
from Player import Player

class Game:
    def __init__(self, players, skat):
        self.players = players                  # List of Player objects
        self.skat = skat                        # The 2 cards left after dealing (skat)
        self.middle = []                        # Cards played in the current trick
        self.played_cards = []                  # All played cards

        self.big_guy_points = 0
        self.small_guy_points = 0

        self.total_points_left = self.calculate_total_points_left()
        self.total_points_in_hands = self.calculate_points_in_hands()
        self.points_in_skat = self.calculate_points_in_skat()
        self.points_in_hand = [self.calculate_points_in_hand(p) for p in players]
        self.cards_in_hand = [len(p.hand) for p in players]
        self.points_not_in_hand = self.calculate_points_not_in_hand()

        self.turn = 0                           # Index of whose turn it is

    def calculate_total_points_left(self):
        all_cards = [card for p in self.players for card in p.hand] + self.skat + self.middle
        return sum(card.points for card in all_cards)

    def calculate_points_in_hands(self):
        return sum(card.points for p in self.players for card in p.hand)

    def calculate_points_in_skat(self):
        return sum(card.points for card in self.skat)

    def calculate_points_in_hand(self, player):
        return sum(card.points for card in player.hand)

    def calculate_points_not_in_hand(self):
        points_in_hands = self.calculate_points_in_hands()
        points_in_skat = self.calculate_points_in_skat()
        points_played = sum(card.points for card in self.played_cards)
        total_points = 120  # Zole deck total points
        return total_points - points_in_hands

    def next_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

    def play_card(self, player_idx, card):
        player = self.players[player_idx]
        player.hand.remove(card)
        self.middle.append(card)
        if len(self.middle) == 3:
            self.played_cards.extend(self.middle)
            self.middle = []  # Clear middle after trick

    @staticmethod
    def create_deck():
        points_map = {7: 0, 8: 0, 9: 0, 10: 4, 11: 10, 12: 11, 13: 2, 14: 3}
        deck = []
        for suit in range(1, 5):
            if suit == 4:  # Diamonds
                values = range(7, 15)
            else:
                values = range(9, 15)
            for value in values:
                points = points_map.get(value, 0)
                deck.append(Card(points, suit, value))
        return deck

    @staticmethod
    def deal_cards(deck):
        random.shuffle(deck)
        players = [Player(), Player(), Player()]
        for i in range(8):
            for p in range(3):
                players[p].hand.append(deck.pop())
        skat = [deck.pop(), deck.pop()]
        return players, skat