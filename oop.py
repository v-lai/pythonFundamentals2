# import random  # for Part 2, attempt 1
from random import shuffle  # for Part 2, attempt 2
# Part 1
# Answer the following questions.

# What is a class?
'''
A class is a blueprint for objects. (like a plans to build a house)
'''
# What is an instance?
'''
An instance is an object that is made from a class.  (like a built house)
'''
# What is encapsulation?
'''
Encapsulation is the idea that data and processes on that data are owned by a
class. This helps hide variables from external scopes.
'''
# What is abstraction?
'''
Abstraction is deciding what functions to add to model the class as closely to
how it should actually interface. It is seeing all the functions available in a
class and understanding what the class does.
'''
# What is inheritance?
'''
Inheritance is going up the chain of classes inheriting to borrowing methods
from a parent class.
'''
# What is multiple inheritance?
'''
Multiple inheritance means that a class can inherit from many other classes
(not just a single class).
'''
# What is polymorphism?
'''
Polymorphism is when you have a method you're borrowing, but the child has
different types of implementation.
'''
# What is method resolution order or MRO?
'''
Method Resolution Order (MRO) is an order that Python sets to determine the
order that Python will look for methods on instances of that class, because
Python allows for multiple inheritance. In other languages with single
inheritance, order doesn't really matter, but it does with multiple
inheritance.
'''

# Part 2
# Create a deck of cards class. Internally, the deck of cards should use
# another class, a card class. Your requirements are:

# The Deck class should have a deal method to deal a single card from the deck
# After a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all
# 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a
# value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

'''
first attempt
'''
# class Card():
#     def __init__(self):
#         self.suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
#         self.value = ["A", "2", "3", "4", "5", "6",
#                       "7", "8", "9", "10", "J", "Q", "K"]

#     def all_cards(self):
#         self.cards = []
#         for self.s in self.suit:
#             for self.v in self.value:
#                 self.cards.append(self.v + " of " + self.s)
#         return self.cards


# class Deck(Card):
#     def __init__(self):
#         super().__init__()
#         self.cards = self.all_cards()

#     def deal(self):
#         pick = random.choice(self.cards)
#         self.cards.remove(pick)
#         return pick

#     def shuffle(self):
#         shuffled_deck = []
#         while len(shuffled_deck) < 52:
#             shuffled_deck.append(self.deal())
#         return shuffled_deck

'''
second attempt (after looking at solution)
'''
# card functionality - suits and values


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} or {}".format(self.value, self.suit)


# deck functionality -
class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5",
                       "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def __repr__(self):
        return "Cards in deck: {}".format(len(self.cards))

    def shuffle(self):
        if len(self.cards) == 52:
            shuffle(self.cards)
        return self

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return "All cards have been dealt"
