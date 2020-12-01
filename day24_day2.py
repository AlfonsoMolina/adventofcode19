input_data = '''#####
...##
#.?#.
#....
#...#'''

layout = [list(row) for row in input_data.split('\n')]

layout = {0:layout}

def create_new_level():
    new = [['.' for t in row] for row in input_data.split('\n')]
    new[2][2] = '?'
    return new

def evolve(layout):
    new_layout = {}
    for level in layout:
        new_level = []
        for y in range(5):
            new_level.append(layout[level][y][:])
            for x in range(5):
                if x == 2 and y ==2 :
                    continue
                bugs = 0
                for i, j in [[1,0], [-1,0], [0,-1], [0,1]]:
                    if not 0 <= y+i < 5 or not 0 <= x+j < 5:
                        continue
                    bugs += 1 if layout[level][y+i][x+j] == '#' else 0
                
                # Check upper and lower grids
                if x == 0:
                    if level-1 in layout:
                        bugs += 1 if layout[level-1][2][1] == '#' else 0
                    elif 0 < sum(1 for row in layout[level] if row[0] == '#') < 3:
                        if level-1 not in new_layout:
                            new_layout[level-1] = create_new_level()
                        new_layout[level-1][2][1] = '#'
                elif x == 4:
                    if level-1 in layout:
                        bugs += 1 if layout[level-1][2][3] == '#' else 0
                    elif 0 < sum(1 for row in layout[level] if row[4] == '#') < 3:
                        if level-1 not in new_layout:
                            new_layout[level-1] = create_new_level()
                        new_layout[level-1][2][3] = '#'
                if y == 0:
                    if level-1 in layout:
                        bugs += 1 if layout[level-1][1][2] == '#' else 0
                    elif 0 < sum(1 for tile in layout[level][0] if tile == '#') < 3:
                        if level-1 not in new_layout:
                            new_layout[level-1] = create_new_level()
                        new_layout[level-1][1][2] = '#'
                elif y == 4:
                    if level-1 in layout:
                        bugs += 1 if layout[level-1][3][2] == '#' else 0
                    elif 0 < sum(1 for tile in layout[level][4] if tile == '#') < 3:
                        if level-1 not in new_layout:
                            new_layout[level-1] = create_new_level()
                        new_layout[level-1][3][2] = '#'



                if x == 1 and y == 2:
                    if level+1 in layout:
                        bugs += sum(1 for row in layout[level+1] if row[0] == '#')
                    elif layout[level][y][x] == '#':
                        if level+1 not in new_layout:
                            new_layout[level+1] = create_new_level()
                        for yy in new_layout[level+1]:
                            yy[0] = '#'
                elif x == 3 and y == 2:
                    if level+1 in layout:
                        bugs += sum(1 for row in layout[level+1] if row[4] == '#')
                    elif layout[level][y][x] == '#':
                        if level+1 not in new_layout:
                            new_layout[level+1] = create_new_level()
                        for yy in new_layout[level+1]:
                            yy[4] = '#'
                elif x == 2 and y == 1:
                    if level+1 in layout:
                        bugs += sum(1 for tile in layout[level+1][0] if tile == '#')
                    elif layout[level][y][x] == '#':
                        if level+1 not in new_layout:
                            new_layout[level+1] = create_new_level()
                        for i in range(len(new_layout[level+1][0])):
                            new_layout[level+1][0][i] = '#'
                elif x == 2 and y == 3:
                    if level+1 in layout:
                        bugs += sum(1 for tile in layout[level+1][4] if tile == '#')
                    elif layout[level][y][x] == '#':
                        if level+1 not in new_layout:
                            new_layout[level+1] = create_new_level()
                        for i in range(len(new_layout[level+1][4])):
                            new_layout[level+1][4][i] = '#'


                if layout[level][y][x] == '#' and bugs != 1:
                    new_level[y][x] = '.'
                elif layout[level][y][x] == '.' and 0 < bugs < 3:
                    new_level[y][x] = '#'

        new_layout[level] = new_level
    return new_layout


for i in range(200):
    print(i)
    layout = evolve(layout)
    
bugs = 0
for level in layout:
    bugs += sum(1 for row in layout[level] for tile in row if tile == '#')

print(bugs)
