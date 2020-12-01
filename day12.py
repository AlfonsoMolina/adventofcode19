import re

data_input = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

exp = r'=(P?[0-9-]*)[,>]'
moons = []
for line in data_input.split('\n'):    
    x, y, z = re.findall(exp, line)
    moon = [[int(x),int(y),int(z)],[0,0,0]]
    moons += [moon]
for i in range(10):
    for moon in moons:
        for second_moon in moons:
            if moon == second_moon:
                continue
            for axis in [0,1,2]:
                if moon[0][axis] > second_moon[0][axis]:
                    moon[1][axis] -= 1
                    second_moon[1][axis] += 1
    for moon in moons:
        for axis in [0,1,2]:
            moon[0][axis] += moon[1][axis] 
# abs
for moon in moons:
    for axis in [0,1,2]:
        moon[0][axis] = abs(moon[0][axis])
        moon[1][axis] = abs(moon[1][axis])
energy = sum(sum(m[0]) * sum(m[1]) for m in moons)
print(moons)
print(energy)
