from card import Card
from Player import Player
from Game import Game
import random



if __name__ == "__main__":
    game = Game([Player(), Player(), Player()])
    print(f"Player 1 cards: {game.players[0].hand}")
    print(f"Table cards: {game.skat[0]}")
    game.legal_cards(game.skat,game.players[0].hand)
    print("Legal cards for Player 1:")
    for card in game.players[0].hand:
        if card.legal:
            print(card)

            