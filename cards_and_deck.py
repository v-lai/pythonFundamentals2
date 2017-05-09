from random import shuffle  # for shuffle function in Deck
from functools import wraps  # for log decorator
import csv  # for reading csv files

# for loading deck from a CSV file - bonus 5
loaded_deck = []
with open('deal.log') as csvfile:
    reader = csv.reader(csvfile, delimiter="\n")
    rows = list(reader)
    for row in rows:
        loaded_deck.extend(row)

print(loaded_deck)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5",
                       "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = loaded_deck or [Card(suit, value)
                                     for suit in self.suits for value in self.values]

    def __iter__(self):  # telling Python we want to use this class as an iterator
        return iter(self.cards)

    def __repr__(self):
        return "Cards in deck: {}".format(len(self.cards))

    def log(fn):  # decorator - bonus 2
        @wraps(fn)
        def inner(*args):
            # print("The name of the function is: {}, args are: {}".format(
                # fn.__name__, fn.__code__.co_varnames))
            # fn.__code__.co_varnames what does this mean? it works, though...

            # with open("deck.log", "a+") as file:  # read and write - bonus 3
            #     file.write("The name of the function is: {}, args are: {}\n".format(
            #         fn.__name__, fn.__code__.co_varnames))
            return fn(*args)
        return inner

    @log
    def shuffle(self):
        if len(self.cards) == 52:
            shuffle(self.cards)
        return self

    @log
    def deal(self):
        if len(self.cards) > 0:
            # return self.cards.pop()
            temp_card = self.cards.pop()
            # with open("deal.log", "a+") as file:  # read and write - bonus 4
            #     file.write("{}\n".format(temp_card))
            return temp_card
        return "All cards have been dealt"


d = Deck()
# for making iterable - bonus 1
for card in d:
    print(card) # matches loaded list

# d.shuffle()
# print(d.deal())

# for saving deck
# d.shuffle() # shuffle
# while len(d.cards) > 0: # log cards
#     d.deal()
