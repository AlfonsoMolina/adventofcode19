import numpy as np

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
for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        if input_data[i][j] == '.':
            continue
        angles = []
        for ii in range(len(input_data)):
            for jj in range(len(input_data[ii])):
                if input_data[ii][jj] == '.':
                    continue
                elif i == ii and j == jj:
                    continue
                v = np.array([(i - ii),(jj - j)])
                mod =  np.linalg.norm(v)
                v = v / mod
                dot_product = np.dot(unit_vector, v)
                a = np.arccos(dot_product)*180/np.pi
                a = np.around(a,8)

                if v[1] < 0:
                    a = 360 - a

                if a in angles:
                    continue

                seen[i][j] += 1
                angles.append(a)

list_seen = [s for ss in seen for s in ss]
max_seen = max(list_seen)

print(max_seen)
for i in range(len(seen)):
    for j in range(len(seen[i])):
        if seen[i][j] == max_seen:
            print(j,i)