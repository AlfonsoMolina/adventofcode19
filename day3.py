wire_one = [[0,0]] # x, y
wire_two = [[0,0]]

# path_one = 'R8,U5,L5,D3'
# path_two = 'U7,R6,D4,L4'
# path_one = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
# path_two = 'U62,R66,U55,R34,D71,R55,D58,R83'
# path_one = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
# path_two = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
path_one = 'R1006,D541,R261,U378,L530,U165,L175,U143,R162,D504,R985,U33,R544,D168,L498,D549,R88,D243,L36,U944,R261,D91,L957,D579,L224,D732,R312,U378,R82,D200,L510,U747,R588,U667,L495,D147,L100,U482,R896,D711,L513,U44,L685,U547,L132,D23,R139,U786,L908,U912,R531,U564,L970,D562,R422,U919,R108,D275,R431,U697,L85,D762,L25,D633,R878,U566,L550,D288,L29,D788,R930,U619,L612,U228,R25,D133,R219,U367,L889,U735,L994,U513,R34,D429,L750,U83,R204,U68,R769,D833,L545,D621,L747,U714,R655,U112,L629,D353,L450,D588,R775,U493,L252,D486,L405,D350,R970,D73,L750,D731,L962,D242,R947,D348,L252,D392,L94,U970,R616,U505,L782,D375,R849,U971,R57,D25,R68,U174,L670,U735,R66,D994,R868,U285,L866,U433,L169,D575,L374,U169,R180,D251,R671,D703,R708,D60,L251,D164,L106,U974,R670,U760,L235,U377,R318,U294,L421,D904,L571,U157,R428,D416,L237,D850,L827,U702,L134,D67,R327,U976,L307,D454,L646,U919,L92,D523,R828,D544,L557,D142,L671,D862,R118,U244,L667,U356,L554,U969,R348,D895,L735,D948,R920,U470,R819,D256,R169,D410,R977,U487,L64,U466,L574,U891,R29,D767,L224,D922,L782,U433,L478,U582,L603,U339,L658,U188,L95,U766,R958,U313,L881,D869,L633,U551,R270,U444,R399,D698,L923,U213,R245,D486,R34,U514,R450,U739,R102,U181,L826,D839,L948,D11,R51,U146,R415,U683,R352,U387,R158,D88,L576,U600,R955,D22,R884,D772,L576,D74,L937,U832,R198,D721,R393,U847,R828,U975,L452,U796,R950,U568,R117,U114,L983,U514,R564,U569,L141,D464,R463,U635,L772,U634,R614,D160,R388,D550,L933,D832,R94,D855,L18,U241,L805,U517,R384,D464,L271,U788,R718,U495,R103'
path_two = 'L1000,D65,L329,D227,R798,U36,R263,D232,R771,D768,R223,D898,L637,U402,L867,U694,R362,U199,L769,U956,L180,U123,L495,U660,L861,D652,R222,D166,R47,D766,R709,U859,L639,U841,L407,D392,R503,D596,R614,D448,L340,D562,L913,U942,L426,D84,R385,U202,R676,U379,L231,D124,L568,D134,L271,D777,R765,U979,R678,D478,R307,D568,L318,D705,R787,U322,R233,D423,L617,U955,R32,U989,R356,U922,R444,U443,R136,U140,L298,U348,L121,U332,R285,D302,L844,D234,L468,U395,R20,D245,L583,U173,L928,U598,L383,D188,L945,D382,L929,D181,L650,U394,L938,U805,L680,U676,R136,U925,L899,U990,R661,D621,R612,D587,R609,U560,R650,D416,L285,D152,R906,U47,L721,D206,L602,U258,R667,U443,L291,D375,L977,D148,R394,U758,L43,D953,R143,D60,R851,D887,R718,D505,R407,D321,R140,D675,L42,U235,L626,D673,L271,D398,L190,U30,L225,D612,R896,U757,L340,D280,L742,U188,L372,D7,R677,U248,R694,U581,L220,U372,R497,U89,R952,D221,L71,D962,L992,U420,R741,U96,R625,U794,L602,U229,R635,D585,R119,U501,R640,D283,L963,U385,L967,D503,L453,D578,L465,D318,L968,U979,L650,D894,L210,U855,R298,D66,R378,D223,L475,D950,L417,D276,L494,D690,R516,D352,L603,U211,R171,U553,L437,U865,L378,D223,R814,D779,L780,D738,R920,D462,L230,U574,L880,D252,R710,D476,L184,U635,R453,U115,R96,U169,R995,D523,R562,D480,L791,U865,R568,D149,L539,U610,R107,D604,R95,D982,R360,U141,L567,D555,R481,U716,R753,D576,R54,D343,R663,U676,R907,D202,R230,U827,L583,U937,R818,D579,R502,D713,R61,U402,L527,D955,R117,U214,R580,U636,R721,U55,L899,U667,R595,U790,L384,U416,L375,D1,L653,U611,L187,D256,L931'

