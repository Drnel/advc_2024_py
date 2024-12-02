def main():
    print("\n-----Solving advent of code 2024 day 2-----\n")
    file = open("input_texts/day_2.txt", "r")
    lines = file.read().split("\n")
    file.close()
    
    safe_counter = 0
    for line in lines:
        nums = line.split(" ")
        report = [int(num) for num in nums]
        
        safe = check_safety(report)

        if safe:
            safe_counter += 1
    
    print(f"part 1 safe counter: | {safe_counter} | \n")

    safe_counter = 0
    for line in lines:
        nums = line.split(" ")
        report = [int(num) for num in nums]
        
        safe = check_safety(report)

        for i in range(len(report)):
            if safe == True:
                break
            damped_report = report[:i] + report[i+1:]
            if check_safety(damped_report):
                safe = True
        
        if safe:
            safe_counter += 1
    
    print(f"part 2 damped safe counter: | {safe_counter} | \n")



def check_safety(report):
    status = "increasing"
    safe = True

    if report[0] > report[1]:
        status = "decreasing"

    for i in range(len(report) - 1):
        if status == "increasing":
            if ((report[i + 1] - report[i]) > 3) or ((report[i + 1] <= report[i])):
                safe = False
        if status == "decreasing":
            if ((report[i] - report[i + 1]) > 3) or ((report[i + 1] >= report[i])):
                safe = False
    return safe

main()