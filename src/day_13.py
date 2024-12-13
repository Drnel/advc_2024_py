def main():
    print("\n-----Solving advent of code 2024 day 13-----\n")
    file = open("input_texts/day_13.txt", "r")
    text = file.read()
    file.close()
    machines_t = [machine.split("\n") for machine in text.split("\n\n")]
    machines = []
    for machine in machines_t:
        mtmp = []
        for line in machine:
            parts1 = line.split(": ")
            parts2 = parts1[1].split(", ")
            x = int(parts2[0][2:])
            y = int(parts2[1][2:])
            mtmp.append([x, y])
        machines.append(mtmp)
    total_min_cost = 0
    for machine in machines:
        min_cost = 1000
        for a in range(101):
            for b in range(101):
                if (
                    ((machine[0][0] * a) + (machine[1][0] * b)) == machine[2][0] and
                    ((machine[0][1] * a) + (machine[1][1] * b)) == machine[2][1]
                ):
                    if ((a * 3) + b ) < min_cost:
                        min_cost = ((a * 3) + b)
        if min_cost < 1000:
            total_min_cost += min_cost
    
    print(f"part 1 total minimum token cost: | {total_min_cost} | \n")

    machines = []
    for machine in machines_t:
        mtmp = []
        num = 0
        for line in machine:
            num = num + 1
            parts1 = line.split(": ")
            parts2 = parts1[1].split(", ")
            x = int(parts2[0][2:])
            y = int(parts2[1][2:])
            if num == 3:
                x += 10000000000000
                y += 10000000000000
            mtmp.append([x, y])
        machines.append(mtmp)
    total_min_cost = 0
    for machine in machines:
        a1 = machine[0][0]
        b1 = machine[1][0]
        c1 = machine[2][0]
        a2 = machine[0][1]
        b2 = machine[1][1]
        c2 = machine[2][1]

        if (
            ((b1 * c2) - (b2 * c1)) % ((b2 * a1) - (b1 * a2)) == 0 and
            ((c1 * a2) - (c2 * a1)) % ((b2 * a1) - (b1 * a2)) == 0
        ):
            a = ((b1 * c2) - (b2 * c1)) // ((b2 * a1) - (b1 * a2))
            b = ((c1 * a2) - (c2 * a1)) // ((b2 * a1) - (b1 * a2))
            total_min_cost += ((3 * abs(a)) + abs(b))

        

    print(f"part 2 total minimum token cost: | {total_min_cost} | \n")


main()
