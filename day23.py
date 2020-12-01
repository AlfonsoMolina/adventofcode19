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
            res = in_data
            yield
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
with open('adventofcode/day23_input.txt', 'r') as f:    
    input_data = f.read()
code = {}
for i, x in enumerate(input_data.split(',')):
    code[i] = int(x)
func_iter = read_code(code.copy())

hosts = [read_code(code.copy()) for i in range(50)]

NAT = None
NAT_previous = [0,0,0]

queue = []
# Start hosts
for i in range(50):
    in_data = i
    next(hosts[i])

while True:
    idle = True
    for i in range(50):
        print('HOST ', i)
        packet = None
        for j in range(len(queue)):
            if queue[j][0] == i:
                packet = queue.pop(j)
                in_data = packet[1]
                break
        else:
            in_data = -1
        while True:
            out = next(hosts[i])
            if out is None: # reading
                if in_data == -1:
                    break
                else:
                    idle = False
                    print('RECEIVE ', packet)
                    in_data = packet[2]
                    next(hosts[i])

                    # Prepare next packet
                    packet = None
                    for j in range(len(queue)):
                        if queue[j][0] == i:
                            packet = queue.pop(j)
                            in_data = packet[1]
                            break
                    else:
                        in_data = -1

            if out is not None: # sending
                idle = False
                new_p = [out, next(hosts[i]), next(hosts[i])]
                print('SEND ', new_p)
                if new_p[0] == 255:
                    NAT = new_p
                    NAT[0] = 0
                else:
                    queue.append(new_p)

    if idle and NAT:
        queue.append(NAT)
        print('NAT: ', new_p)
        print('Previous: ', NAT_previous)
        if all(NAT[k] == NAT_previous[k] for k in range(3)):
            print('FOUND IT: ', new_p)
            input()
        NAT_previous = NAT