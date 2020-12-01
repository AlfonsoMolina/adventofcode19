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

x1 = 67729481370408
x2 = 4870029286288
l = 119315717514047
for a in range (500):
    for b in range(500):
        if any(c*l == a*x1 + b for c in range(500)) and any(c*l+1 == a*x2 + b for c in range(500)):
                print(a, b)
    print(a)
exit()
# On position i comes the card at position j
def new_stack(l, i):
    j = l-1-i
    return j

def cut(l, n, i):
    j = (i + n) % l
    return j

def increment(l, n, i):
    r = l%n
    o = l//n
    k = 0
    m = 0
    while True:
        if (i + k*r) % n == 0:
            break
        k += 1
        m += o
        if r*k%n > n:
            m -= 1
    j = (i+k*r)/n + m
    return int(j)

# with open('adventofcode/day22_input.txt', 'r') as f:    
#     input_data = f.read()

input_data = input_data.split('\n')
input_data.reverse()

l = 10
i = 2020
# # deck = [0,1,2,3,4,5,6,7,8,9]
# # for j in range(10):
#     # for k in range(l):
#         i = deck[k]
#         for cmd in input_data:
#             if 'deal into new stack' in cmd:
#                 i = new_stack(l, i)
#             elif 'deal with increment' in cmd:
#                 n = int(cmd.split()[-1])
#                 i = increment(l, n, i)
#             elif 'cut' in cmd:
#                 n = int(cmd.split()[-1])
#                 i = cut(l, n, i)
#         deck[k] = i
#     print(deck)

# exit()
i = 1
for k in range(1):
    for cmd in input_data:
        if 'deal into new stack' in cmd:
            i = new_stack(l, i)
        elif 'deal with increment' in cmd:
            n = int(cmd.split()[-1])
            i = increment(l, n, i)
        elif 'cut' in cmd:
            n = int(cmd.split()[-1])
            i = cut(l, n, i)
    print(i)
# print(l)