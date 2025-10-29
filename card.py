from SuitEnum import Suit
from RankEnum import Rank

class Card:
    def __init__(self,rank:Rank,suit:Suit):
        self.rank= rank
        self.suit= suit
        self.points =self.calc_points()
        
    def __eq__(self, value):
        if not isinstance(value, Card):
            raise TypeError(f"Comparing Card with another incompatible class {type(value)}")
        return self.__key() == value.__key()
    
    def __key(self):
        return (self.rank, self.suit)
    
    def __hash__(self):
        return hash(self.__key())

    def calc_points(self):
        point_map = {Rank.SEVEN:0,Rank.EIGHT:0,Rank.NINE:0,Rank.TEN:10,Rank.JACK:2,Rank.QUEEN:3,Rank.KING:4,Rank.ACE:11 }
        return point_map[self.rank]
    
    def __repr__(self):
        return f"{self.rank.name} of {self.suit.name}"
    
card1 = Card(Rank.ACE, Suit.CLUBS)
card2 = Card(Rank.ACE, Suit.CLUBS)
