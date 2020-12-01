input_data = """         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       """

input_data = """                   A               
                   A               
  #################.#############  
  #.#...#...................#.#.#  
  #.#.#.###.###.###.#########.#.#  
  #.#.#.......#...#.....#.#.#...#  
  #.#########.###.#####.#.#.###.#  
  #.............#.#.....#.......#  
  ###.###########.###.#####.#.#.#  
  #.....#        A   C    #.#.#.#  
  #######        S   P    #####.#  
  #.#...#                 #......VT
  #.#.#.#                 #.#####  
  #...#.#               YN....#.#  
  #.###.#                 #####.#  
DI....#.#                 #.....#  
  #####.#                 #.###.#  
ZZ......#               QG....#..AS
  ###.###                 #######  
JO..#.#.#                 #.....#  
  #.#.#.#                 ###.#.#  
  #...#..DI             BU....#..LF
  #####.#                 #.#####  
YN......#               VT..#....QG
  #.###.#                 #.###.#  
  #.#...#                 #.....#  
  ###.###    J L     J    #.#.###  
  #.....#    O F     P    #.#...#  
  #.###.#####.#.#####.#####.###.#  
  #...#.#.#...#.....#.....#.#...#  
  #.#####.###.###.#.#.#########.#  
  #...#.#.....#...#.#.#.#.....#.#  
  #.###.#####.###.###.#.#.#######  
  #.#.........#...#.............#  
  #########.###.###.#############  
           B   J   C               
           U   P   P               """

with open('adventofcode/day20_input.txt', 'r') as f:    
    input_data = f.read()

input_data = [list(row) for row in input_data.split('\n')]
print(input_data)
parsed_data = {}

start_x, start_y = 0, 0
end_x, end_y = 0, 0

def surr_tiles(y,x, input_data):
    res = []
    if y < len(input_data) -1:
        res.append(input_data[y+1][x])
    if x < len(input_data[y]) -1:
        res.append(input_data[y][x+1])
    if y > 0:
        res.append(input_data[y-1][x])
    if x > 0:
        res.append(input_data[y][x-1])
    return res

def char_in_surr_tiles(char, y,x, input_data):
    if y < len(input_data) -1 and input_data[y+1][x] in char:
        return y+1, x
    if x < len(input_data[y]) -1 and input_data[y][x+1] in char:
        return y, x+1
    if y > 0 and input_data[y-1][x] in char:
        return y-1, x
    if x > 0 and input_data[y][x-1] in char:
        return y, x-1
    return None

portals = {}

for y in range(len(input_data)):
    parsed_data[y] = {}
    for x in range(len(input_data[y])):
        parsed_data[y][x] = {}
        tile = input_data[y][x]
        if tile in '#. ':
            parsed_data[y][x] = {'tile': tile, 'steps': 99999}
        elif tile in 'A' and 'A' in surr_tiles(y, x, input_data):
            if '.' in surr_tiles(y, x, input_data):
                start_y, start_x = char_in_surr_tiles('.', y, x, input_data)
                parsed_data[y][x] = {'tile': '@', 'steps': 99999}
        elif tile in 'Z' and 'Z' in surr_tiles(y, x, input_data):
            if '.' in surr_tiles(y, x, input_data):
                parsed_data[y][x] = {'tile': '$', 'steps': 99999}
                end_x, end_y = x, y
        elif tile in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if '.' in surr_tiles(y, x, input_data):
                # print(y, x)
                # print(tile)
                # print(surr_tiles(y, x, input_data))
                # print(char_in_surr_tiles('ABCDEFGHIJKLMNOPQRSTUVWXYZ', y, x, input_data))
                # print(input_data[other_tile_y][other_tile_x])
                other_tile_y, other_tile_x = char_in_surr_tiles('ABCDEFGHIJKLMNOPQRSTUVWXYZ', y, x, input_data)
                if other_tile_y < y or other_tile_x < x:
                    code = input_data[other_tile_y][other_tile_x] + tile
                else:
                    code = tile + input_data[other_tile_y][other_tile_x]
                parsed_data[y][x] = {'tile': '*', 'portal': code, 'steps': 99999}
                if code not in portals:
                    portals[code] = [y,x]
                else:
                    portals[code].extend([y,x])

for y in range(len(input_data)):
    row = ''
    for x in range(len(input_data[y])):
        if 'tile' in parsed_data[y][x]:
            row += parsed_data[y][x]['tile']
        else:
            row += ' '
    print(row)
print(portals)

# explore(parsed_data, [start_y, start_x], 0)

# def explore(parsed_data, robot, steps):

next_steps = [[start_y, start_x, 0]]

while next_steps:
    ns = next_steps[:]
    next_steps = []
    for robot in ns:
        y, x, steps = robot
        parsed_data[y][x]['steps'] = steps
        for i, j in [[1,0], [-1,0], [0,-1], [0,1]]:
            if not 0 <= y+i < len(input_data) or not 0 <= x+j < len(input_data[0]):
                continue
            elif not 'tile' in parsed_data[y+i][x+j]:
                continue
            tile = parsed_data[y+i][x+j]['tile']
            if tile == '.':
                if parsed_data[y+i][x+j]['steps'] > steps+1:
                    next_steps.append([y+i,x+j, steps+1])
            if tile == '*':
                code = parsed_data[y+i][x+j]['portal']
                y1, x1, y2, x2 = portals[code]
                if y1 == y+i and x1 == x+j:
                    next_steps.append([y2,x2, steps])
                else:
                    next_steps.append([y1,x1, steps])
            if tile == '$':
                print('SOL: ', steps)
                next_steps = None
                exit()
                