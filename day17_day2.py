
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
            # res =  input(str(index) + ':')
            # # for ch in 'ABCDRLyn,':
            # #     res = res.replace(ch, str(ord(ch)))
            # # res += '10'
            # res = int(res)
            # print(res)
            code[args[0]] = in_data[0]
            in_data = in_data[1:]
            print(code[args[0]])
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
with open('adventofcode/day17_input.txt', 'r') as f:    
    input_data = f.read()
code = {}
for i, x in enumerate(input_data.split(',')):
    code[i] = int(x)
func_iter = read_code(code)

mapp = []
mapp.append([])
in_data = [65,44,66,44,65,44,67,44,66,44,67,44,65,44,66,44,65,44,67,10,82,44,54,44,76,44,49,48,44,82,44,56,44,82,44,56,10,82,44,49,50,44,76,44,56,44,76,44,49,48,10,82,44,49,50,44,76,44,49,48,44,82,44,54,44,76,44,49,48,10,110,10]
try:
    while True:
        out = next(func_iter)
        if out:
            if out == 10:
                try:
                    print(''.join( [chr(mm) for mm in mapp[-1]]))
                except:
                    pass
                mapp.append([])
            else:
                mapp[-1].append(out)

except StopIteration:
    print('Stopped')  
    try:
        print(mapp[-1])
    except:
        pass
except RecursionError:
    pass





