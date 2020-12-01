def read_code(code):
    index = 0
    cmd = code[0]
    while True:
        if cmd == 1:
            code[code[index+3]] = code[code[index+1]] + code[code[index+2]]
            index += 4
            cmd = code[index]
        elif cmd == 2:
            code[code[index+3]] = code[code[index+1]] * code[code[index+2]]
            index += 4
            cmd = code[index]
        elif cmd == 99:
            break
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

with open('adventofcode/day2_input.txt', 'r') as f:    
    input_data = f.read()
input_data = [int(x) for x in input_data.split(',')]
for i in range(0,100):
    for j in range(0,100):
        code = input_data[:]
        code[1] = i
        code[2] = j
        res = read_code(code)
        if res[0] == 19690720:
            print(i)
            print(j)
            print(100*i + j)
            break