"""
Blackjack library with utils and shoe/deck operations.
"""

import random

CARDS = {1:'As', 2:'Ks', 3:'Qs', 4:'Js', 5:'Ts', 6:'9s', 7:'8s', 8:'7s',
         9:'6s', 10:'5s', 11:'4s', 12:'3s', 13:'2s',

         14:'Ah', 15:'Kh', 16:'Qh', 17:'Jh', 18:'Th', 19 :'9h', 20:'8h',
         21:'7h', 22:'6h', 23:'5h', 24:'4h', 25 :'3h', 26:'2h',

         27:'Ad', 28:'Kd', 29:'Qd', 30:'Jd', 31:'Td', 32 :'9d', 33:'8d',
         34:'7d', 35:'6d', 36:'5d', 37:'4d', 38 :'3d', 39:'2d',

         40:'Ac', 41:'Kc', 42:'Qc', 43 :'Jc', 44 :'Tc', 45 :'9c', 46 :'8c',
         47:'7c', 48:'6c', 49:'5c', 50:'4c', 51 :'3c', 52:'2c'}

CARD_VALUES = {1:1, 2:10, 3:10, 4:10, 5:10, 6:9, 7:8, 8:7,
               9:6, 10:5, 11:4, 12:3, 13:2,

               14:1, 15:10, 16:10, 17:10, 18:10, 19:9, 20:8,
               21:7, 22:6, 23:5, 24:4, 25:3, 26:2,

               27:1, 28:10, 29:10, 30:10, 31:10, 32:9, 33:8,
               34:7, 35:6, 36:5, 37:4, 38:3, 39:2,

               40:1, 41:10, 42:10, 43:10, 44:10, 45:9, 46:8,
               47:7, 48:6, 49:5, 50:4, 51:3, 52:2}

ACES = set([1, 14, 27, 40])

TENS = set([2, 3, 4, 5, 15, 16, 17, 18, 28, 29, 30, 31, 41, 42, 43, 44])

class Utils(object):
    """
    Blackjack utilities for hand evaluation.
    """

    @staticmethod
    def _unmodified_hand_value(hand):
        """
        Returns hand value where aces are counted as one.
        """
        return sum([CARD_VALUES[card] for card in hand])

    @staticmethod
    def hand_value(hand):
        """
        Returns hand value where aces are counted as one or eleven.
        """
        value = Utils._unmodified_hand_value(hand)
        aces = ACES & set(hand)

        for ace in aces:
            if value < 12:
                value += 10

        return value

    @staticmethod
    def blackjack(hand):
        """
        Returns True if hand is a blackjack.
        Hand must contain two cards, otherwise an exception is raised.
        """
        return len(hand) == 2 and len(set(hand) & ACES) == 1 and len(set(hand) & TENS) == 1

    @staticmethod
    def twenty_one(hand):
        """
        Returns True if hand has a value of twenty one.
        Hand may contain any number cards.
        """
        return Utils.hand_value(hand) == 21

    @staticmethod
    def bust(hand):
        """
        Returns True if hand value exceeds 21.
        Hand may contain any number of cards.
        """
        return Utils.hand_value(hand) > 21

    @staticmethod
    def soft_17(hand):
        """
        Returns True if hand is a soft seventeen.
        A soft seventeen is defined as a hand with a
        value of seven or seventeen.
        Hand may contain any number of cards.
        """
        value = Utils._unmodified_hand_value(hand)
        aces = ACES & set(hand)
        return value == 7 and len(aces) >= 1

    @staticmethod
    def aces(hand):
        """
        Returns True if a two card hand contains two aces.
        """
        return len(hand) == 2 and len(ACES & set(hand)) == 2

    @staticmethod
    def surrender(hand):
        """
        Returns True if a two card hand may be eligible
        for surrender play.
        """
        return hand[0] in ACES or hand[0] in TENS

class Shoe(object):
    """
    Supports blackjack shoe operations for any number of decks.
    """

    def __init__(self, num_of_decks=1):
        """
        Instantiate shoe with one deck.
        """
        self.build_shoe(num_of_decks)

    def build_shoe(self, num_of_decks):
        """
        Build deck.
        """
        self.num_of_decks = num_of_decks
        self.cards_left = num_of_decks * 52
        self.cards_dealt = 0
        self.cards = [num for decks in range(num_of_decks) for num in range(1, 53)]
        self.shuffle()

    def shuffle(self):
        """
        Shuffle cards.
        """
        random.shuffle(self.cards)

    def deal_cards(self, num_of_cards):
        """
        Deal cards.
        """
        cards = random.sample(self.cards, num_of_cards)
        for card in cards:
            self.cards.remove(card)
            self.cards_left -= 1
            self.cards_dealt += 1

        return cards
