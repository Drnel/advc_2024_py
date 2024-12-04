def main():
    print("\n-----Solving advent of code 2024 day 4-----\n")
    file = open("input_texts/day_4.txt", "r")
    text = file.read()
    file.close()
    lines = text.split("\n")
    size = len(lines)
    lines = ([("." * (size + 6))] * 3) + lines + ([("." * (size + 6))] * 3)
    for i in range(3, (size + 3)):
        lines[i] = "..." + lines[i] + "..."
    xmas_count = 0
    for i in range(3, (size+3)):
        for j in range(3, (size + 3)):
            if (lines[i][j] + lines[i + 1][j] + lines[i + 2][j] + lines[i + 3][j]) == "XMAS":
                xmas_count += 1
            if (lines[i][j] + lines[i - 1][j] + lines[i - 2][j] + lines[i - 3][j]) == "XMAS":
                xmas_count += 1
            if (lines[i][j] + lines[i][j + 1] + lines[i][j + 2] + lines[i][j + 3]) == "XMAS":
                xmas_count += 1
            if (lines[i][j] + lines[i][j - 1] + lines[i][j - 2] + lines[i][j - 3]) == "XMAS":
                xmas_count += 1
            if (lines[i][j] + lines[i + 1][j + 1] + lines[i + 2][j + 2] + lines[i + 3][j + 3]) == "XMAS":
                xmas_count += 1
            if (lines[i][j] + lines[i - 1][j - 1] + lines[i - 2][j - 2] + lines[i - 3][j - 3]) == "XMAS":
                xmas_count += 1
            if (lines[i][j] + lines[i - 1][j + 1] + lines[i - 2][j + 2] + lines[i - 3][j + 3]) == "XMAS":
                xmas_count += 1
            if (lines[i][j] + lines[i + 1][j - 1] + lines[i + 2][j - 2] + lines[i + 3][j - 3]) == "XMAS":
                xmas_count += 1
    
    print(f"part 1 XMAS total: | {xmas_count} | \n")

    x_mas_count = 0
    for i in range(3, (size+3)):
        for j in range(3, (size + 3)):
            s1 = (lines[i - 1][j - 1] + lines[i][j] + lines[i + 1][j + 1])
            s2 = (lines[i + 1][j - 1] + lines[i][j] + lines[i - 1][j + 1])
            if ((s1 == "MAS") or (s1 == "SAM")) and ((s2 == "MAS") or (s2 == "SAM")):
                x_mas_count += 1
    
    print(f"part 2 X-MAS total: | {x_mas_count} | \n")





main()