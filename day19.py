
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
            yield
            res = in_data
            for ch in 'RL,':
                res.replace(ch, str(ord(ch)))
            res += '10'
            res = int(res)
            code[args[0]] = res
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

in_data = '0'
with open('adventofcode/day19_input.txt', 'r') as f:    
    input_data = f.read()
code = {}
for i, x in enumerate(input_data.split(',')):
    code[i] = int(x)
func_iter = read_code(code.copy())

max_range = 200
mapa = [['.' for x in range(max_range)] for y in range(max_range)]
count = 0

def get_beam(x, y):
    global in_data
    func_iter = read_code(code.copy())
    next(func_iter)
    in_data = str(x)
    next(func_iter)
    in_data = str(y)
    return next(func_iter)

start_x = 3
start_y = 4

while True:
    print(start_x)
    start_y += 3
    while True:
        if get_beam(start_x, start_y):
            break
        start_y -= 1
    
    if start_y > 100 and get_beam(start_x, start_y - 99) and get_beam(start_x + 99, start_y) and get_beam(start_x + 99, start_y - 99):
            break

    start_x += 1

print(start_x, start_y-99)

# for x in range(max_range):
#     for y in range(max_range):
        
#         # with open('adventofcode/day19_input.txt', 'r') as f:    
#         #     input_data = f.read()
#         # code = {}
#         # for i, c in enumerate(input_data.split(',')):
#         #     code[i] = int(c)
#         func_iter = read_code(code.copy())
#         next(func_iter)
#         in_data = str(x)
#         next(func_iter)
#         in_data = str(y)
#         res = next(func_iter)
#         count += res
#         mapa[y][x] = '#' if res else '.'

# for r in mapa:
#     print(''.join(r))


# mapp = []
# mapp.append([])
# try:
#     while True:
#         out = next(func_iter)
#         if out:
#             if out == 10:
#                 mapp.append([])
#             else:
#                 mapp[-1].append(out)

# except StopIteration:
#     print('Stopped')  
# except RecursionError:
#     pass

# mapp = mapp[:-2]
# for m in mapp:
#     mmm = [chr(mm) for mm in m]
#     print(''.join(mmm))


# coord = []
# for i in range(1,len(mapp)-1):
#     for j in range(1, len(mapp[0])-1):
#         if mapp[i][j] == 35:
#             if all(m == 35 for m in [mapp[i-1][j], mapp[i+1][j], mapp[i][j-1], mapp[i][j+1]]):
#                 coord.append(i*j)

# print(sum(coord))


