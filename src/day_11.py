import functools

def main():
    print("\n-----Solving advent of code 2024 day 11-----\n")
    file = open("input_texts/day_11.txt", "r")
    text = file.read()
    file.close()
    
    stones = text.split(" ")
    blinks = 25
    total_stones = 0
    for stone in stones:
        total_stones += recursive_stone_length(int(stone), blinks)

    print(f"part 1 (25 blinks) number of stones: | {total_stones} | \n")

    blinks = 75
    total_stones = 0
    for stone in stones:
        total_stones += recursive_stone_length(int(stone), blinks)

    print(f"part 1 (75 blinks) number of stones: | {total_stones} | \n")

@functools.cache
def recursive_stone_length(num, depth):
    if depth == 0:
        return 1
    if num == 0:
        return recursive_stone_length(1, (depth - 1))
    strn = str(num)
    if (len(strn) % 2) == 1:
        return recursive_stone_length((num * 2024), (depth - 1))
    left = recursive_stone_length(int(strn[:(len(strn) // 2)]), (depth - 1))
    right = recursive_stone_length(int(strn[(len(strn) // 2):]), (depth - 1))
    return left + right
    


main()