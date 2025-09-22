from card import Card
from Player import Player
import random

def create_deck():
    # Zole deck: 7-Ace for each suit, total 28 cards
    points_map = {7: 0, 8: 0, 9: 0, 10: 10, 11: 2, 12: 3, 13: 4, 14: 11}
    deck = []
    for suit in range(1, 5):
        for value in range(7, 15):
            points = points_map[value]
            deck.append(Card(points, suit, value))
    return deck

def deal_cards(deck):
    random.shuffle(deck)
    players = [Player(), Player(), Player()]
    for i in range(8):
        for p in range(3):
            players[p].hand.append(deck.pop())
    table_cards = [deck.pop(), deck.pop()]
    return players, table_cards

if __name__ == "__main__":
    deck = create_deck()
    players, table_cards = deal_cards(deck)
    for idx, player in enumerate(players):
        print(f"Player {idx+1} cards: {player.hand}")
    print(f"Table cards: {table_cards}")