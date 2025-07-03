def best_hands(hands):
    high_cards = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    suits = ['H', 'D', 'S', 'C']

    def parse_hand(hand_str):
        cards = []
        for card_str in hand_str.split():
            if len(card_str) < 2:
                print(f'Incorrect card: {card_str}')
                return None
            suit = card_str[-1].upper()
            value = card_str[:-1].upper()
            if suit not in suits:
                print(f'Invalid suit: {suit}')
                return None
            if value in high_cards:
                num_value = high_cards[value]
            elif value.isdigit() and 2 <= int(value) <= 10:
                num_value = int(value)
            else:
                print(f'Invalid card value: {value}')
                return None
            cards.append({'value': num_value, 'suit': suit})
        return cards

    def evaluate_hand(hand):
        values = sorted([card['value'] for card in hand], reverse=True)
        suits_set = set(card['suit'] for card in hand)
        value_counts = {v: values.count(v) for v in set(values)}
        unique_values = sorted(set(values))

        # Check for flush
        flush = len(suits_set) == 1

        # Check for straight (including Ace-low: A,2,3,4,5)
        straight = False
        if len(unique_values) == 5:
            if unique_values[-1] - unique_values[0] == 4:
                straight = True
            elif unique_values == [2, 3, 4, 5, 14]:  # Ace-low straight
                values = [1 if v == 14 else v for v in values]  # Treat A as 1
                straight = True

        # Royal flush
        if flush and straight and max(values) == 14 and min(values) == 10:
            return (10, values)
        # Straight flush
        if flush and straight:
            return (9, values)
        # Four of a kind
        if 4 in value_counts.values():
            quad_value = [v for v, count in value_counts.items() if count == 4][0]
            kicker = [v for v in values if v != quad_value][:1]
            return (8, [quad_value] + kicker)
        # Full house
        if sorted(value_counts.values()) == [2, 3]:
            trio = [v for v, count in value_counts.items() if count == 3][0]
            pair = [v for v, count in value_counts.items() if count == 2][0]
            return (7, [trio, pair])
        # Flush
        if flush:
            return (6, values)
        # Straight
        if straight:
            return (5, values)
        # Three of a kind
        if 3 in value_counts.values():
            trio = [v for v, count in value_counts.items() if count == 3][0]
            kickers = sorted([v for v in values if v != trio], reverse=True)[:2]
            return (4, [trio] + kickers)
        # Two pair
        if list(value_counts.values()).count(2) == 2:
            pairs = sorted([v for v, count in value_counts.items() if count == 2], reverse=True)
            kicker = sorted([v for v in values if v not in pairs], reverse=True)[:1]
            return (3, pairs + kicker)
        # One pair
        if 2 in value_counts.values():
            pair = [v for v, count in value_counts.items() if count == 2][0]
            kickers = sorted([v for v in values if v != pair], reverse=True)[:3]
            return (2, [pair] + kickers)
        # High card
        return (1, values)

    # Parse and evaluate all hands
    parsed_hands = [parse_hand(hand) for hand in hands]
    if any(hand is None for hand in parsed_hands):
        return None

    # Get rankings and tiebreaker values
    rankings = [(evaluate_hand(hand), idx, hand_str) for idx, (hand, hand_str) in enumerate(zip(parsed_hands, hands))]
    
    # Find the best hand(s)
    max_rank = max(rank for rank, _, _ in rankings)
    best_hands = [(rank, hand_str) for rank, _, hand_str in rankings if rank[0] == max_rank[0]]
    
    # Collect hands with identical tiebreaker values
    max_tiebreaker = max(rank[1] for rank, _ in best_hands)
    tied_hands = [hand_str for rank, hand_str in best_hands if rank[1] == max_tiebreaker]
    
    return tied_hands