
def get_tester():
    """This is a tester that I will use to see if the algorithm is correct"""
    tester = ["L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82"]

    return tester



def get_instructions():
    input_file = open("Day-1/input-day-one.txt", "r")
    input_list = input_file.readlines()
    input_list = [instruction.strip("\n") for instruction in input_list] # getting rid of the new lines

    return input_list    


def perform_rotations(rotation_instructions, upper_bound=100, starting_point=50):
    # get where we are starting at
    current_position = starting_point

    # count to see when we pass 0
    pass_zero_count = 0

    # read each instruction in the list
    for instruction in rotation_instructions:
        if instruction.startswith("L") or instruction.startswith("l"):
            current_position = (current_position - int(instruction[1:])) % upper_bound
        elif instruction.startswith("R") or instruction.startswith("r"):
            current_position = (current_position + int(instruction[1:])) % upper_bound
        
        if current_position == 0: pass_zero_count += 1

    return pass_zero_count

def main():
    rotation_instructions = get_instructions()
    print(perform_rotations(rotation_instructions))


if __name__ == "__main__":
    main()