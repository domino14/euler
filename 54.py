def extract_rank(card):
    rank = card[0]
    try:
        rank = int(rank)
    except ValueError:
        # XXX: What about if A == 1 ?? for example in a straight.
        rank = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[rank]
    return rank


def sort_hand(hand):
    """
    Sort a hand.

    >>> sort_hand(['5C', 'QC', 'QH', 'AS', 'TS'])
    ['5C', 'TS', 'QC', 'QH', 'AS']

    >>> sort_hand(['6S','2D','AS','3H','KC'])
    ['2D', '3H', '6S', 'KC', 'AS']

    """

    return sorted(hand, key=extract_rank)


def consecutive(hand, value_dict, ranks):
    """
    Checks if this sorted hand represents a straight. Returns highest
    value card in straight, or None if not a straight.

    """
    if len(value_dict) != 5:
        return None

    if ranks[-1] - ranks[0] == 4:
        return ranks[-1]
    # XXX: Might not need this case if P:E is dumb.
    if ranks[-1] - ranks[0] == 12:
        # 2 3 4 5 A gets mis-sorted
        if ranks[-2] - ranks[0] == 3:
            return 5  # This is the only case in which it's straight

    return None


def remove_card_with_value(ranks, value):
    """
    Remove value from ranks. Return number of cards removed.

    """
    num_removed = 0
    while True:
        try:
            ranks.remove(value)
            num_removed += 1
        except ValueError:
            break

    return num_removed


def eval_three_of_a_kind(hand, ranks, value_dict):
    three = None
    high = None
    low = None
    others = []
    for rank, num in value_dict.iteritems():
        if num == 3:
            three = rank
        else:
            others.append(rank)

    high = max(others)
    low = min(others)
    return float('4.{:02}{:02}{:02}'.format(three, high, low))


def eval_two_pair(hand, ranks, value_dict):
    high_pair = None
    low_pair = None
    single = None
    pairs = []
    for rank, num in value_dict.iteritems():
        if num == 2:
            pairs.append(rank)
        else:
            single = rank

    high_pair = max(pairs)
    low_pair = min(pairs)
    return float('3.{:02}{:02}{:02}'.format(high_pair, low_pair, single))


def eval_one_pair(hand, ranks, value_dict):
    pair = None
    others = []
    for rank, num in value_dict.iteritems():
        if num == 2:
            pair = rank
        else:
            others.append(rank)
    others.sort()

    return float('2.{:02}{:02}{:02}{:02}'.format(pair, others[2],
                                                 others[1], others[0]))


def eval_three_or_less(hand, ranks, value_dict):
    """
    The logic for evaluating a three-of-a-kind or less is a little more
    complex so we split it here. This evaluates 3-of-a-kind, 2-pair,
    single pair, and high card, using same scoring system as evaluate_hand.
    :hand - The card hand
    :ranks - An array of card ranks, like [2, 3, 5, 7, 11]

    """
    # A three of a kind or a two pair
    # 2 2 2 3 5    2 3 3 3 5    2 3 5 5 5
    # 2 2 3 3 5    2 2 3 5 5    2 3 3 5 5

    if len(value_dict) == 3:
        if any([val == 3 for val in value_dict.values()]):
            return eval_three_of_a_kind(hand, ranks, value_dict)

        return eval_two_pair(hand, ranks, value_dict)

    elif len(value_dict) == 4:
        return eval_one_pair(hand, ranks, value_dict)

    # Otherwise, straightforward high card.
    return float('1.{:02}{:02}{:02}{:02}{:02}'.format(
        ranks[4], ranks[3], ranks[2], ranks[1], ranks[0]))


