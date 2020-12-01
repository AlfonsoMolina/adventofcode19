def read_code(code):
    index = 0
    
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
            code[args[0]] = int(input('Insert input: '))
            index += 2
        elif cmd == 4:            
            print(code[args[0]])
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
    return(code)

# input_data = ['1,0,0,0,99', '2,3,0,3,99', '2,4,4,5,99,0', '1,1,1,4,99,5,6,0,99']
# for input in input_data:
#     code = [int(x) for x in input.split(',')]
#     res = read_code(code)
#     res_str = [str(x) for x in res]
#     print(",".join(res_str))

with open('adventofcode/day4_input.txt', 'r') as f:    
    input_data = f.read()
# input_data = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
input_data = [int(x) for x in input_data.split(',')]
res = read_code(input_data)
