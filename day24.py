input_data = '''#####
...##
#..#.
#....
#...#'''

layout = [list(row) for row in input_data.split('\n')]

for row in layout:
    print(''.join(row))

state_track = []
track = ''
for row in layout:
    track += ''.join(row)

state_track.append(track)

def evolve(layout):
    new_layout = []
    for y in range(5):
        new_layout.append(layout[y][:])
        for x in range(5):
            bugs = 0
            for i, j in [[1,0], [-1,0], [0,-1], [0,1]]:
                if not 0 <= y+i < 5 or not 0 <= x+j < 5:
                    continue
                bugs += 1 if layout[y+i][x+j] == '#' else 0
            if layout[y][x] == '#' and bugs != 1:
                new_layout[y][x] = '.'
            elif layout[y][x] == '.' and 0 < bugs < 3:
                new_layout[y][x] = '#'
    return new_layout

while True:
    layout = evolve(layout)
    state = ''
    for row in layout:
        state += ''.join(row)
    
    

    if any(state == t for t in state_track):
        print('FOUND!')
        for row in layout:
            print(''.join(row))
        break

    state_track.append(state)

res = 0
for i in range(len(state)):
    if state[i] == '#':
        res += 2**i
print(state)
print(res)

