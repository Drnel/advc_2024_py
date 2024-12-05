def main():
    print("\n-----Solving advent of code 2024 day 5-----\n")
    file = open("input_texts/day_5.txt", "r")
    text = file.read()
    file.close()
    lines = text.split("\n")
    dictionary = {}
    for i in range(1,100):
        dictionary[i] = []

    linebreak = 0
    for line in lines:
        linebreak += 1
        if line == "":
            break
        temp_l = line.split("|")
        dictionary[int(temp_l[0])].append(temp_l[1])
    
    page_number_sum = 0

    illegal_fixed_page_number_sum = 0

    for line in lines[linebreak:]:
        legal = True
        temp_list = line.split(",")
        full_list = []
        for i in temp_list:
            for j in range(len(full_list)):
                if full_list[j] in dictionary[int(i)]:
                    legal = False
            full_list.append(i)
        if legal:
            page_number_sum += (int(full_list[len(full_list)//2]))
        else:
            for i in range(len(full_list)):
                for j in range(i):
                    if full_list[j] in dictionary[int(full_list[i])]:
                        temp = full_list[j]
                        full_list[j] = full_list[i]
                        full_list[i] = temp
            illegal_fixed_page_number_sum += (int(full_list[len(full_list)//2]))
    
    print(f"part 1 legal page number sum: | {page_number_sum} | \n")

    print(f"part 1 illegal fixed page number sum: | {illegal_fixed_page_number_sum} | \n")
    
    
    


main()