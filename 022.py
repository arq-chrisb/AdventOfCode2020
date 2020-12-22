from copy import deepcopy

DEBUG = False

def play_game_one(decks):

    while decks[0] and decks[1]:
        if (first := decks[0].pop(0)) > (second := decks[1].pop(0)):
            decks[0] += [first, second]
        else:
            decks[1] += [second, first]

    return decks

def play_game_two(decks):
    (deck1, deck2) = decks
    history = set()

    while deck1 and deck2:
        cfg = ('|'.join([','.join(map(str, deck)) for deck in decks]))

        if cfg in history:
            return (decks, 1)

        # add config to history
        history.add(cfg)

        # draw
        first = deck1.pop(0)
        second = deck2.pop(0)

        # enough cards?
        if first <= len(deck1) and second <= len(deck2):
            _, winner = play_game_two([deck1[:first], deck2[:second]])

            if winner == 1:
                deck1 += [first, second]
            else:
                deck2 += [second, first]
        else:
            if first > second:
                deck1 += [first, second]
            else:
                deck2 += [second, first]

    return [deck1, deck2], 1 if decks[0] else 2


with open ('022.txt') as input_file:
    orig_decks = [[int(card) for card in player[1:]] for player in [player.strip().split('\n') for player in input_file.read().split('\n\n')]]

    decks = play_game_one(deepcopy(orig_decks))
    print(f'part one: {sum([card * (idx + 1) for idx, card in enumerate(reversed(decks[0] if decks[0] else decks[1]))])}')
    
    (decks, winner) = play_game_two(deepcopy(orig_decks))
    print(f'part two: {sum([card * (idx + 1) for idx, card in enumerate(reversed(decks[0] if winner == 1 else decks[1]))])}')