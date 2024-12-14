def main():
    print("\n-----Solving advent of code 2024 day 14-----\n")
    file = open("input_texts/day_14.txt", "r")
    text = file.read()
    file.close()
    lines = text.split("\n")
    robots = []
    width = 101
    height = 103
    middle_row = height // 2
    middle_column = width // 2
    for line in lines:
        parts = line.split(" ")
        position = parts[0][2:].split(",")
        x = int(position[0])
        y = int(position[1])
        velocity = parts[1][2:].split(",")
        xv = int(velocity[0])
        yv = int(velocity[1])
        robots.append([x, y, xv, yv])
    for robot in robots:
        robot[0] = (robot[0] + (robot[2] * 100)) % width
        robot[1] = (robot[1] + (robot[3] * 100)) % height
    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0
    for robot in robots:
        x = robot[0]
        y = robot[1]
        if (x < middle_column) and (y < middle_row):
            top_left += 1
        if (x > middle_column) and (y < middle_row):
            top_right += 1
        if (x < middle_column) and (y > middle_row):
            bottom_left += 1
        if (x > middle_column) and (y > middle_row):
            bottom_right += 1
    safety_factor = top_left * top_right * bottom_left * bottom_right

    print(f"part 1 safety factor: | {safety_factor} | \n")

    robots = []
    width = 101
    height = 103
    middle_row = height // 2
    middle_column = width // 2
    for line in lines:
        parts = line.split(" ")
        position = parts[0][2:].split(",")
        x = int(position[0])
        y = int(position[1])
        velocity = parts[1][2:].split(",")
        xv = int(velocity[0])
        yv = int(velocity[1])
        robots.append([x, y, xv, yv])    
    for i in range(1, 10000):
        for robot in robots:
            robot[0] = (robot[0] + (robot[2])) % width
            robot[1] = (robot[1] + (robot[3])) % height
        clumped_robots = robot_clump_test(robots)
        if clumped_robots > 10:
            print(clumped_robots, i)
            break
        
    print(f"part 2 minimum seconds to easter egg: | {i} | \n")
    print_robots(robots, width, height)

def print_robots(robots, width, height):
    render = []
    for _ in range(height):
        render.append(["."] * width)
    for robot in robots:
        x = robot[0]
        y = robot[1]
        render[y][x] = "0"
    for line in render:
        print("".join(line))

def robot_clump_test(robots):
    clumped_robots = 0
    for robot1 in robots:
        left = False
        right = False
        up = False
        down = False
        for robot2 in robots:
            x1, y1, x2, y2 = robot1[0], robot1[1], robot2[0], robot2[1]
            if (x2 == (x1 - 1)) and  (y1 == y2):
                left = True
            if (x2 == (x1 + 1)) and  (y1 == y2):
                right = True
            if (x2 == x1) and  ((y1 - 1) == y2):
                up = True
            if (x2 == x1) and  ((y1 + 1) == y2):
                down = True
        if left and right and up and down:
            clumped_robots += 1
    return clumped_robots
    
            

main()