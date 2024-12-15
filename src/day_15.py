def main():
    print("\n-----Solving advent of code 2024 day 15-----\n")
    file = open("input_texts/day_15.txt", "r")
    text = file.read()
    file.close()
    mapp, movements = text.split("\n\n")
    movements = "".join(movements.split("\n"))
    mapp_rows = mapp.split("\n")
    mapp = []
    for row in mapp_rows:
        mapp.append(list(row))
    draw_map(mapp)
    robot_y = 0
    robot_x = 0
    for y in range(len(mapp)):
        for x in range(len(mapp[0])):
            if mapp[y][x] == "@":
                robot_y = y
                robot_x = x

    for direction in movements:
        if direction == "^":
            if move_object(robot_y, robot_x, mapp, direction):
                robot_y -= 1
        if direction == "v":
            if move_object(robot_y, robot_x, mapp, direction):
                robot_y += 1
        if direction == "<":
            if move_object(robot_y, robot_x, mapp, direction):
                robot_x -= 1
        if direction == ">":
            if move_object(robot_y, robot_x, mapp, direction):
                robot_x += 1
    draw_map(mapp)
    sum_gps_box = 0
    for y in range(len(mapp)):
        for x in range(len(mapp[0])):
            if mapp[y][x] == "O":
                sum_gps_box += ((y * 100) + x)
    
    print(f"part 1 box gps sum: | {sum_gps_box} | \n")

    mapp = []
    for row in mapp_rows:
        wide_row = []
        for ch in row:
            if ch == "#":
                wide_row.append("#")
                wide_row.append("#")
            if ch == ".":
                wide_row.append(".")
                wide_row.append(".")
            if ch == "@":
                wide_row.append("@")
                wide_row.append(".")
            if ch == "O":
                wide_row.append("[")
                wide_row.append("]")
        mapp.append(wide_row)
    draw_map(mapp)
    robot_y = 0
    robot_x = 0
    for y in range(len(mapp)):
        for x in range(len(mapp[0])):
            if mapp[y][x] == "@":
                robot_y = y
                robot_x = x
    print(robot_y, robot_x)
    for direction in movements:
        if direction == "^":
            if wide_move_object(robot_y, robot_x, mapp, direction):
                robot_y -= 1
        if direction == "v":
            if wide_move_object(robot_y, robot_x, mapp, direction):
                robot_y += 1
        if direction == "<":
            if wide_move_object(robot_y, robot_x, mapp, direction):
                robot_x -= 1
        if direction == ">":
            if wide_move_object(robot_y, robot_x, mapp, direction):
                robot_x += 1
    draw_map(mapp)
    sum_gps_box = 0
    for y in range(len(mapp)):
        for x in range(len(mapp[0])):
            if mapp[y][x] == "[":
                sum_gps_box += ((y * 100) + x)
    
    print(f"part 2 box gps sum: | {sum_gps_box} | \n")

def move_object(y, x, mapp, direction):
    if mapp[y][x] == "#":
        return False
    if mapp[y][x]== ".":
        return True
    if direction == "^":
        y2 = y - 1
        if move_object(y2, x, mapp, direction):
            mapp[y2][x] = mapp[y][x]
            mapp[y][x] = "."
            return True
        else:
            return False
    if direction == "v":
        y2 = y + 1
        if move_object(y2, x, mapp, direction):
            mapp[y2][x] = mapp[y][x]
            mapp[y][x] = "."
            return True
        else:
            return False
    if direction == "<":
        x2 = x - 1
        if move_object(y, x2, mapp, direction):
            mapp[y][x2] = mapp[y][x]
            mapp[y][x] = "."
            return True
        else:
            return False
    if direction == ">":
        x2 = x + 1
        if move_object(y, x2, mapp, direction):
            mapp[y][x2] = mapp[y][x]
            mapp[y][x] = "."
            return True
        else:
            return False

