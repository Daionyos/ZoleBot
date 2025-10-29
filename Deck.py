from SuitEnum import Suit
from Card import Card
from RankEnum import Rank

class Deck:
    @staticmethod
    def get_all_cards():
        all_cards = []
        for rank in [Rank.ACE, Rank.JACK, Rank.KING, Rank.NINE, Rank.QUEEN, Rank.TEN]:
            for suit in [Suit.CLUBS, Suit.DIAMONDS, Suit.HEARTS, Suit.SPADES]:
                all_cards.append(Card(rank, suit))

        all_cards.append(Card(Rank.SEVEN, Suit.DIAMONDS))
        all_cards.append(Card(Rank.EIGHT, Suit.DIAMONDS))
        return all_cards
    
    @staticmethod
    def get_trump_cards():
        return [
            Card(Rank.QUEEN, Suit.CLUBS), Card(Rank.QUEEN, Suit.SPADES), Card(Rank.QUEEN, Suit.HEARTS), Card(Rank.QUEEN, Suit.DIAMONDS),
            Card(Rank.JACK, Suit.CLUBS), Card(Rank.JACK, Suit.SPADES), Card(Rank.JACK, Suit.HEARTS), Card(Rank.JACK, Suit.DIAMONDS),
            Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.TEN, Suit.DIAMONDS), Card(Rank.KING, Suit.DIAMONDS), Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.EIGHT, Suit.DIAMONDS), Card(Rank.SEVEN, Suit.DIAMONDS),
                ]

    @staticmethod
    def is_trump_card(card):
        return card in Deck.get_trump_cards()

    @staticmethod
    def get_suit_cards(suit:Suit):
        return [Card(Rank.ACE, suit), Card(Rank.TEN, suit), Card(Rank.KING, suit), Card(Rank.NINE, suit)]

    @staticmethod
    def get_legal_cards(hand, middleCards:list[Card]):
        if(len(middleCards)==0):
            return hand
        else:
            #legal cards->
            #1)if played card is trump card -> set all trump cards as legal -> if no trump cards then all cards legal
            #2) else what suit is the card -> set all non-trump cards of that suit to legal-> if there are none then all cards legal
            middle_card = middleCards[0]
            if(Deck.is_trump_card(middle_card)==True):
                hand_trump_cards = list(set(hand).intersection(set(Deck.get_trump_cards())))
                if(len(hand_trump_cards)==0):
                    return hand
                else:
                    return hand_trump_cards
            else:
                playable_cards=list(set(hand).intersection(set(Deck.get_suit_cards(middle_card.suit))))
                if(len(playable_cards)!=0):
                    return playable_cards
                else:
                    return hand



hand = [
            Card(Rank.QUEEN, Suit.CLUBS), Card(Rank.QUEEN, Suit.SPADES), Card(Rank.QUEEN, Suit.HEARTS), Card(Rank.QUEEN, Suit.DIAMONDS),
            Card(Rank.KING, Suit.CLUBS), Card(Rank.JACK, Suit.SPADES), Card(Rank.JACK, Suit.HEARTS), Card(Rank.JACK, Suit.DIAMONDS),
]
middle_cards=[Card(Rank.NINE,Suit.DIAMONDS)]
# print(Deck.get_legal_cards(hand, middle_cards))