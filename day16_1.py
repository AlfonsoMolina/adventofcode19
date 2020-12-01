from itertools import groupby

# input_data = '59750530221324194853012320069589312027523989854830232144164799228029162830477472078089790749906142587998642764059439173975199276254972017316624772614925079238407309384923979338502430726930592959991878698412537971672558832588540600963437409230550897544434635267172603132396722812334366528344715912756154006039512272491073906389218927420387151599044435060075148142946789007756800733869891008058075303490106699737554949348715600795187032293436328810969288892220127730287766004467730818489269295982526297430971411865028098708555709525646237713045259603175397623654950719275982134690893685598734136409536436003548128411943963263336042840301380655801969822'
# input_data = '80871224585914546619083218645595'
# input_data = '03036732577212944063491565474664'
input_data = '12345678'
input_data = [int(c) for c in input_data] * 10
inp =  input_data[:]

size = len(inp)

# sum in chuncks of 10
sum_cache_mini = []
sum_cache_medium = []
sum_cache_big = []
big_chunk = 75000
medium_chunk = 50000
mini_chunk = 10000

caches = [[[], 150000], [[], 75000], [[], 10000], [[], 1000]]
# caches = [[[], 100], [[], 50], [[], 10], [[], 5]]

def suma(start, stop):
    out = 0
    for sum_cache, chunk in caches:        
        chunk_start = start // chunk +1
        chunk_stop = stop // chunk
        if chunk_start < chunk_stop:
            out += sum(sum_cache[chunk_start:chunk_stop])
            out += suma(start,chunk_start*chunk)
            out += suma(chunk_stop*chunk,stop)
            break
    else:
        out += sum(inp[start:stop])
    return out

pattern_list = []
pattern = {1: [0,1], -1:[2,3]}
for j in range(0, size):
    u1 = pattern[1][0]
    u2 = pattern[-1][0]
    if j > 0:
        u1 += 1
        u2 += 3
    pattern = {1: [u1,u1+j+1], -1:[u2,u2+j+1]}
    p =  {1: [u1,u1+j+1], -1:[u2,u2+j+1]}
    k = 0
    subpattern = []
    while True:
        if k > 0:
            u1 = p[1][0]+4*(j+1)
            u2 = p[-1][0]+4*(j+1) 
            p = {1: [u1,u1+j+1], -1:[u2,u2+j+1]}
        else: 
            u1 = p[1][0]
            u2 = p[-1][0]
        if u1 >= size:
            break
        elif u1+j+1 > (size-1):
            p[1][1] = size
            p[-1][0] = 0
            p[-1][1] = 0
        elif u2 >= size:
            p[-1][0] = 0
            p[-1][1] = 0
        elif u2+j+1 > (size-1):
            p[-1][1] = size
        subpattern.append(p)
        k += 1
    pattern_list.append(subpattern)

phases = 4
for i in range(phases):    
    print('Phase: ', i)

    pattern = {1: [0,1], -1:[2,3]}
    caches = [[[], 100], [[], 50], [[], 10], [[], 5]]
    for sum_cache, chunk in caches:  
        for i in range(0,size, chunk):
            sum_cache.append(sum(inp[i:i+chunk]))

    output = []
    prev_sums = 0
    ind = 0

    for j in range(0, size):

        if j > size / 2 + 1:
            out -= inp[j-1]
            output.append(str(out)[-1])  
            continue
        elif j > 3 and (j > size / 5 +1):            
            oldp = pattern_list[j-1][0]
            newp = pattern_list[j][0]
            out -= sum(inp[oldp[1][0]:newp[1][0]])
            out += sum(inp[oldp[1][1]:newp[1][1]]) 
            out += sum(inp[oldp[-1][0]:newp[-1][0]])
            out -= sum(inp[oldp[-1][1]:newp[-1][1]])  
            if  oldp[-1][0] > newp[-1][0]:
                out += sum(inp[oldp[-1][0]:])
            output.append(str(out)[-1])  
            continue
 
        out = 0
        # print('Number ', j)
        for p in pattern_list[j]:
            out += suma(*p[1]) 
            out -= suma(*p[-1])
        output.append(str(out)[-1])  
              
    print('RES: ', ''.join(output))
    inp = [int(c) for c in output]

start_point = int(''.join([str(c) for c in input_data[0:7]]))
print(inp[start_point:start_point+8])

# start = int(inp[:7])
# stop = start + 8
# print(inp[start-1:stop+1])

