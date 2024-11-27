"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    rounds_list = []
    i = 0
    while i < 3:
        rounds_list.append(number + i)
        i += 1
    return rounds_list

print(get_rounds(5))

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    new_list = rounds_1 + rounds_2
    return new_list

print(concatenate_rounds([1,2,3],[4,5,6]))


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    return False

print(list_contains_round([4,5,6], 5))
print(list_contains_round([4,5,6], 8))


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand)/len(hand)

print(card_average([1,2,3,4,5,6,7,8,9,9,8]))


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    first_card = hand[0]
    last_card = hand[-1]
    length = len(hand)
    middle_index = int((length - 1) / 2)
    middle_card = hand[middle_index]
    calc_avg = sum(hand)/len(hand)
    fal_avg = (first_card+last_card) / 2 #fal_avg = first and last average
    values = [calc_avg, fal_avg, middle_index, middle_card]
    print(values)
    if fal_avg == calc_avg or middle_card == calc_avg:
        return True
    return False

print(approx_average_is_average([1,2,3]))
print(approx_average_is_average([2,3,4,8,8]))
print(approx_average_is_average([0,1,5]))

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    length = len(hand)
    i = 0
    odd_index_cards = []
    even_index_cards = []
    while i < length:
        if i % 2 == 0:
            even_index_cards.append(hand[i])
        else:
            odd_index_cards.append(hand[i])
        i +=1
    print(odd_index_cards, even_index_cards)
    odd_index_cards_avg = sum(odd_index_cards)/ len(odd_index_cards)
    even_index_cards_avg = sum(even_index_cards)/ len(even_index_cards)
    if odd_index_cards_avg == even_index_cards_avg:
        return True
    return False
print(average_even_is_average_odd([1,2,3,4,5,6,7]))
print(average_even_is_average_odd([1,2,3,4,5,6,7,8]))


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] *= 2
    
    return hand

print(maybe_double_last([4,3,11]))
print(maybe_double_last([4,3,9]))

