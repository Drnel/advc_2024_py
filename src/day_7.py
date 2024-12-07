def main():
    print("\n-----Solving advent of code 2024 day 7-----\n")
    file = open("input_texts/day_7.txt", "r")
    text = file.read()
    file.close()
    lines = text.split("\n")
    calibration_list = []
    for line in lines:
        parts = line.split(": ")
        result = int(parts[0])
        nums = [int(chr) for chr in parts[1].split(" ")]
        if recursive_res(result, nums[0], nums[1:]):
            calibration_list.append(result)
    
    calibration_sum = 0
    for i in calibration_list:
        calibration_sum += i
    
    print(f"part 1 total calibration result: | {calibration_sum} | \n")

    calibration_list = []
    for line in lines:
        parts = line.split(": ")
        result = int(parts[0])
        nums = [int(chr) for chr in parts[1].split(" ")]
        if recursive_res_with_string(result, nums[0], nums[1:]):
            calibration_list.append(result)
    
    calibration_sum = 0
    for i in calibration_list:
        calibration_sum += i

    print(f"part 2 new total calibration result: | {calibration_sum} | \n")


def recursive_res(result, current, nums):
    if len(nums) == 0:
        if result == current:
            return True
        else:
            return False

    if recursive_res(result, current + nums[0], nums[1:]) == True:
        return True
    if recursive_res(result, current * nums[0], nums[1:]) == True:
        return True
    return False

def recursive_res_with_string(result, current, nums):
    if len(nums) == 0:
        if result == current:
            return True
        else:
            return False

    if recursive_res_with_string(result, current + nums[0], nums[1:]) == True:
        return True
    if recursive_res_with_string(result, current * nums[0], nums[1:]) == True:
        return True
    if recursive_res_with_string(result, int(str(current) + str(nums[0])), nums[1:]) == True:
        return True
    return False



main()