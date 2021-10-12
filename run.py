
import random


class card:
    def __init__(self, value, suit):
        self.price = value
        self.value = ['A', '2', '3', '4', '5', '6',  
                       '7', '8', '9', '10', 'J', 'Q', 'K'][value-1]
        self.suit = '♥♦♣♠' [suit]
    

    def show(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')
    
    
    def cost(self):
        if self.price >= 10:
            return 10
        elif self.price == 1:
            return 11
        return self.price


class Deck:
    def __init__(self):
        self.cards = []

    def full_deck(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(card(i, j))

    def draw(self, iterartion):
        cards = []
        for i in range(iterartion):
            card = random.choice(self.cards) 
            self.cards.remove(card)
            cards.append(card)
        return cards

    def count(self):
        return len(self.cards)

    
class player_dealer:
    def __init__(self, dealer, deck):
        self.cards = []
        self.dealer = dealer
        self.deck = deck
        self.score = 0
    
    def hit(self):
        self.cards.extend(self.deck.draw(1))
        self.score_checker()
        if self.score ==21:
            return 1
        return 0





        
















