from itertools import permutations

input_data = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""


with open('adventofcode/day18_input.txt', 'r') as f:    
    input_data = f.read()
input_data = [list(row) for row in input_data.split('\n')]


keys = ''
robot = [0,0]
for y in range(len(input_data)):
    for x, value in enumerate(input_data[y]):
        if value in 'abcdefghijklmnopqrstuvwyz':
            keys += value
        elif value == '@':
            robot = [y, x]
            input_data[y][x]='.'

def get_next_perm(keys, failed_paths):
    for p in permutations(keys):
        p_str = ''.join(p)

        if not any(p_str.startswith(fp) for fp in failed_paths):
            yield(p)

min_path = 99999999999

tested_paths = {}


def explore(keys_found, next_step, count):
    global min_path, good_paths
    print(keys_found, count)
    # print('EXPLORE: ', keys_found, next_step, count)

    if len(keys_found) in tested_paths:
        for path in tested_paths[len(keys_found)]:
            p, dist = path
            if all(k in path for k in keys_found) and p[-1] == keys_found[-1]:
                if count > dist:
                    return
                else:
                    path[1] = count
                break
        else:
            tested_paths[len(keys_found)].append([keys_found, count])
    else:
        tested_paths[len(keys_found)] = [[keys_found, count]]


    m = input_data
    m = [['.' if any(t.lower() == k for k in keys_found) else t for t in r] for r in m]
    next_steps = [next_step]
    m[next_step[0]][next_step[1]] = 'x'
    # while True:
    end = 0 # 1 found end, 2 failed
    while not end:
        ns = next_steps[:]
        next_steps = []
        count += 1
        if count >= min_path:
            break
        # for r in m:
        #     print(''.join(r))
        for y, x in ns:
            for i, j in [[1,0], [-1,0], [0,-1], [0,1]]:
                if not 0 <= y+i < len(m) or not 0 <= x+j < len(m[0]):
                    continue
                tile = m[y+i][x+j]
                if any(tile == k for k in keys):
                    
                    if len(keys_found) +1 == len(keys):
                        end = 1
                        keys_found += tile
                        break
                    else:
                        explore(keys_found + tile, [y+i, x+j], count)
                        # print('Fuera de explore con ', keys_found)
                elif tile == '.':
                    next_steps.append([y+i,x+j])
                    m[y+i][x+j] = 'x'
            else:
                continue
            break
        if not end and not next_steps:
            end = 2
            if len(keys_found) in tested_paths:
                tested_paths[len(keys_found)].append([keys_found, count])
            else:
                tested_paths[len(keys_found)] = [[keys_found, count]]
        # print('Next steps: ', next_steps)

    if end == 1:
        good_paths[keys_found] = count
        if count < min_path:
            min_path = count
        print('For ' + keys_found + ' count is ' + str(count))

count = 0
keys_found = ''
# next_perms = iter(get_next_perm(keys, failed_paths))
good_paths = {}
explore(keys_found,robot,0)


print('-'*10)
for keys in good_paths.keys():
    print(keys, good_paths[keys])
    
print(min_path)
# Explore map
# for p in next_perms:
    # print('Testing ', p)
    # m = [r[:] for r in input_data[:]]
    # next_steps = [robot]
    # m[robot[0]][robot[1]] = 'x'
    # p = list(p)
    # keys_found = ''
    # # while True:
    # count = 0
    # end = 0 # 1 found end, 2 failed
    # while not end:
    #     ns = next_steps[:]
    #     next_steps = []
    #     count += 1
    #     if count > min_path:
    #         failed_paths.append(keys_found+ p[0])
    #         break
    #     # for r in m:
    #     #     print(''.join(r))
    #     for y, x in ns:
    #         for i, j in [[0,1], [0,-1], [-1,0], [1,0]]:
    #             if not 0 <= y+i < len(m) or not 0 <= x+j < len(m[0]):
    #                 continue
    #             tile = m[y+i][x+j]
    #             if tile == p[0]:
    #                 m = [['.' if t == 'x' or t.lower() == tile else t for t in r] for r in m]
    #                 m[y+i][x+j] = 'x'
    #                 p = p[1:]
    #                 keys_found += tile
    #                 if not p:
    #                     end = 1
    #                     break
    #                 else:
    #                     next_steps = [[y+i, x+j]]
    #                     break
    #             elif tile == '.':
    #                 next_steps.append([y+i,x+j])
    #                 m[y+i][x+j] = 'x'
    #         else:
    #             continue
    #         break
    #     if not end and not next_steps:
    #         end = 2
    #         failed_paths.append(keys_found + p[0])

    #     # print('Next steps: ', next_steps)

    # if end == 1:
    #     good_paths[keys_found] = count
    #     if count < min_path:
    #         min_path = count
    #     print('For ' + keys_found + ' count is ' + str(count))
    


    