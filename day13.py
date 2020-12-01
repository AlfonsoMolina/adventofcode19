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
with open('adventofcode/day13_input.txt', 'r') as f:    
    input_data = f.read()
code = {}
for i, x in enumerate(input_data.split(',')):
    code[i] = int(x)
func_iter = read_code(code)
output = []

score = 0
canvas = []
ball = [0,0]
paddle = 0

for y in range(24):
    c = []
    for x in range(42):
        c.append(0)
    canvas.append(c)
def draw(canvas):
    for row in canvas:
        r = ''.join([str(r) for r in row])
        r = r.replace('0','.').replace('1','#').replace('2','█').replace('3','=').replace('4','O')
        print(r)
    print(score)
    input()

try:
    count = 0
    while True:
        x, y, tile = next(func_iter), next(func_iter), next(func_iter)
        if x == -1 and y == 0:
            score = tile
        else:
            canvas[y][x] = tile
        if tile == 4:
            ball = [x,y]
        if tile == 3:
            paddle = x

        if paddle < ball[0]:
            in_data = 1
        elif paddle > ball[0]:
            in_data = -1
        else:
            in_data = 0

        # draw(canvas)




except StopIteration:
    output = output[:-2]    

draw(canvas)
print(score)
print(sum(1 for row in canvas for tile in row if tile == 2))
# print(output)