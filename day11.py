in_data = 0
def read_code(code):
    global in_data
    
    index = 0
    rel_base = 0
    while True:
        cmd = int(str(code[index])[-2:])
        modes = [int(ch) for ch in str(code[index])[:-2]]
        # 1 argument
        total = 0
        if cmd in [1, 2, 7, 8]:
            total = 3
        if cmd in [5, 6]:
            total = 2
        if cmd in [3, 4, 9]:
            total = 1
        args = [0] * total

        for i in range (1, total+1):
            if len(modes) >= i and modes[-i] == 1: # Inmediate
                args[i-1] = index + i 
            elif len(modes) >= i and modes[-i] == 2: # Position
                args[i-1] = rel_base + code[index+i]
            else: # Relative
                args[i-1] = code[index+i]
            if args[i-1] not in code:
                code[args[i-1]] = 0
        if cmd == 1:
            code[args[2]] = code[args[0]] + code[args[1]]
            index += 4
        elif cmd == 2:
            code[args[2]] = code[args[0]] * code[args[1]]
            index += 4
        elif cmd == 3:
            code[args[0]] = in_data
            # print('Insert input: ', code[args[0]])
            index += 2
        elif cmd == 4:         
            # print('Output: ', code[args[0]])
            yield code[args[0]]
            index += 2
        elif cmd == 5:            
            if code[args[0]] != 0:
                index = code[args[1]]
            else:
                index += 3
        elif cmd == 6:            
            if code[args[0]] == 0:
                index = code[args[1]]
            else:
                index += 3
        elif cmd == 7:
            if code[args[0]] < code[args[1]]:
                code[args[2]] = 1
            else:
                code[args[2]] = 0
            index += 4
        elif cmd == 8:
            if code[args[0]] == code[args[1]]:
                code[args[2]] = 1
            else:
                code[args[2]] = 0
            index += 4
        elif cmd == 9:
            rel_base += code[args[0]]
            index += 2
        elif cmd == 99:
            yield None
            break
        else:
            print('ERROR')
            break

if __name__ == '__main__':
    with open('adventofcode/day11_input.txt', 'r') as f:    
        input_data = f.read()
    code = {}
    for i, x in enumerate(input_data.split(',')):
        code[i] = int(x)
    func_iter = read_code(code)
    output = ''
    robot_pos = [0,0]
    robot_dir = 'U'
    hull = {'0,0': [1, False]}
    while output is not None:
        pos_key = str(robot_pos[0]) + ',' + str(robot_pos[1])
        in_data = hull[pos_key][0]
        output = next(func_iter)
        if output is None:
            break
        hull[pos_key] = [output, True]
        output = next(func_iter)
        if output is None:
            break
        if output == 0:
            if robot_dir == 'U':
                robot_dir = 'L'
                robot_pos[0] -= 1
            elif robot_dir == 'D':
                robot_dir = 'R'
                robot_pos[0] += 1
            elif robot_dir == 'L':
                robot_dir = 'D'
                robot_pos[1] -= 1
            elif robot_dir == 'R':
                robot_dir = 'U'
                robot_pos[1] += 1
        elif output == 1:
            if robot_dir == 'U':
                robot_dir = 'R'
                robot_pos[0] += 1
            elif robot_dir == 'D':
                robot_dir = 'L'
                robot_pos[0] -= 1
            elif robot_dir == 'L':
                robot_dir = 'U'
                robot_pos[1] += 1
            elif robot_dir == 'R':
                robot_dir = 'D'
                robot_pos[1] -= 1
        else:
            print('ERRRRROR')
            break
        pos_key = str(robot_pos[0]) + ',' + str(robot_pos[1])
        if pos_key not in hull:
            hull[pos_key] = [0, False]
    max_x = max(int(h.split(',')[0]) for h in hull)+2
    min_x = min(int(h.split(',')[0]) for h in hull)-2
    max_y = max(int(h.split(',')[1]) for h in hull)+2
    min_y = min(int(h.split(',')[1]) for h in hull)-2
    l = [1 for h in hull if hull[h][1]]
    paint = []
    for y in range(max_y , min_y-1, -1):
        row = []
        for x in range(min_x, max_x +1):
            pos_key = str(x) + ',' + str(y)
            if pos_key == str(robot_pos[0]) + ',' + str(robot_pos[1]):
                row.append('+')
            elif pos_key in hull:
                row.append('.' if hull[pos_key][0] == 0 else '#')
            else:
                row.append('.')
        paint.append(row)

    for row in paint:
        print(' '.join(row))
    print(sum(l))