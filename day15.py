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
            # res = input(':')
            # if res == 'a':
            #     in_data = -1
            # if res == 'd':
            #     in_data = 1
            # if res == 's':
            #     in_data = 0
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

in_data = 0
with open('adventofcode/day15_input.txt', 'r') as f:    
    input_data = f.read()
code = {}
for i, x in enumerate(input_data.split(',')):
    code[i] = int(x)

func_iter = read_code(code)
canvas = {}

x, y = 0, 0
status = -1
def draw(canvas):
    mapita = []
    max_x = max(int(k.split(',')[0]) for k in canvas)
    min_x = min(int(k.split(',')[0]) for k in canvas)
    max_y = max(int(k.split(',')[1]) for k in canvas)
    min_y = min(int(k.split(',')[1]) for k in canvas)
    for i in range(max_y, min_y-1, -1):
        # row = [str(i) if i < 0 else '+' + str(i)]
        row = []
        for j in range(min_x, max_x+1):
            loc = f'{j},{i}'
            if loc in canvas:
                tile = canvas[loc]
                if j == 0 and i == 0:
                    tile = '/'
                elif tile == 2:
                    tile = '#'
                elif tile == 0:
                    tile = '█'
                elif tile == 1:
                    tile = ' '
                elif tile == 3:
                    tile = 'O'
                row.append(tile)
            else:
                row.append('?')
        mapita.append(row)
    first_row = [str(i) if i < 0 else '+' + str(i) for i in range(min_x, max_x+1)]
    first_row = [''] + first_row
    # print(' '.join(first_row))
    for row in mapita:
        print(' '.join(row))

def explore(x, y):
    global in_data
    for xx, yy, dire in [[x+1,y,4],[x-1,y,3],[x,y-1,2],[x,y+1,1]]:
        if f'{xx},{yy}' not in canvas:
            in_data = dire
            status = next(func_iter)
            canvas[f'{xx},{yy}'] = status
            if status != 0:
                explore(xx, yy)
                in_data = 3 if dire == 4 else (4 if dire == 3 else (1 if dire == 2 else (2 if dire == 1 else 0)))
                next(func_iter)
def find(x,y, px, py):    
    paths = []
    print(x,y)
    for xx, yy in [[x+1,y],[x-1,y],[x,y-1],[x,y+1]]:
        if xx == px and yy == py:
            continue
        if canvas[f'{xx},{yy}'] == 2:
            return 1
        elif canvas[f'{xx},{yy}'] == 1:
            res = find(xx,yy, x, y)
            if res:
                paths.append(res)
    if paths:
        return min(paths) + 1
    else:
        return 0

def oxygen():
    count = 0
    finished = False
    while not finished:
        finished = True
        oxygen_rooms = [key for key in canvas if canvas[key] == 3]
        for loc in oxygen_rooms:
            x = int(loc.split(',')[0])
            y = int(loc.split(',')[1])
            for xx, yy in [[x+1,y],[x-1,y],[x,y-1],[x,y+1]]:
                if canvas[f'{xx},{yy}'] == 1:
                    canvas[f'{xx},{yy}'] = 3
                    finished = False
        count += 1
    return count-1

try:
    explore(0, 0)
    
except StopIteration:
    print('Stopped')  
except RecursionError:
    pass

# draw(canvas)
# print(find(0,0,0,0))
for key in canvas:
    if canvas[key] == 2:
        canvas[key] = 3
print(oxygen())
# try:
#     while status != 0:
#         while status != 0:
#             in_data = 1
#             y += 1
#             status = next(func_iter)
#             canvas[f'{x},{y}'] = status
#             if status == 0:
#                 y -= 1
#         status = -1
#         while status != 0:
#             in_data = 2
#             y -= 1
#             status = next(func_iter)
#             canvas[f'{x},{y}'] = status
#             if status == 0:
#                 y += 1
#         while y != 0:
#             in_data = 1
#             status = next(func_iter)
#             y += 1

#         in_data = 3
#         x -= 1
#         status = next(func_iter)
#         canvas[f'{x},{y}'] = status
#         if status == 0:
#             x += 1

#     while x != 0:
#         in_data = 4
#         next(func_iter)
#         x += 1

#     status = -1
#     while status != 0:
#         while status != 0:
#             in_data = 1
#             y += 1
#             status = next(func_iter)
#             canvas[f'{x},{y}'] = status
#             if status == 0:
#                 y -= 1
#         status = -1
#         while status != 0:
#             in_data = 2
#             y -= 1
#             status = next(func_iter)
#             canvas[f'{x},{y}'] = status
#             if status == 0:
#                 y += 1
#         while y != 0:
#             in_data = 1
#             status = next(func_iter)
#             y += 1

#         in_data = 4
#         x += 1
#         status = next(func_iter)
#         canvas[f'{x},{y}'] = status
#         if status == 0:
#             x -= 1

# except StopIteration:
#     pass
