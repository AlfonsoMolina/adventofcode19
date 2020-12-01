import re

data_input = """<x=17, y=-12, z=13>
<x=2, y=1, z=1>
<x=-1, y=-17, z=7>
<x=12, y=-14, z=18>"""

exp = r'=(P?[0-9-]*)[,>]'
moons = []
for line in data_input.split('\n'):    
    x, y, z = re.findall(exp, line)
    moon = [[int(x),int(y),int(z)],[0,0,0]]
    moons += [moon]
new_state = ''
# first_state = ','.join([str(m) for moon in moons for moo in moon for m in moo])
m = []
for axis in [0,1,2]:
    counter = 0
    print('axis', axis)
    first_state = ','.join([str(moo[axis]) for moon in moons for moo in moon])
    states = [first_state]
    while new_state != first_state:
        for moon in moons:
            for second_moon in moons:
                if moon == second_moon:
                    continue
                if moon[0][axis] > second_moon[0][axis]:
                    moon[1][axis] -= 1
                    second_moon[1][axis] += 1
        for moon in moons:
            moon[0][axis] += moon[1][axis] 
        # new_state = ','.join([str(m) for moon in moons for moo in moon for m in moo])
        new_state = ','.join([str(moo[axis]) for moon in moons for moo in moon])
        if new_state in states:
            print('FOUND')
            print(new_state)
        states.append(new_state)
        counter += 1
    print(counter)
    m.append(counter)
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a
tmp = m[0] * m[1] /  gcd ( m[0] , m[1] )
lcm = tmp * m[2] /  gcd ( tmp , m[2] )
print(lcm)

