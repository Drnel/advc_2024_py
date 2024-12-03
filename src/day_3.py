import re

def main():
    print("\n-----Solving advent of code 2024 day 3-----\n")
    file = open("input_texts/day_3.txt", "r")
    text = file.read()
    file.close()
    matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", text)
    total = 0
    for item in matches:

        halves = item.split(",")
        num1 = int(halves[0][4:])
        num2 = int(halves[1][:-1])
        total += (num1 * num2)
    
    print(f"part 1 total: | {total} | \n")

    matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", text)
    total = 0
    disabled = False
    for item in matches:
        if item == "do()":
            disabled = False
            continue
        if item == "don't()":
            disabled = True
            continue
        if disabled:
            continue
        halves = item.split(",")
        num1 = int(halves[0][4:])
        num2 = int(halves[1][:-1])
        total += (num1 * num2)
    
    print(f"part 2 total: | {total} | \n")




main()