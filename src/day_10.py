def main():
    print("\n-----Solving advent of code 2024 day 10-----\n")
    file = open("input_texts/day_10.txt", "r")
    text = file.read()
    file.close()
    hmap = text.split("\n")
    hmap = [[int(ch) for ch in l] for l in hmap]
    scores_sum = 0
    ratings_sum = [0]
    for y in range(len(hmap)):
        for x in range(len(hmap[0])):
            s = set()
            if hmap[y][x] == 0:
                search_r(hmap, y, x, s, ratings_sum)
                scores_sum += len(s)
    
    print(f"part 1 sum of scores: | {scores_sum} | \n")

    print(f"part 1 sum of ratings: | {ratings_sum[0]} | \n")


def search_r(hmap, y, x, s, ratings_sum):
    if hmap[y][x] == 9:
        s.add((y, x))
        ratings_sum[0] += 1
        return
    # up
    if y != 0:
        if hmap[y - 1][x] == (hmap[y][x] + 1):
            search_r(hmap, (y - 1), x, s, ratings_sum)
    # down
    if y != len(hmap) - 1:
        if hmap[y + 1][x] == (hmap[y][x] + 1):
            search_r(hmap, (y + 1), x, s, ratings_sum)
    # left
    if x != 0:
        if hmap[y][x - 1] == (hmap[y][x] + 1):
            search_r(hmap, y, (x - 1), s, ratings_sum)
    # right
    if x != len(hmap[0]) - 1:
        if hmap[y][x + 1] == (hmap[y][x] + 1):
            search_r(hmap, y, (x + 1), s, ratings_sum)
    


main()