from itertools import permutations

def read_code(code, in_data):
    index = 0
    in_count = 0
    print(in_data)
    out = []
    while True:
        cmd = int(str(code[index])[-2:])
        modes = [int(ch) for ch in str(code[index])[:-2]]
        args = [0, 0, 0, 0]
        # 1 argsument
        total = 0
        if cmd in [1, 2, 7, 8]:
            total = 3
        if cmd in [5, 6]:
            total = 2
        if cmd in [3, 4]:
            total = 1

        for i in range (1, total+1):
            if len(modes) >= i and modes[-i] == 1:
                args[i-1] = index + i 
            else:
                args[i-1] = code[index+i]

        if cmd == 1:
            code[args[2]] = code[args[0]] + code[args[1]]
            index += 4
        elif cmd == 2:
            code[args[2]] = code[args[0]] * code[args[1]]
            index += 4
        elif cmd == 99:
            break
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
        else:
            print('ERROR')
            break
    return(out)

with open('adventofcode/day7_input.txt', 'r') as f:    
    input_data = f.read()
values = '01234'
output = []
for comb in permutations(values):
    freq = [int(x) for x in comb]
    res = [0]
    for f in freq:
        code = [int(x) for x in input_data.split(',')]    
        res = read_code(code,[f,res[0]])
    output.append(res)
print(max(output))
