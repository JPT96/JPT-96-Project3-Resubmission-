""" Import random due to it being a card game to make it fair"""

import random



""" The card class is the creation of the 52 cards within the deck
it is also where the design comes in and the value assignment as well."""

class card:
    def __init__(self, value, suit):
        self.price = value
        self.value = ['A', '2', '3', '4', '5', '6',  
                       '7', '8', '9', '10', 'J', 'Q', 'K'][value-1]
        self.suit = '♥♦♣♠' [suit]
    
    """ This is the show function which displays the cards
    with the assigned values that are written out in a list in the card class
    as well as having a random suit with is also assigned in the card class.
    """

    def show(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')
   
   
   
    """This is where we determine the value/cost of the card
    and if the value is above a 10 it will still be a 10 this will
    be for our jack queens and kings.
    it also establishes that if the value is equal to one make it 11"""

    def cost(self):
        if self.price >= 10:
            return 10
        elif self.price == 1:
            return 11
        return self.price

""" This class is where the deck is made for the game"""

class Deck:
    def __init__(self):
        self.cards = []

   
    """ The full deck function is simply multiplying each card by four
        and creating a range of all the different values you can have
        followed by appending them to the cards creating a full deck."""

    def full_deck(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(card(i, j))



    """ the draw function randomly takes from the full deck
        and appends it to the player or dealer removing it from
        the deck and then returning the cards back to the deck."""


    def draw(self, iterartion):
        cards = []
        for i in range(iterartion):
            card = random.choice(self.cards) 
            self.cards.remove(card)
            cards.append(card)
        return cards

    """ This just returns the length of the cards"""

    def count(self):
        return len(self.cards)

    
""" player dealer assigns the cards
     as a empty list and selfs to appropriate
    values as well as keeping score at 0"""

class player_dealer:
    def __init__(self, dealer, deck,):
        self.cards = []
        self.dealer = dealer
        self.deck = deck
        self.score = 0
    
  
    """ Hit adds a card to your hand and uses
    the score checker to assess the value of the cards
    and if you bust or not"""


    def hit(self):
        self.cards.extend(self.deck.draw(1))
        self.score_checker()
        if self.score > 21:
            return 1
        return 0

    """ The deal function distributes cards
        and checks if the value exceeds 21 by extending
        the cards and drawing 2 from the deck"""

    def deal(self):
        self.cards.extend(self.deck.draw(2))
        self.score_checker()
        if self.score == 21:
            return 1
        return 0




    """ Score checker function assesses the score
        to check whether or not a ace should be counted
        as 1 or 11 and it then returns the value """

    def score_checker(self):
        ace_counter = 0 
        self.score = 0
        for card in self.cards:
            if card.cost() == 11:
                ace_counter += 1
            self.score += card.cost()
        
        while ace_counter != 0 and self.score > 21:
            ace_counter -= 1
            self.score -= 10
           
        return self.score
    
    

    """ The show function reveals both players
        cards and scores by implementing the self.score
        and having player or dealer printed next to the value."""

    def show(self):
        if self.dealer:
            print("Dealers Cards")
        else:
            print("Players Cards")
        
        for i in self.cards:
            i.show()
        print("Score: " + str(self.score))

    
    
""" The Game class simply creates the functionality base of the game
    by assigning the appropriate variables and functions as well as previous classes
    like the deck class to create a full deck."""

class the_game:
    def __init__(self):
        self.deck = Deck()
        self.deck.full_deck()
        self.player = player_dealer(False, self.deck)
        self.dealer = player_dealer(True, self.deck)
        self.round_count = 0
        
    """This round function deal cards to the relative statuses
       and has a welcome message for the user to view """
    
    def round(self):
        p_status = self.player.deal()
        d_status = self.dealer.deal()
        print("Welcome to Black Jack")
        
       

        """ This has the value of player chips within the take bet
        function and reveals the card value that the player has.
        There is also a remainder of round counter in here to
        start work on increasing the rounds of the game."""


        self.round_count += 1
        take_bet(player_chips)
        self.player.show()

        """ This if statement just checks for either dealer
            or player getting blackjack and applying the correct
            chips method to the players total."""

        if p_status == 1:
            print("Player got Blackjack! Congrats!")
            player_chips.win_bet()
            print('\n Your total chips are: {}'.format(player_chips.total))
            if d_status == 1:
                print("Dealer and Player got Blackjack! It's a push. (Tie)")
                player_chips.loss_bet()
                print('\n Your total chips are: {}'.format(player_chips.total))
            return 1
        
       

        """ This While true statement has all of the hit hold functionality
        and also monitors the bust of the player.
        It also has error handling for when either hit or hold isn't
        entered correctly or something else entirely. This while statement
        will print various print statements based on your result."""

        while True:
            bust = 0
            command = input("Hit or Hold?:\n")
            if command == "Hit":
                bust = self.player.hit()
                self.player.show()
            elif command == "Hold":
                break
            else:
                print("Please enter Hit or Hold starting with a capital letter")
                continue
            if bust == 1:
                print("Player Busted, You're flat Broke!")
                player_chips.loss_bet()
                print('\n Your total chips are: {}'.format(player_chips.total))
                return 1



        """ This portion prints on a new line
            and reveals the dealers cards.
            it also checks for black jack
            and then gives you your chips total
            after the loss bet function is called"""

        print("\n")
        self.dealer.show()
        if d_status == 1:
            print("The Dealer got BlackJack. Is he cheating?")
            player_chips.loss_bet()
            print('\n Your total chips are: {}'.format(player_chips.total))
            return 1
            
        """ This while loop checks if the dealer is below 17 and makes it hit
            It also reveals its cards and prints your total chips value
            """
 
        while self.dealer.score_checker() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer Bust. I guess he wasn't cheating after all. You win!")
                player_chips.win_bet()
                print('\n Your total chips are: {}'.format(player_chips.total))
                return 1
            self.dealer.show()


        """ This section covers all the outcomes of the game
            if either player does not draw black jack out the gate
            all with a formar at the end to give a chips update
"""

        if self.dealer.score_checker() == self.player.score_checker():
            print("It's a tie, Dealer wins by default") 
            player_chips.loss_bet()
        elif self.dealer.score_checker() > self.player.score_checker():
            print("dealer wins. Is it rigged?")
            player_chips.loss_bet()
            print('\n Your total chips are: {}'.format(player_chips.total))
        elif self.dealer.score_checker() < self.player.score_checker():
            print("You did it You won! Take your win and run")
            player_chips.win_bet()
            print('\n Your total chips are: {}'.format(player_chips.total))


""" this is the chips class it establishes the basic function
of the currency within the game
it also takes in the parameters of how to update
the chips based on whether or not the player
loses or wins
"""

class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def loss_bet(self):
        self.total -= self.bet


""" This is the take_bet function
    in here we take a prompt of an integer and check for a value error
    if the error is triggered it will give a desired print to ask
    for a number. This function also checks if your bet is higher than
    your chip total and if it is. It will print a statement of you dont have enough
    with a format attached to the end to give you your current chip value
"""



def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips do you want to gamble? :"))
        except ValueError:
            print("Please input a number")
        else:
            if chips.bet > chips.total:

                print("You don't have enough for that you have: {}".format(chips.total))
            else:
                break

""" establishing a random letter the class the_game
so that we can combine the game and the round to
start the terminal console game. """

b = the_game()

player_chips = Chips()

"""This initiates the game I did have it so it would start a new round based on a prompt
at the end of the game but this lead to a few errors of score carrying over.
this was an attempt to make the chips have more of a use over a multitude of
rounds but ended up being to buggy and took the fun from the game."""

b.round()

"""This is a print statement for the end
of the game
 """

print("Thank you for playing don't be a stranger now.")