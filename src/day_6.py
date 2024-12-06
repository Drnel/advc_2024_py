
def main():
    print("\n-----Solving advent of code 2024 day 6-----\n")
    file = open("input_texts/day_6.txt", "r")
    text = file.read()
    file.close()
    lines = text.split("\n")
    for i in range(len(lines)):
        lines[i] = list(lines[i])
    y = 0
    x = 0
    length = len(lines)
    for i in range(len(lines)):
        if "^" in lines[i]:
            y = i
            x = lines[i].index("^")
    
    direction = "up"
    while(True):
        lines[y][x] = "X"
        if direction == "up":
            y = y - 1
        if direction == "down":
            y = y + 1
        if direction == "right":
            x = x + 1
        if direction == "left":
            x = x - 1
        
        if (x < 0) or  (x == length) or (y < 0) or (y == length):
            break
        
        if lines[y][x] != "#":
            continue

        if direction == "up":
            y = y + 1
            direction = "right"
            continue
        if direction == "down":
            y = y - 1
            direction = "left"
            continue
        if direction == "right":
            x = x - 1
            direction = "down"
            continue
        if direction == "left":
            x = x + 1
            direction = "up"

    distinct_guard_positions = 0
    for line in lines:
        for ch in line:
            if ch == "X":
                distinct_guard_positions += 1


    print(f"part 1 distinct guard positions: | {distinct_guard_positions} | \n")

    lines = text.split("\n")
    for i in range(len(lines)):
        lines[i] = list(lines[i])
    y = 0
    x = 0
    length = len(lines)
    for i in range(len(lines)):
        if "^" in lines[i]:
            y = i
            x = lines[i].index("^")
    
    num_loops_count = 0
    temp_loop_count = 0

    for oy in range(length):
        for ox in range(length):
            temp_loop_count += 1
            if temp_loop_count % 100 == 0:
                print(temp_loop_count,"/",(length * length),"  done ----", num_loops_count)
            if not ((lines[oy][ox] == "#") or ((ox == x) and (oy == y))):
                loop_state = check_loop(lines, x, y, ox, oy)
                if loop_state == "looping":
                    num_loops_count += 1
                

    print(f"part 2 possible loop positions: | {num_loops_count} | \n")

    
    
def check_loop(lines, x, y, ox, oy):
    lines[oy][ox] = "#"
    direction = "up"
    length = len(lines)
    dictionary = {}
    dictionary["up"] = []
    dictionary["down"] = []
    dictionary["left"] = []
    dictionary["right"] = []

    while(True):
        if (x, y) in dictionary[direction]:
            lines[oy][ox] = "."
            return "looping"
        dictionary[direction].append((x, y))
        if direction == "up":
            y = y - 1
        if direction == "down":
            y = y + 1
        if direction == "right":
            x = x + 1
        if direction == "left":
            x = x - 1
        
        if (x < 0) or  (x == length) or (y < 0) or (y == length):
            lines[oy][ox] = "."
            return "not looping"
        
        if lines[y][x] != "#":
            continue

        if direction == "up":
            y = y + 1
            direction = "right"
            continue
        if direction == "down":
            y = y - 1
            direction = "left"
            continue
        if direction == "right":
            x = x - 1
            direction = "down"
            continue
        if direction == "left":
            x = x + 1
            direction = "up"
    
    

        

main()