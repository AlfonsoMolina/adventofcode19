from itertools import permutations

last_output = 0

def read_code(code, freq_mode):
    global last_output
    index = 0
    in_count = 0
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
            print('HALT')
            break
        elif cmd == 3:
            if in_count == 0:
                code[args[0]] = freq_mode
            else:
                code[args[0]] = last_output
            in_count += 1
            print('Insert input: ', code[args[0]])
            index += 2
        elif cmd == 4:            
            print('Output: ', code[args[0]])
            index += 2
            yield code[args[0]]
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

with open('adventofcode/day7_input.txt', 'r') as f:    
    input_data = f.read()
# input_data = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
input_data = [int(x) for x in input_data.split(',')]
values = '56789'
output = []


for comb in permutations(values):
    freq = [int(x) for x in comb]
    ampl = []
    last_output = 0
    last_res = 0
    for i in freq:        
        ampl.append(read_code(input_data[:], i))
    end = False
    while not end:
        last_res = last_output
        for i in range(0,5):
            try:
                last_output = next(ampl[i])
            except StopIteration:
                end = True
    output.append(last_res)
print(max(output))
        
    
