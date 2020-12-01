input_data = """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1
"""

def new_deck(n):
    deck = []
    for i in range(n):
        deck.append(i)
    return deck

def new_stack(deck):
    deck.reverse()
    return deck

def cut(deck, n):
    if n > 0:
        cut = deck[:n]
        del deck[:n]
        deck.extend(cut)
        return deck
    elif n < 0:
        cut = deck[n:]
        del deck[n:]
        cut.extend(deck)
        del deck[:]
        deck.extend(cut)
        return cut
    else:
        return deck

def increment(deck, n):
    new_deck = [None] * len(deck)
    l = len(new_deck)
    i = 0
    while deck:        
        new_deck[n*i%l] = deck.pop(0)
        i += 1
    
    deck.extend(new_deck)
    
    return deck

# with open('adventofcode/day22_input.txt', 'r') as f:    
#     input_data = f.read()

input_data = input_data.split('\n')
deck = new_deck(10)
print(deck)
for i in range(10):
    for cmd in input_data:
        if 'deal into new stack' in cmd:
            new_stack(deck)
        elif 'deal with increment' in cmd:
            increment(deck, int(cmd.split()[-1]))
        elif 'cut' in cmd:
            cut(deck, int(cmd.split()[-1]))

    print(deck)
