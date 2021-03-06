##Python27 library for blackjack shoe/deck operations and hand validation utils

##Installation:

```python
pip install git+https://github.com/jkrooskos/pyblackjack.git
```
##Basic Usage:

###Create and use a shoe instance
```python
from pyblackjack import pyblackjack

>>> shoe = pyblackjack.Shoe()
>>> hand = shoe.deal_cards(2)

>>> hand
[2, 50]

#represent hand with rank/suit
>>>[pyblackjack.CARDS[card] for card in hand]
['Ks', '4c']

>>> shoe.cards_left
50

>>> shoe.cards_dealt
2

#create multi-deck shoe
>>> shoe = pyblackjack.Shoe(3)

>>> shoe.cards_left
156

```

###Create/use utils instance
```python
from pyblackjack import pyblackjack

ut = pyblackjack.Utils()
shoe = pyblackjack.Shoe()
hand = shoe.deal_cards(3)

>>> [pyblackjack.CARDS[card] for card in hand]
['Js', '4d' , 'Ac']

#test for blackjack
>>> ut.blackjack(hand)
False

#test for 21
>>> ut.twenty_one(hand)
False

#test for bust
>>> ut.bust(hand)
False

#get hand value
>>> ut.hand_value(hand)
15

#test for soft 17
>>> ut.soft_seventeen(hand)
False
```
##Further Documentation:

Read the Docs:   <a href=http://pyblackjack.readthedocs.org>pyblackjack</a>

##Licensing
 
Please see the file called LICENSE.txt.
