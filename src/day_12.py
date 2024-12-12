def main():
    print("\n-----Solving advent of code 2024 day 12-----\n")
    file = open("input_texts/day_12.txt", "r")
    text = file.read()
    file.close()
    lines = text.split("\n")
    mapp = [list(line) for line in lines]
    visited = []
    for _ in range(len(mapp)):
        visited.append([False] * len(mapp[0]))
    total_cost = 0
    total_cost_fused = 0
    for y in range(len(mapp)):
        for x in range(len(mapp[0])):
            if not visited[y][x]:
                corners = [0]
                res = rec_area(y, x, mapp, visited, mapp[y][x], corners)
                total_cost += ((res[0]) * (res[1]))
                total_cost_fused += ((res[0]) * (corners[0]))

    print(f"part 1 total cost: | {total_cost} | \n")

    print(f"part 2 total cost: | {total_cost_fused} | \n")

def rec_area(y, x, mapp, visited, ch, corners):
    if ch != mapp[y][x]:
        return (0, 1)
    if visited[y][x] == True:
        return (0, 0)
    visited[y][x] = True
    determ_dir(y, x, mapp, corners)
    area = 1
    perimeter = 0
    # up
    if y > 0:
        val = rec_area((y - 1), x, mapp, visited, ch, corners)
        area += val[0]
        perimeter += val[1]
    else:
        perimeter += 1
    # down
    if y < (len(mapp) - 1):
        val = rec_area((y + 1), x, mapp, visited, ch, corners)
        area += val[0]
        perimeter += val[1]
    else:
        perimeter += 1
    # left
    if x > 0:
        val = rec_area(y, (x - 1), mapp, visited, ch, corners)
        area += val[0]
        perimeter += val[1]
    else:
        perimeter += 1
    # right
    if x < (len(mapp[0]) - 1):
        val = rec_area(y, (x + 1), mapp, visited, ch, corners)
        area += val[0]
        perimeter += val[1]
    else:
        perimeter += 1
    return (area, perimeter)


def determ_dir(y, x, mapp, corners):
    up, down, left, right = False, False, False, False
    # up
    if y > 0:
        if mapp[y - 1][x] != mapp[y][x]:
            up = True
    else:
        up = True
    # down
    if y < (len(mapp) - 1):
        if mapp[y + 1][x] != mapp[y][x]:
            down = True
    else:
        down = True
    # left
    if x > 0:
        if mapp[y][x - 1] != mapp[y][x]:
            left = True
    else:
        left = True
    # right
    if x < (len(mapp[0]) - 1):
        if mapp[y][x + 1] != mapp[y][x]:
            right = True
    else:
        right = True
    if left and up:
        corners[0] += 1
    if right and up:
        corners[0] += 1
    if left and down:
        corners[0] += 1
    if right and down:
        corners[0] += 1
    if (not up) and (not right):
        if mapp[y - 1][x + 1] != mapp[y][x]:
            corners[0] += 1
    if (not up) and (not left):
        if mapp[y - 1][x - 1] != mapp[y][x]:
            corners[0] += 1
    if (not down) and (not right):
        if mapp[y + 1][x + 1] != mapp[y][x]:
            corners[0] += 1
    if (not down) and (not left):
        if mapp[y + 1][x - 1] != mapp[y][x]:
            corners[0] += 1

main()

