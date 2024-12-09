def main():
    print("\n-----Solving advent of code 2024 day 8-----\n")
    file = open("input_texts/day_8.txt", "r")
    text = file.read()
    file.close()
    lines = text.split("\n")

    width = len(lines[0])
    height = len(lines)
    unique_antinodes = set()
    for y1 in range(height):
        for x1 in range(width):
            node1 = lines[y1][x1]
            if node1 == ".":
                continue
            for y2 in range(y1, height):
                for x2 in range(width):
                    if (y2 == y1) and (x2 <= x1):
                        continue
                    node2 = lines[y2][x2]
                    if node1 == node2:
                        top_antinode_y = y1 - (y2 - y1)
                        top_antinode_x = x1 + (x1 - x2)
                        if not (
                            top_antinode_y < 0 or
                            top_antinode_y >= height or
                            top_antinode_x < 0 or
                            top_antinode_x >= width
                        ):
                            unique_antinodes.add((top_antinode_y, top_antinode_x))
                        bottom_antinode_y = y2 + (y2 - y1)
                        bottom_antinode_x = x2 + (x2 - x1)
                        if not (
                            bottom_antinode_y < 0 or
                            bottom_antinode_y >= height or
                            bottom_antinode_x < 0 or
                            bottom_antinode_x >= width
                        ):
                            unique_antinodes.add((bottom_antinode_y, bottom_antinode_x))

    print(f"part 1 unique antinode locations: | {len(unique_antinodes)} | \n")

    unique_antinodes = set()
    for y1 in range(height):
        for x1 in range(width):
            node1 = lines[y1][x1]
            if node1 == ".":
                continue
            for y2 in range(y1, height):
                for x2 in range(width):
                    if (y2 == y1) and (x2 <= x1):
                        continue
                    node2 = lines[y2][x2]
                    if node1 == node2:
                        top_antinode_y = y1
                        top_antinode_x = x1
                        while(True):
                            if (
                                top_antinode_y < 0 or
                                top_antinode_y >= height or
                                top_antinode_x < 0 or
                                top_antinode_x >= width
                            ):
                                break
                            unique_antinodes.add((top_antinode_y, top_antinode_x))
                            top_antinode_y = top_antinode_y - (y2 - y1)
                            top_antinode_x = top_antinode_x + (x1 - x2)
                        bottom_antinode_y = y2
                        bottom_antinode_x = x2
                        while(True):
                            if (
                                bottom_antinode_y < 0 or
                                bottom_antinode_y >= height or
                                bottom_antinode_x < 0 or
                                bottom_antinode_x >= width
                            ):
                                break
                            unique_antinodes.add((bottom_antinode_y, bottom_antinode_x))
                            bottom_antinode_y = bottom_antinode_y + (y2 - y1)
                            bottom_antinode_x = bottom_antinode_x + (x2 - x1)

    print(f"part 2 fixed unique antinode locations: | {len(unique_antinodes)} | \n")



main()