from itertools import permutations

input_data = '''########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################'''

with open('adventofcode/day18_input.txt', 'r') as f:    
    input_data = f.read()
input_data = [list(row) for row in input_data.split('\n')]

# for r in input_data:
#     print(''.join(r))

keys = ''
robots = []

m = []

for y in range(len(input_data)):
    m.append([])
    for x, value in enumerate(input_data[y]):
        m[y].append({'tile': value, 'paths' : []})
        if value in 'abcdefghijklmnopqrstuvwxyz':
            keys += value
        elif value == '@':
            robots.append({'coord':[y, x], 'keys': '', 'steps':0, 'previous':[-1, -1]})
            m[y][x][ 'tile']='.'

keys = ''.join(sorted(keys))

print(keys)
# exit()
def explore():
    new_steps = robots
    count = 0
    while new_steps:
        print(count, len(new_steps))
        count += 1

        next_steps = new_steps
        new_steps = []
        new_paths = []
        for step in next_steps:
            y = step['coord'][0]
            x = step['coord'][1]
            new_step = {'keys': step['keys'], 'previous': [y, x], 'steps': step['steps'] +1}
            if step['keys'] in m[y][x]['paths']:
                continue
            else: 
                # new_paths.append([y+i, x+j, step['keys']])
                m[y][x]['paths'].append(step['keys'])
            for i, j in [[1,0], [-1,0], [0,-1], [0,1]]:

                if not 0 <= y+i < len(m) or not 0 <= x+j < len(m[0]):
                    continue

                if step['previous'] == [y+i, x+j]:
                    continue

                tile = m[y+i][x+j]['tile']
                ns = dict(new_step)
                
                if tile == '#':
                    continue

                if tile in keys:
                    ns['keys'] = str(new_step['keys'])

                    if tile not in step['keys']:
                        ns['keys'] = ''.join(sorted(ns['keys']+tile))
                        if ns['keys'] == keys:
                            print('FOUND: ', ns)
                            exit()
                        ns['previous'] = [-1, -1]
                    ns['coord'] = [y+i, x+j]
                    new_steps.append(ns)
                elif tile.lower() in keys: # door
                    if tile.lower() in step['keys']:
                        ns['coord'] = [y+i, x+j]
                        new_steps.append(ns)
                elif tile == '.' or tile == '*':
                    ns['coord'] = [y+i, x+j]
                    new_steps.append(ns)
        
        for np in new_paths:
            if np[2] not in m[np[0]][np[1]]['paths']:
                m[np[0]][np[1]]['paths'].append(np[2])

            

explore()


