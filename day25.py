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
            yield
            res = in_data
            code[args[0]] = res
            index += 2
        elif cmd == 4: 
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
with open('adventofcode/day25_input.txt', 'r') as f:    
    input_data = f.read()
code = {}
for i, x in enumerate(input_data.split(',')):
    code[i] = int(x)
func_iter = read_code(code.copy())

output = ''
try:
    out = next(func_iter)
    while True:
        output = ''
        if out is None:
            command = input()
            command = [ord(c) for c in command]
            command.append(10)
            while out is None:
                in_data = command[0]
                command = command[1:] 
                out = next(func_iter)
        if out is not None:
            while out is not None:
                output += chr(out)
                out = next(func_iter)
            print(output)
except StopIteration:
    print('Stopped') 