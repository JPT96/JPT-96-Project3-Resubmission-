
import random


class card:
    def __init__(self, value, suit):
        self.price = value
        self.value = ['A', '2', '3', '4', '5', '6',  
                       '7', '8', '9', '10', 'J', 'Q', 'K'][value-1]
        self.suit = '♥♦♣♠' [suit]
        

