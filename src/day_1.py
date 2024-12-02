def main():
    print("\n-----Solving advent of code 2024 day 1-----\n")
    file = open("input_texts/day_1.txt", "r")
    lines = file.read().split("\n")
    file.close()
    l1 = []
    l2 = []
    for line in lines:
        nums = line.split("   ")
        l1.append(int(nums[0]))
        l2.append(int(nums[1]))
    l1.sort()
    l2.sort()

    total = 0
    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])
    
    print(f"part 1 total difference: | {total} | \n");

    similarity_score = 0

    for num in l1:
        similarity_score += (num * (l2.count(num)))
    
    print(f"part 2 similarity score: | {similarity_score} | \n");


main()