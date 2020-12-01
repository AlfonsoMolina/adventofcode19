from itertools import permutations
from copy import deepcopy
import time
start_time = time.time()

input_data = '''#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba@#@BcIJ#
#############
#nK.L@#@G...#
#M###N#H###.#
#o#m..#i#jk.#
#############'''


with open('adventofcode/day18_input2.txt', 'r') as f:    
    input_data = f.read()
input_data = [list(row) for row in input_data.split('\n')]

# for r in input_data:
#     print(''.join(r))

keys = ''
robot = {'coord':[], 'keys': '', 'steps':0, 'previous':[[-1, -1],[-1, -1],[-1, -1],[-1, -1]], 'current_q': 0}
doors_for_q = ['', '', '', '']
keys_for_q = ['', '', '', '']
m = []

for y in range(len(input_data)):
    m.append([])
    for x, value in enumerate(input_data[y]):
        m[y].append({'tile': value, 'paths' : []})
        if value in 'abcdefghijklmnopqrstuvwxyz':
            keys += value
            if y < len(input_data)/2 and x < len(input_data[y])/2:
                keys_for_q[0] += value
            elif y < len(input_data)/2 and x > len(input_data[y])/2:
                keys_for_q[1] += value
            elif x < len(input_data[y])/2:
                keys_for_q[2] += value
            else:
                keys_for_q[3] += value
        elif value in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if y < len(input_data)/2 and x < len(input_data[y])/2:
                doors_for_q[0] += value
            elif y < len(input_data)/2 and x > len(input_data[y])/2:
                doors_for_q[1] += value
            elif x < len(input_data[y])/2:
                doors_for_q[2] += value
            else:
                doors_for_q[3] += value
        elif value == '@':
            robot['coord'].append([y, x])
            m[y][x][ 'tile']='.'

keys = ''.join(sorted(keys))

# exit()
def explore():
    new_steps = []
    for i in range(4):
        r = deepcopy(robot)
        r['current_q'] = i
        new_steps.append(r)
    count = 0
    while new_steps:
        print(count, len(new_steps))
        count += 1

        # coords = []
        # for n in new_steps:
        #     if 'abcde'.startswith(n['keys']):
        #         print(n)
        #         coords.append(n['coord'][n['current_q']])
        # for y in range(len(m)):
        #     r = ''
        #     for x in range(len(m[0])):
        #         if [y, x] in coords:
        #             r += '@' 
        #         else:
        #             r += m[y][x]['tile']
        #     print(r)

        # input()
        next_steps = new_steps
        new_steps = []
        for step in next_steps:
            c = step['current_q']
            y = step['coord'][c][0]
            x = step['coord'][c][1]
            new_step = {'keys': step['keys'], 'previous': step['previous'], 'steps': step['steps'] +1, 'coord': step['coord'], 'current_q': c}
            new_step['previous'][c] = [y, x]
            if step['keys'] in m[y][x]['paths']:
                continue
            else: 
                m[y][x]['paths'].append(step['keys'])
                # m[y][x]['paths'].append(step['keys'])
            for i, j in [[0,-1], [0,1], [1,0], [-1,0]]:
                if not 0 <= y+i < len(m) or not 0 <= x+j < len(m[0]):
                    continue

                if step['previous'][c] == [y+i, x+j]:
                    continue
                
                # h = (y+i)*100 + (x+j)
                # if h in step['hist'] and step['hist'][h] == step['keys']:
                #     continue
                # else:
                #     step['hist'][h] = step['keys']

                tile = m[y+i][x+j]['tile']
                ns = deepcopy(new_step)
                                    
                if tile == '#':
                    continue

                if tile in keys:
                    ns['keys'] = str(new_step['keys'])
                    ns['coord'][c] = [y+i, x+j]

                    if tile not in step['keys']:
                        ns['keys'] = ns['keys']+tile
                        if ''.join(sorted(ns['keys'])) == keys:
                            print('FOUND: ', ns)
                            print("--- %s seconds ---" % (time.time() - start_time))
                            exit()
                        ns['previous'] = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
                        # Look up for other quadrants:
                        for q in range(4):
                            if q == c:
                                continue
                            if tile.upper() in doors_for_q[q]: # or not any(k in keys_for_q[q] for k in step['keys']):
                                nns = deepcopy(ns)
                                nns['current_q'] = q
                                new_steps.append(nns)
                    new_steps.append(ns)

                elif tile.lower() in keys: # door
                    if tile.lower() in step['keys']:
                        ns['coord'][c] = [y+i, x+j]
                        new_steps.append(ns)
                elif tile == '.' or tile == '*':
                    ns['coord'][c] = [y+i, x+j]
                    new_steps.append(ns)

            

explore()


