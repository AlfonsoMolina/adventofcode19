def check_n(n):
    n = str(n)
    if len(n) != 6:
        return False
    if n != ''.join(sorted(n)):
        return False
    if not any(n.count(ch) == 2 for ch in n):
        return False
    return True
res = check_n(123789)
print(res)
count = 0
for n in range(134792, 675810):
    if check_n(n):
        count += 1

print(count)

