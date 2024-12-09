def main():
    print("\n-----Solving advent of code 2024 day 9-----\n")
    file = open("input_texts/day_9.txt", "r")
    text = file.read()
    file.close()
    file_blocks = []
    case = "file"
    current_id = 0
    for i in text:
        if case == "file":
            file_blocks.extend([current_id] * int(i))
            case = "space"
            current_id += 1
            continue
        if case == "space":
            file_blocks.extend(["."] * int(i))
            case = "file"

    left = 0
    right = len(file_blocks) - 1

    while(True):
        while(file_blocks[left] != "."):
            left += 1
        while(file_blocks[right] == "."):
            right -= 1
        if right <= left:
            break
        file_blocks[left], file_blocks[right] = file_blocks[right], file_blocks[left]
    
    check_sum = 0
    for i in range(len(file_blocks)):
        if file_blocks[i] == ".":
            break
        check_sum += (i * file_blocks[i])

    print(f"part 1 checksum: | {check_sum} | \n")

    file_blocks = []
    case = "file"
    current_id = 0
    for i in text:
        if case == "file":
            file_blocks.append([current_id, int(i)])
            case = "space"
            current_id += 1
            continue
        if case == "space":
            file_blocks.append([".", int(i)])
            case = "file"

    current_id = 1000000000

    while(current_id > 0):
        ind = len(file_blocks)
        while(True):
            ind -= 1
            if file_blocks[ind][0] == ".":
                continue
            if file_blocks[ind][0] < current_id:
                current_id = file_blocks[ind][0]
                # print(f"currentid {current_id}")
                # print(file_blocks)
                for j in range(ind):
                    if file_blocks[j][0] == ".":
                        if file_blocks[j][1] >= file_blocks[ind][1]:
                            # print(j)
                            file_blocks[j][1] = file_blocks[j][1] - file_blocks[ind][1]
                            temp = file_blocks[ind][:]
                            file_blocks[ind][0] = "."
                            # print(temp)
                            file_blocks.insert(j, temp)
                            # print(file_blocks)
                            break
                break
                        

    
    # print(file_blocks)
    
    file_blocks_render = []

    for item in file_blocks:
        file_blocks_render.extend([item[0]] * item[1])
    
    # print("".join([str(i) for i in file_blocks_render]))

    check_sum = 0
    for i in range(len(file_blocks_render)):
        if file_blocks_render[i] == ".":
            continue
        check_sum += (i * file_blocks_render[i])

    print(f"part 2 checksum: | {check_sum} | \n")



main()