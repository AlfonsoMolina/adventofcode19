from math import ceil

data = """2 KBRD => 3 NSPQ
1 TMTNM, 5 WMZD => 4 JVBK
3 TMTNM => 8 JTPF
3 NDXL => 2 BDQP
2 VTGNT => 2 TNWR
1 ZQRBC => 2 WGDN
2 MJMC => 3 QZCZ
10 MDXVB, 3 DHTB => 1 SRLP
1 KBRD, 1 PNPW => 6 SQCB
1 KDTRS, 4 VTGNT => 7 NDXL
1 FZSJ => 1 CJPSR
6 TKMKD => 8 FTND
2 ZNBSN => 4 DNPT
16 SKWKQ, 2 FZSJ, 3 GSQL, 1 PNRC, 4 QNKZW, 4 RHZR, 10 MTJF, 1 XHPK => 3 RJQW
1 NHQW => 8 QNKZW
16 JZFCN, 9 KWQSC, 1 JGTR => 7 TMTNM
2 PNRC => 7 LCZD
1 NLSNC, 14 SXKC, 2 DHTB => 1 ZQRBC
1 MXGQ, 2 KWQPL => 3 FZSJ
6 DWKLT, 1 VHNXW, 3 NSPQ => 1 BQXNW
23 KDTRS => 1 XHPK
1 PFBF, 3 KBLHZ => 3 MBGWZ
5 NSPQ => 3 TPJP
27 SRLP, 12 KWQSC, 14 ZNBSN, 33 HQTPN, 3 HWFQ, 23 QZCZ, 6 ZPDN, 32 RJQW, 3 GDXG => 1 FUEL
2 NSPQ, 5 ZNBSN, 1 TPJP => 8 PFBF
1 MSCRZ => 3 ZNBSN
1 TNWR, 2 ZNBSN => 5 MDXVB
10 SQCB => 5 MXGQ
3 JVBK, 1 MTJF, 1 KBLHZ => 2 HQTPN
2 MJMC => 2 KMLKR
2 BQXNW, 1 CJPSR, 25 KWQPL => 4 PNRC
1 VHNXW, 3 KWZKV => 4 TKMKD
10 VTGNT, 4 JTPF => 9 KWZKV
168 ORE => 3 JZFCN
173 ORE => 5 KBRD
2 TNWR, 1 MBGWZ, 3 NSPQ => 8 SKWKQ
1 KWZKV, 2 MJMC, 14 SKWKQ => 9 NSTR
4 JZFCN, 13 PNPW => 2 WMZD
6 JQNGL => 6 MGFZ
1 SQCB, 4 NLSNC => 5 DHTB
5 MGFZ, 39 WGDN, 1 MBGWZ, 2 NSTR, 1 XKBND, 1 SXKC, 1 JVBK => 5 ZPDN
7 NSPQ, 6 PNPW => 7 NLSNC
3 TNWR => 9 KWQPL
9 NLSNC, 4 NDXL, 1 MDXVB => 4 MTJF
2 VTJC => 7 PNPW
2 JZFCN => 8 MSCRZ
134 ORE => 3 JGTR
3 HQTPN => 4 GSQL
154 ORE => 9 VTJC
1 KWQSC, 14 KBRD => 4 JQCZ
7 PNRC, 1 XKBND => 8 RHZR
1 JQCZ => 4 VTGNT
6 BDQP => 6 JQNGL
7 FTND => 3 XKBND
2 XHPK, 4 NHQW => 1 MJMC
1 JQCZ => 5 KDTRS
1 DNPT => 4 KBLHZ
1 KMLKR, 26 ZNBSN, 1 LCZD, 11 QNKZW, 2 SQCB, 3 FTND, 24 PNRC => 4 HWFQ
179 ORE => 6 KWQSC
2 TKMKD, 3 FZSJ => 2 SXKC
2 JTPF => 7 VHNXW
1 FTND => 7 DWKLT
13 TNWR, 2 QNKZW, 6 SQCB => 5 GDXG
5 JTPF, 4 ZNBSN, 8 WMZD => 8 NHQW"""

d = {}
for line in data.split('\n'):
    inp, out = line.split('=>')
    cant, prod = out.split()

    d[prod] = [int(cant)]

    for i in inp.split(','):
        d[prod].append([int(i.split()[0]), i.split()[1]])

fuel = 1
ore = 1
max_ore = 1000000000000
while True:

    cost = [[fuel, 'FUEL']]
    extra = {}
    ore = 0
    count = 0
    while True:
        # print('We need ' + str(cost))
        # print(extra)
        for c in cost[:]:
            cant, el = c
            log = str(c) + ' => '
            if el in extra and extra[el] > 0:
                if extra[el] >= cant:
                    extra[el] -= cant
                    cant = 0
                else:
                    cant -= extra[el]
                    extra[el] = 0
            if el != 'ORE':
                cant_fab = ceil(cant / d[el][0]) 
                if cant_fab * d[el][0] > cant:
                    if el in extra:
                        extra[el] += cant_fab * d[el][0] - cant
                    else:
                        extra[el] = cant_fab * d[el][0] - cant
                
                cost.remove(c)
                for e in d[el][1:]:
                    log += str([cant_fab * e[0] , e[1]]) + ', '
                    cost.append([cant_fab * e[0] , e[1]])
            log += ' | EXTRA ' + el + ' ' + str(extra[el]) if el in extra else ''
            # print(log)
        if all(i[1] == 'ORE' for i in cost):
            for i in cost:
                ore += i[0]
            break

    print(ore, ' => ', fuel)
    if fuel == max_ore * fuel // ore:
        break
    fuel = max_ore * fuel // ore
    # break