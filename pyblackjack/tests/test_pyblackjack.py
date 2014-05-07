import unittest
from .. import pyblackjack

class TestUtils(unittest.TestCase):
    """
    Unittests for Utils class
    """

    def test_unmodified_hand_value(self):
        """
        Test unmodified hand value method
        """
        ut = pyblackjack.Utils()
        self.assertEqual(ut._unmodified_hand_value([1, 2]), 11)
        self.assertEqual(ut._unmodified_hand_value([14, 17, 36]), 16)
        self.assertEqual(ut._unmodified_hand_value([50, 4]), 14)
        self.assertNotEqual(ut._unmodified_hand_value([1, 2]), 21)
        self.assertNotEqual(ut._unmodified_hand_value([40, 19]), 20)
        self.assertNotEqual(ut._unmodified_hand_value([1, 48]), 17)

    def test_hand_value(self):
        """
        Test hand value method
        """
        ut = pyblackjack.Utils()
        self.assertEqual(ut.hand_value([1, 2]), 21)
        self.assertEqual(ut.hand_value([14, 17, 48, 52]), 19)
        self.assertEqual(ut.hand_value([40, 26]), 13)
        self.assertNotEqual(ut.hand_value([2, 8]), 18)
        self.assertNotEqual(ut.hand_value([50, 5]), 22)
        self.assertNotEqual(ut.hand_value([1, 2, 3]), 4)

    def test_blackjack(self):
        """
        Test blackjack validation method
        """
        ut = pyblackjack.Utils()
        self.assertTrue(ut.blackjack([1, 2]))
        self.assertTrue(ut.blackjack([14, 17]))
        self.assertTrue(ut.blackjack([40, 4]))
        self.assertFalse(ut.blackjack([2, 8]))
        self.assertFalse(ut.blackjack([50, 5]))
        self.assertFalse(ut.blackjack([1, 2, 3]))

    def test_wenty_one(self):
        """
        Test twenty_one validation method
        """
        ut = pyblackjack.Utils()
        self.assertTrue(ut.twenty_one([1, 10, 23]))
        self.assertTrue(ut.twenty_one([48, 52, 52, 29, 1]))
        self.assertTrue(ut.twenty_one([47, 12, 27]))
        self.assertFalse(ut.twenty_one([48, 50]))
        self.assertFalse(ut.twenty_one([41, 2]))
        self.assertFalse(ut.twenty_one([1]))

    def test_bust(self):
        """
        Test bust validation method
        """
        ut = pyblackjack.Utils()
        self.assertTrue(ut.bust([9, 10, 49, 17]))
        self.assertTrue(ut.bust([1, 2, 42, 39]))
        self.assertTrue(ut.bust([52, 28, 29]))
        self.assertFalse(ut.bust([1, 2]))
        self.assertFalse(ut.bust([52]))
        self.assertFalse(ut.bust([29, 30]))

    def test_soft_17(self):
        """
        Test soft_17 validation method
        """
        ut = pyblackjack.Utils()
        self.assertTrue(ut.soft_17([1, 22]))
        self.assertTrue(ut.soft_17([40, 51, 25]))
        self.assertTrue(ut.soft_17([14, 36, 1]))
        self.assertFalse(ut.soft_17([1, 2, 8]))
        self.assertFalse(ut.soft_17([41, 23, 52]))
        self.assertFalse(ut.soft_17([42, 1, 22]))


    def test_aces(self):
        """
        Test aces validation method
        """
        ut = pyblackjack.Utils()
        self.assertTrue(ut.aces([1, 14]))
        self.assertTrue(ut.aces([1, 40]))
        self.assertTrue(ut.aces([14, 27]))
        self.assertFalse(ut.aces([1, 14, 27]))
        self.assertFalse(ut.aces([48, 49]))
        self.assertFalse(ut.aces([1, 48, 40]))


    def test_surrender(self):
        """
        Test surrender validation method
        """
        ut = pyblackjack.Utils()
        self.assertTrue(ut.surrender([1, 52]))
        self.assertTrue(ut.surrender([28, 17]))
        self.assertTrue(ut.surrender([40, 2]))
        self.assertFalse(ut.surrender([52, 9]))
        self.assertFalse(ut.surrender([45, 15]))
        self.assertFalse(ut.surrender([19, 3]))

class TestShoe(unittest.TestCase):
    """
    Unittest for Shoe class
    """

    def test_build_shoe(self):
        """
        Test deck length for build shoe method
        """
        shoe = pyblackjack.Shoe()
        self.assertEqual(len(shoe.cards), 52)
        
        shoe = pyblackjack.Shoe(3)
        self.assertEqual(len(shoe.cards), 156)

        shoe = pyblackjack.Shoe(2)
        self.assertNotEqual(len(shoe.cards), 52)

    def test_deal_cards(self):
        """
        Test hand length for build shoe method
        """
        shoe = pyblackjack.Shoe()
        hand = shoe.deal_cards(7)
        self.assertEqual(len(hand), 7)
        
        hand = shoe.deal_cards(5)
        self.assertEqual(len(hand), 5)

        hand = shoe.deal_cards(3)
        self.assertNotEqual(len(hand), 4)


    def test_count_of_cards(self):
        """
        Test shoe object count of cards left and cards dealt
        """
        shoe = pyblackjack.Shoe()
        hand = shoe.deal_cards(7)
        self.assertEqual(shoe.cards_dealt, 7)
        self.assertEqual(shoe.cards_left, 45)

        shoe.deal_cards(2)
        self.assertEqual(shoe.cards_dealt, 9)
        self.assertEqual(shoe.cards_left, 43)

        shoe = pyblackjack.Shoe(2)
        hand = shoe.deal_cards(4)
        self.assertEqual(shoe.cards_dealt, 4)
        self.assertEqual(shoe.cards_left, 100)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
