"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    face_cards = ['J','Q','K']
    if str(card) in face_cards:
        return 10
    if str(card) == 'A':
        return 1
    return int(card)


print(value_of_card('2'))
print(value_of_card('A'))
print(value_of_card('J'))



def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    face_cards = ['J','Q','K']

    if card_one in face_cards:
        card_one_value = 10
    elif card_one.isdigit():
        card_one_value = int(card_one)
    else:
        card_one_value = 1
    
    if card_two in face_cards:
        card_two_value = 10
    elif card_two.isdigit():
        card_two_value = int(card_two)
    else:
        card_two_value = 1

    if card_one_value > card_two_value:
        return card_one
    if card_two_value > card_one_value:
        return card_two
    else:
        return (card_one, card_two)


print(higher_card('5', 'K'))
print(higher_card('J', 'J'))
print(higher_card('Q', '5'))



def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    face_cards = ['J','K','Q']

    if card_one in face_cards:
        card_one_value = 10
    elif card_one == 'A':
        card_one_value = 11
    else:
        card_one_value = int(card_one)
    
    if card_two in face_cards:
        card_two_value = 10
    elif card_two == 'A':
        card_two_value = 11
    else:
        card_two_value = int(card_two)

    if card_one_value + card_two_value > 10:
        return 1
    else:
        return 11

    
print(value_of_ace('A', '8'))
print(value_of_ace('2', '7'))
print(value_of_ace('J', '5'))



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    face_cards = ['J','K','Q']

    if card_one in face_cards:
        card_one_value = 10
    elif card_one == 'A':
        card_one_value = 11
    else:
        card_one_value = int(card_one)
    
    if card_two in face_cards:
        card_two_value = 10
    elif card_two == 'A':
        card_two_value = 11
    else:
        card_two_value = int(card_two)

    if card_one == 'A' and card_two == card_one:
        card_two_value = 1
    
    if card_one_value + card_two_value < 21:
        return False
    else:
        return True
    
    
print(is_blackjack('10','9'))
print(is_blackjack('A','K'))
print(is_blackjack('A','10'))
    

    


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    face_cards = ['J','Q','K']
    if card_one in face_cards and card_two in face_cards:
        return True
    if card_one == card_two:
        return True
    else:
        return False
    
print(can_split_pairs('J','A'))
print(can_split_pairs('A','A'))
print(can_split_pairs('2','2'))



def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    face_cards = ['J','K','Q']

    if card_one in face_cards:
        card_one_value = 10
    elif card_one == 'A':
        card_one_value = 1
    else:
        card_one_value = int(card_one)
    
    if card_two in face_cards:
        card_two_value = 10
    elif card_two == 'A':
        card_two_value = 1
    else:
        card_two_value = int(card_two)

    if card_one == 'A' and card_two == card_one:
        card_one_value = 11
    
    if card_one_value + card_two_value <= 11:
        return True
    else:
        return False
    

print(can_double_down('A', '9'))
print(can_double_down('K', '2'))
print(can_double_down('1', 'J'))
print(can_double_down('A', 'A'))

