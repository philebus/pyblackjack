##Python27 library for blackjack shoe/deck operations and hand validation utils

##Basic Usage:

###Create/use a shoe instance
```python
import pyblackjack

>>> shoe = pyblackjack.Shoe()
>>> hand = shoe.deal_cards(2)

>>> hand
[2, 50]

#convert to cards
>>>[pyblackjack.CARDS[card] for card in hand]
['Ks', '4c']

>>> shoe.cards_left
50

>>> shoe.cards_dealt
2

```

##Licensing
 
Please see the file called LICENSE.txt.
