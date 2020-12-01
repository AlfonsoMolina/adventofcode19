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

# On position i comes the card at position j
def new_stack(l, i):
    a = -1
    b = l-1
    j = l-1-i
    return a, b

def cut(l, n, i):
    j = (i + n) % l
    a = 1
    b = n
    return a, b

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
    a = 1/n
    b = (k*r)/n + m
    return a, b

# with open('adventofcode/day22_input.txt', 'r') as f:    
#     input_data = f.read()

input_data = input_data.split('\n')
input_data.reverse()

l = 119315717514047
i = 0
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
a, b = 0, 0
for k in range(1):
    for cmd in input_data:
        if 'deal into new stack' in cmd:
            aa, bb = new_stack(l, i)
            a += aa
            b += bb
        elif 'deal with increment' in cmd:
            n = int(cmd.split()[-1])
            aa, bb = increment(l, n, i)
            a += aa
            b += bb
        elif 'cut' in cmd:
            n = int(cmd.split()[-1])
            aa, bb = cut(l, n, i)
            a += aa
            b += bb
    print(a, b)
# print(l)
res = 2020
for i in range(101741582076661):
    res = (a*res + b) % l
    if i % 1000000 == 0:
        print(i)
