import numpy as np
from numpy import linalg, dot, arccos, around, pi
        
input_data = '''###..#.##.####.##..###.#.#..
#..#..###..#.......####.....
#.###.#.##..###.##..#.###.#.
..#.##..##...#.#.###.##.####
.#.##..####...####.###.##...
##...###.#.##.##..###..#..#.
.##..###...#....###.....##.#
#..##...#..#.##..####.....#.
.#..#.######.#..#..####....#
#.##.##......#..#..####.##..
##...#....#.#.##.#..#...##.#
##.####.###...#.##........##
......##.....#.###.##.#.#..#
.###..#####.#..#...#...#.###
..##.###..##.#.##.#.##......
......##.#.#....#..##.#.####
...##..#.#.#.....##.###...##
.#.#..#.#....##..##.#..#.#..
...#..###..##.####.#...#..##
#.#......#.#..##..#...#.#..#
..#.##.#......#.##...#..#.##
#.##..#....#...#.##..#..#..#
#..#.#.#.##..#..#.#.#...##..
.#...#.........#..#....#.#.#
..####.#..#..##.####.#.##.##
.#.######......##..#.#.##.#.
.#....####....###.#.#.#.####
....####...##.#.#...#..#.##.'''

seen = [[0 for ch in line] for line in input_data.split('\n')]
input_data = [[ch for ch in line] for line in input_data.split('\n')]

unit_vector = [1,0]

# station = [0,0]
# for i in range(len(input_data)):
#     for j in range(len(input_data[i])):
#         if input_data[i][j] == 'X':
#             station = [i,j]
#             break
#     else:
#         continue
#     break
station = [19,22]
print(station)

asteroids = []
for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        if input_data[i][j] == '.':
            continue
        elif i == station[0] and j == station[1]:
            continue
        v = np.array([(station[0] - i),(j - station[1])])
        mod =  linalg.norm(v)
        v = v / mod
        dot_product = dot(unit_vector, v)
        a = arccos(dot_product)*180/pi
        a = around(a,8)

        if v[1] < 0:
            a = 360 - a

        asteroids.append([a, mod, i, j])

asteroids = sorted(asteroids, key=lambda a: (a[0],a[1]))
count = 1
while len(asteroids) > 0:
    print('Next round!')
    last_angle = -1
    for a in asteroids[:]:
        if a[0] != last_angle:
            print('Asteroid ', count, ' in ', a[3], a[2], ' destroyed.')
            asteroids.remove(a)
            count += 1
        last_angle = a[0]
