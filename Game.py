from Player import Player
from Deck import Deck
import random
class Game:
    counter = 1
    def __init__(self):
        player1= Player()
        player2= Player()
        player3= Player()
        self.player_list=[player1,player2,player3]
        self.table_cards=[]#as in the cards left after dealing or "galds"
        self.middle_cards=[]# current hand played in the game or "stiķis"
        self.starting_player=player1
        self.round_timer=0
        self.start_new_game()
        
    def start_new_game(self):
        if self.round_timer !=0:
            self.resolve_round()
        self.round_timer=0
        self.player_list.append(self.player_list.pop(0))
        deck=self.shuffle_cards()
        for player in self.player_list:
               player.round_points=0
               for i in range(0,7):
                   player.hand[i]=deck.pop()
        self.table_cards[deck.pop(),deck.pop()]
        self.game_loop()
        
    def play_a_card(self):
        if self.round_timer==0:
            player=self.player_list[0]
        else:
            pass    #first write a method that resolves a round then use it to set the player to be the player who won lost round then 
            
        print(Deck.get_legal_cards(player.hand,self.middle_cards))
        player.hand.pop(player.hand.index(Deck.get_legal_cards(player.hand,self.middle_cards)[0]))
        self.round_timer+=1
        if self.round_timer==3:
            self.resolve_hand()
        if self.round_timer==24:
            self.start_new_game
    
    def shuffle_cards(self):
        dick=Deck.get_all_cards()
        dick=random.shuffle(dick)
        return dick
    def resolve_hand(self):
        #need a way to compare hands probably happens in the deck
        #need to find who played the winning card <-set that as a game parametter
        pass
    def resolve_round(self):
        #TODO finish
        for i in range(0,2):
            print(self.player_list[i].round_points)
            
    