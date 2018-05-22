# Use Monte Carlo most likely. This should be fun.
import logging
import random

# In clockwise order
squares = [
    'GO', 'A1', 'CC1', 'A2', 'T1',
    'R1', 'B1', 'CH1', 'B2', 'B3',
    'JAIL', 'C1', 'U1', 'C2', 'C3',
    'R2', 'D1', 'CC2', 'D2', 'D3',
    'FP', 'E1', 'CH2', 'E2', 'E3',
    'R3', 'F1', 'F2', 'U2', 'F3',
    'G2J', 'G1', 'G2', 'CC3', 'G3',
    'R4', 'CH3', 'H1', 'T2', 'H2',
]

# 16 cards total, we only care about the destination cards GO and JAIL.
cc_cards = [
    'GO', 'JAIL', '', '',
    '', '', '', '',
    '', '', '', '',
    '', '', '', '',
]

chance_cards = [
    'GO', 'JAIL', 'C1', 'E3',
    'H2', 'R1', '(next r)', '(next r)',
    '(next u)', '(back 3)', '', '',
    '', '', '', '',
]

dice_pips = 4
iterations = 5000000

logging.basicConfig(level=logging.INFO)


def reset_game():
    random.shuffle(cc_cards)
    random.shuffle(chance_cards)


def record_square(squares_at, square):
    if square not in squares_at:
        squares_at[square] = 1
    else:
        squares_at[square] += 1
    logging.debug('Recording square: %s', square)


def start_game():
    squares_at = {}
    consecutive_doubles = 0
    scope = {
        'cc_idx': 0,
        'ch_idx': 0,
        'square_idx': 0,
    }

    def go_to_jail():
        record_square(squares_at, 'JAIL')
        return 10  # index of jail

    def go_to_go():
        record_square(squares_at, 'GO')
        return 0  # index of GO

    def community_chest(landed_on, square_idx):
        drawn = cc_cards[scope['cc_idx']]
        if drawn == '':
            record_square(squares_at, landed_on)
            idx = square_idx
        elif drawn == 'GO':
            idx = go_to_go()
        elif drawn == 'JAIL':
            idx = go_to_jail()
        scope['cc_idx'] = (scope['cc_idx'] + 1) % 16
        return idx

    def chance(landed_on, square_idx):
        drawn = chance_cards[scope['ch_idx']]

        if drawn == '':
            record_square(squares_at, landed_on)
            idx = square_idx
        elif drawn == 'GO':
            idx = go_to_go()
        elif drawn == 'JAIL':
            idx = go_to_jail()

        elif drawn in ('C1', 'E3', 'H2', 'R1'):
            record_square(squares_at, drawn)
            idx = {
                'C1': 11,
                'E3': 24,
                'H2': 39,
                'R1': 5,
            }[drawn]
        elif drawn == '(next r)':
            for i in range(square_idx, 80):
                if squares[i % 40].startswith('R'):
                    record_square(squares_at, squares[i % 40])
                    idx = i % 40
                    break

        elif drawn == '(next u)':
            for i in range(square_idx, 80):
                if squares[i % 40].startswith('U'):
                    record_square(squares_at, squares[i % 40])
                    idx = i % 40
                    break

        elif drawn == '(back 3)':
            idx = (square_idx - 3) % 40
            if squares[idx] == 'CC3':
                idx = community_chest('CC3', idx)
            else:
                record_square(squares_at, squares[idx])
        else:
            import sys
            sys.exit('Unhandled')

        scope['ch_idx'] = (scope['ch_idx'] + 1) % 16
        return idx

    for i in range(iterations):
        if i % 10000 == 0:
            logging.info('Move %s', i)

        die1 = random.randint(1, dice_pips)
        die2 = random.randint(1, dice_pips)
        if die1 == die2:
            consecutive_doubles += 1
        else:
            consecutive_doubles = 0
        logging.debug(' -> Rolled %s and %s', die1, die2)

        if consecutive_doubles > 0 and consecutive_doubles % 3 == 0:
            # Go to jail
            logging.debug(' -> %s consecutive doubles, go to jail',
                          consecutive_doubles)
            go_to_jail()
            continue

        scope['square_idx'] = (scope['square_idx'] + die1 + die2) % 40
        landed_on = squares[scope['square_idx']]
        logging.debug(' -> Advancing to index %s (%s)', scope['square_idx'],
                                                              landed_on)

        if landed_on in ('CC1', 'CC2', 'CC3'):
            scope['square_idx'] = community_chest(landed_on,
                                                  scope['square_idx'])
            logging.debug(' -> New index is %s (%s)', scope['square_idx'],
                                                      squares[scope['square_idx']])
        elif landed_on in ('CH1', 'CH2', 'CH3'):
            scope['square_idx'] = chance(landed_on, scope['square_idx'])
            logging.debug(' -> New index is %s (%s)', scope['square_idx'],
                                               squares[scope['square_idx']])
        elif landed_on == 'G2J':
            scope['square_idx'] = go_to_jail()
            logging.debug(' -> New index is %s (%s)', scope['square_idx'],
                                                      squares[scope['square_idx']])
            continue
        else:
            record_square(squares_at, landed_on)
            continue

    logging.info(squares_at)
    logging.info('%s (exp 6.24) %s (exp 3.18) %s (exp 3.09)',
                 squares_at['JAIL']/float(iterations),
                 squares_at['E3']/float(iterations),
                 squares_at['GO']/float(iterations))

    items = squares_at.items()
    std = sorted(items, key=lambda item: -item[1])
    logging.info('%s%s%s', modal_for_square(std[0][0]),
                 modal_for_square(std[1][0]),
                 modal_for_square(std[2][0]))


def modal_for_square(square):
    idx = squares.index(square)
    if idx < 10:
        return '0' + str(idx)
    return str(idx)


if __name__ == '__main__':
    reset_game()
    start_game()
