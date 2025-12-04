import argparse
# WRONG SOLUTION:
# thinking that if you find the set of a number (unique digits), multiply the length of that set by two


# my test input
test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
              1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
              824824821-824824827,2121212118-2121212124"

def break_num_in_half(number):
    num_str = str(number)
    num_len = len(num_str)
    if num_len % 2 != 0:
        # return something outrageous if the number if not even
        return 0xfffffff, 0xfffffff

    middle_idx = int(num_len/2)
    return int(num_str[:middle_idx]), int(num_str[middle_idx:])


def get_numbers_in_range(a_range):
    lower_num, upper_num = a_range.split("-")
    lower_num = int(lower_num)
    upper_num = int(upper_num)
    return [num for num in range(lower_num, upper_num + 1)]

def check_num_validity(ids):
    invalid_nums = []
    for num in ids:
        half_1, half_2 = break_num_in_half(num)

        if half_1 == 0xfffffff or half_2 == 0xfffffff:
            continue

        if half_1 == half_2:
            invalid_nums.append(num)

    return invalid_nums

def main(args):

    
    if args.run_type == "t":
        # test ranges
        ranges_ls = test_input.split(",")
        ranges_ls = [a_range.strip() for a_range in ranges_ls]

    else:
        file = open("/Users/brizzybri/Documents/Coding/Python_Code/Misc Projects/AdventOfCode2025/2025-Advent-of-Code/brianna/Day-2/input-day-two.txt", "r")
        lines = file.readlines()

        # grab the individual ranges from the txt file
        ranges_ls = lines[0].split(",")

    invalid_ids_sum = 0
    for a_range in ranges_ls:
        ids = get_numbers_in_range(a_range)
        invalid_ids_sum += sum(check_num_validity(ids))

    
    
    print(invalid_ids_sum)


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(description="Run the code with test or real input.", formatter_class=argparse.RawTextHelpFormatter)
    
    argument_parser.add_argument("--run_type", type=str, default="r",
                                 help="Describes whether you wish to run the code with the test input or the real input.\n" \
                                      "Options:\n" \
                                      "\t 't' : use test input\n" \
                                      "\t 'r' : use real input ")
    
    args = argument_parser.parse_args()
    
    main(args)