def evaluate_hand(hand):
    """
    Return a numerical evaluation of a hand.

    1 - High Card
    2 - One Pair
    3 - Two Pairs
    4 - Three of a Kind
    5 - Straight
    6 - Flush
    7 - Full House
    8 - Four of a Kind
    9 - Straight Flush

    Add decimals -- 2 decimals for each set of card values.

    >>> evaluate_hand(['5H','5C','6S','7S','KD'])
    2.05130706

    >>> evaluate_hand(['2C','3S','8S','8D','TD'])
    2.08100302

    >>> evaluate_hand(['5D','8C','9S','JS','AC'])
    1.1411090805

    >>> evaluate_hand(['2H','2D','4C','4D','4S'])
    7.0402

    >>> evaluate_hand(['3C','3D','3S','9S','9D'])
    7.0309

    >>> evaluate_hand(['KS','8S','3S','TS','7S'])
    6.1310080703

    >>> evaluate_hand(['KS','8S','3S','KC','7S'])
    2.13080703

    >>> evaluate_hand(['JC','9S','AS','JS','9H'])
    3.110914

    >>> evaluate_hand(['JC','JH','AS','JS','9H'])
    4.111409

    >>> evaluate_hand(['4H','5S','2C','6C','3D'])
    5.06

    >>> evaluate_hand(['4H','4S','4C','QH','4D'])
    8.0412

    >>> evaluate_hand(['4H','5H','2H','6H','3H'])  # straight flush
    9.06

    >>> evaluate_hand(['TC','AC','KC','JC','QC'])  # royal flush
    9.14

    >>> evaluate_hand(['7C', '5C', '9C', '8S', '7D'])  # not 5.09!!
    2.07090805
    """
    hand = sort_hand(hand)
    value_dict = {}
    for card in hand:
        rank = extract_rank(card)
        if rank not in value_dict:
            value_dict[rank] = 0
        value_dict[rank] += 1
    # Try to find each of the above from bottom up.
    ranks = [extract_rank(card) for card in hand]
    high_value_straight = consecutive(hand, value_dict, ranks)
    suit_set = set()
    for card in hand:
        suit_set.add(card[1])
    if len(suit_set) == 1:
        # It is a flush or a straight/royal flush.
        if high_value_straight:
            # It is a straight/royal flush
            return 9 + high_value_straight/float(100)
        # It's a flush, use card values as decimals.
        return float('6.{:02}{:02}{:02}{:02}{:02}'.format(
            ranks[4], ranks[3], ranks[2], ranks[1], ranks[0]))

    if high_value_straight:
        # It's just a straight.
        return float('5.{:02}'.format(high_value_straight))
    # Look for other types of hands

    if len(value_dict) == 2:
        # This is a 4 of a kind or a full house.
        l_ct = ranks.count(ranks[0])
        h_ct = 5 - l_ct
        if l_ct == 4:
            # 4 of a kind
            return float('8.{:02}{:02}'.format(ranks[0], ranks[-1]))
        elif h_ct == 4:
            return float('8.{:02}{:02}'.format(ranks[-1], ranks[0]))
        elif l_ct == 3:
            return float('7.{:02}{:02}'.format(ranks[0], ranks[-1]))
        elif h_ct == 3:
            return float('7.{:02}{:02}'.format(ranks[-1], ranks[0]))
    elif len(value_dict) >= 3:
        return eval_three_or_less(hand, ranks, value_dict)


def poker_winner(p1_hand, p2_hand):
    """
    Determines the winner of a poker hand. Returns 1 or 2 for the player.

    >>> poker_winner(['5H','5C','6S','7S','KD'], ['2C','3S','8S','8D','TD'])
    2

    >>> poker_winner(['5D','8C','9S','JS','AC'], ['2C','5C','7D','8S','QH'])
    1

    >>> poker_winner(['2D','9C','AS','AH','AC'], ['3D','6D','7D','TD','QD'])
    2

    >>> poker_winner(['4D','6S','9H','QH','QC'], ['3D','6D','7H','QD','QS'])
    1

    >>> poker_winner(['2H','2D','4C','4D','4S'], ['3C','3D','3S','9S','9D'])
    1

    >>> poker_winner(['2H','3D','4C','6D','5S'], ['9C','2C','5C','TC','KC'])
    2
    """
    hand1_val = evaluate_hand(p1_hand)
    hand2_val = evaluate_hand(p2_hand)

    # print '{0}: {1}  ----   {2}: {3}'.format(p1_hand, hand1_val,
    #                                          p2_hand, hand2_val)

    return 1 if hand1_val > hand2_val else 2


def solve():
    p1_wins = 0
    p2_wins = 0
    f = open('p054_poker.txt')
    for line in f:
        cards = line.split(' ')
        p1_hand = [card.strip() for card in cards[:5]]
        p2_hand = [card.strip() for card in cards[5:]]
        winner = poker_winner(p1_hand, p2_hand)
        #print 'comparing', p1_hand, p2_hand, '<---' if winner == 1 else '--->'
        if winner == 1:
            p1_wins += 1
        else:
            p2_wins += 1
    f.close()

    return p1_wins, p2_wins

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    p1, p2 = solve()
    print 'p1 wins: {0}, p2 wins: {1}'.format(p1, p2)
