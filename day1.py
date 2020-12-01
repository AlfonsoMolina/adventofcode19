fuel = []
def compute_fuel(mass):
    fuel = int(mass/3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + compute_fuel(fuel)

with open('adventofcode/day1_input.txt', 'r') as f:
    for line in f:
        fuel.append(compute_fuel(int(line.strip())))

print(sum(fuel))