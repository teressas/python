from . import card
from random import shuffle

class Deck:
    player1_hand = []
    player2_hand = []

    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(2,15):
                str_val = ""
                if i == 14:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_cards(self):
        # self.player1_hand = []
        # self.player2_hand = []
        for idx in range(0,len(self.cards)):
            if idx % 2 == 0:
                self.player1_hand.append(self.cards.pop(0))
            else:
                self.player2_hand.append(self.cards.pop(0))