for wire, path in [[wire_one, path_one], [wire_two, path_two]]:
    for step in path.split(','):
        direction = step[0]
        distance = int(step[1:])

        if direction == 'U' or direction == 'D':
            new_y = wire[-1][1] + (distance if direction == 'U' else -distance)
            wire.append([wire[-1][0], new_y])
        elif direction == 'R' or direction == 'L':
            new_x = wire[-1][0] + (distance if direction == 'R' else -distance)
            wire.append([new_x, wire[-1][1]])

cross = []
wire_one_x_steps = []
wire_one_y_steps = []
total = 0
for i in range(0,len(wire_one)-1):
    s = wire_one[i]
    ss = wire_one[i+1]
    if s[0] == ss[0]:
        wire_one_y_steps.append([ss[0], [s[1], ss[1]], total])
        total += abs(ss[1] - s[1])
    if s[1] == ss[1]:
        wire_one_x_steps.append([ss[1], [s[0], ss[0]], total])
        total += abs(ss[0] - s[0])
    

wire_two_x_steps = []
wire_two_y_steps = []
total = 0
for i in range(0,len(wire_two)-1):
    s = wire_two[i]
    ss = wire_two[i+1]
    if s[0] == ss[0]:
        wire_two_y_steps.append([ss[0], [s[1], ss[1]], total])
        total += abs(ss[1] - s[1])
    if s[1] == ss[1]:
        wire_two_x_steps.append([ss[1], [s[0], ss[0]], total])
        total += abs(ss[0] - s[0])

cross = []
for s in wire_one_x_steps:
    for ss in wire_two_y_steps:
        if ss[1][0] < s[0] < ss[1][1] or ss[1][0] > s[0] > ss[1][1]:
            if s[1][0] < ss[0] < s[1][1] or s[1][0] > ss[0] > s[1][1]:
                total_one = s[2] + abs(ss[0] - s[1][0])
                total_two = ss[2] + abs(s[0] - ss[1][0])
                cross.append([ss[0], s[0], total_one, total_two])
for s in wire_two_x_steps:
    for ss in wire_one_y_steps:
        if ss[1][0] < s[0] < ss[1][1] or ss[1][0] > s[0] > ss[1][1]:
            if s[1][0] < ss[0] < s[1][1] or s[1][0] > ss[0] > s[1][1]:
                total_one = ss[2] + abs(s[0] - ss[1][0])
                total_two = s[2] + abs(ss[0] - s[1][0])
                cross.append([ss[0], s[0], total_one, total_two])
manh_dist = [abs(x[2]) + abs(x[3]) for x in cross ]
res = min(manh_dist)
print(res)

# for i in range(1,len(wire_one)-1):
#     s = wire_one[i]
#     ss = wire_one[i+1]
#     if s[0] == ss[0]:
#         y = range(s[1], ss[1], 1 if s[1] < ss[1] else -1)
#         x = [s[0]] * ((s[1] - ss[1] ) * (1 if s[1] > ss[1] else -1))
#     if s[1] == ss[1]:
#         x = range(s[0], ss[0], 1 if s[0] < ss[0] else -1)
#         y = [s[1]] * ((s[0] - ss[0] ) * (1 if s[0] > ss[0] else -1))
#     for j in zip(x,y):
#         for ii in range(1,len(wire_two)-1):
#             s = wire_two[ii]
#             ss = wire_two[ii+1]
#             if s[0] == ss[0]:
#                 yy = range(s[1], ss[1], 1 if s[1] < ss[1] else -1)
#                 xx = [s[0]] * ((s[1] - ss[1] ) * (1 if s[1] > ss[1] else -1))
#             if s[1] == ss[1]:
#                 xx = range(s[0], ss[0], 1 if s[0] < ss[0] else -1)
#                 yy = [s[1]] * ((s[0] - ss[0] ) * (1 if s[0] > ss[0] else -1))
#             for jj in zip(xx,yy):
#                 if j == jj:
#                     cross.append(j)