def wide_move_object(y, x, mapp, direction, magic_num=0):
    if mapp[y][x] == "#":
        return False
    if mapp[y][x]== ".":
        return True
    if direction == "^":
        if mapp[y][x] == "[":
            if magic_num == 0:
                if can_move(y, x+1, mapp, direction, 1):
                    if can_move(y, x, mapp, direction, 1):
                        wide_move_object(y, x+1, mapp,direction, 1)
                        wide_move_object(y, x, mapp, direction, 1)
                        return True
                else:
                    return False
        if mapp[y][x] == "]":
            if magic_num == 0:
                if can_move(y, x-1, mapp, direction, 1):
                    if can_move(y, x, mapp, direction, 1):
                        wide_move_object(y, x-1, mapp, direction, 1)
                        wide_move_object(y, x, mapp, direction, 1)
                        return True
                else:
                    return False
        y2 = y - 1
        if wide_move_object(y2, x, mapp, direction):
            mapp[y2][x] = mapp[y][x]
            mapp[y][x] = "."
            return True
        else:
            return False
    if direction == "v":
        if mapp[y][x] == "[":
            if magic_num == 0:
                if can_move(y, x+1, mapp, direction, 1):
                    if can_move(y, x, mapp, direction, 1):
                        wide_move_object(y, x+1, mapp,direction, 1)
                        wide_move_object(y, x, mapp, direction, 1)
                        return True
                else:
                    return False
        if mapp[y][x] == "]":
            if magic_num == 0:
                if can_move(y, x-1, mapp, direction, 1):
                    if can_move(y, x, mapp, direction, 1):
                        wide_move_object(y, x-1, mapp, direction, 1)
                        wide_move_object(y, x, mapp, direction, 1)
                        return True
                else:
                    return False
        y2 = y + 1
        if wide_move_object(y2, x, mapp, direction):
            mapp[y2][x] = mapp[y][x]
            mapp[y][x] = "."
            return True
        else:
            return False
    if direction == "<":
        x2 = x - 1
        if wide_move_object(y, x2, mapp, direction):
            mapp[y][x2] = mapp[y][x]
            mapp[y][x] = "."
            return True
        else:
            return False
    if direction == ">":
        x2 = x + 1
        if wide_move_object(y, x2, mapp, direction):
            mapp[y][x2] = mapp[y][x]
            mapp[y][x] = "."
            return True
        else:
            return False

def can_move(y, x, mapp, direction, magic_num=0):
    if mapp[y][x] == "#":
        return False
    if mapp[y][x]== ".":
        return True
    if direction == "^":
        if mapp[y][x] == "[":
            if magic_num == 0:
                if can_move(y, x+1, mapp, direction, 1):
                    if can_move(y, x, mapp, direction, 1):
                        return True
                else:
                    return False
        if mapp[y][x] == "]":
            if magic_num == 0:
                if can_move(y, x-1, mapp, direction, 1):
                    if can_move(y, x, mapp, direction, 1):
                        return True
                else:
                    return False
        y2 = y - 1
        if can_move(y2, x, mapp, direction):
            return True
        else:
            return False
    if direction == "v":
        if mapp[y][x] == "[":
            if magic_num == 0:
                if can_move(y, x+1, mapp, direction, 1):
                    if can_move(y, x, mapp, direction, 1):
                        return True
                else:
                    return False
        if mapp[y][x] == "]":
            if magic_num == 0:
                if can_move(y, x-1, mapp, direction, 1):
                    if can_move(y, x, mapp, direction, 1):
                        return True
                else:
                    return False
        y2 = y + 1
        if can_move(y2, x, mapp, direction):
            return True
        else:
            return False
    if direction == "<":
        x2 = x - 1
        if can_move(y, x2, mapp, direction):
            return True
        else:
            return False
    if direction == ">":
        x2 = x + 1
        if can_move(y, x2, mapp, direction):
            return True
        else:
            return False


def draw_map(mapp):
    for row in mapp:
        print("".join(row))            

main()