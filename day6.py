o = {}
with open('adventofcode/day6_input.txt', 'r') as f:    
    for line in f.readlines():
        l = line.strip().split(')')
        o[l[1]] = l[0]
count = 0
for oo in o:
    oo = o[oo]
    while oo != 'COM':
        oo = o[oo]
        count += 1
    count += 1
print(count)

count = 0
san = []
oo=o['SAN']
while oo != 'COM':
    san.append(oo)
    oo = o[oo]
oo=o['YOU']
you = []
while oo not in san and oo != 'COM':
    you.append(oo)
    oo = o[oo]
print(you)
print(san)
count = len(you) + san.index(oo)
print(count)
