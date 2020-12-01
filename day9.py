def read_code(code, in_data=[]):
    index = 0
    in_count = 0
    rel_base = 0
    out = []
    while True:
        cmd = int(str(code[index])[-2:])
        # print(code)
        # print('index : ', index, ', base: ', rel_base)
        modes = [int(ch) for ch in str(code[index])[:-2]]
        # 1 argsument
        total = 0
        if cmd in [1, 2, 7, 8]:
            total = 3
        if cmd in [5, 6]:
            total = 2
        if cmd in [3, 4, 9]:
            total = 1
        args = [0] * total
        # print('cmd : ', cmd, ', modes: ', modes)

        for i in range (1, total+1):
            if len(modes) >= i and modes[-i] == 1: # Inmediate
                args[i-1] = index + i 
            elif len(modes) >= i and modes[-i] == 2: # Position
                args[i-1] = rel_base + code[index+i]
            else: # Relative
                args[i-1] = code[index+i]
            if args[i-1] not in code:
                code[args[i-1]] = 0
        # print('args: ', args)
        if cmd == 1:
            code[args[2]] = code[args[0]] + code[args[1]]
            index += 4
        elif cmd == 2:
            code[args[2]] = code[args[0]] * code[args[1]]
            index += 4
        elif cmd == 3:
            code[args[0]] = in_data[in_count]
            in_count += 1
            print('Insert input: ', code[args[0]])
            index += 2
        elif cmd == 4:            
            print('Output: ', code[args[0]])
            out.append(code[args[0]])
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
            break
        else:
            print('ERROR')
            break
    return(out)

with open('adventofcode/day9_input.txt', 'r') as f:    
    input_data = f.read()
# input_data = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
# input_data = '104,1125899906842624,99'
code = {}
for i, x in enumerate(input_data.split(',')):
    code[i] = int(x)
read_code(code, [2])
