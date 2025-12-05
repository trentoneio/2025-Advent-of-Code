import argparse
import numpy as np
import time


test_input = np.array(["..@@.@@@@.",
                        "@@@.@.@.@@", 
                        "@@@@@.@.@@", 
                        "@.@@@@..@.",
                        "@@.@@@@.@@",
                        ".@@@@@@@.@",
                        ".@.@.@.@@@",
                        "@.@@@.@@@@",
                        ".@@@@@@@@.",
                        "@.@.@@@.@."])


def check_for_rolls():
    pass


def create_binary_matrix(input_arr):
    """
    Creates a binary matrix from the str matrix

    Within the matrix:
        `.` = 0
        `@` = 1

    Ex: 
    If the input matrix is 
    [[..@]
     [@@.]
     [.@.]]

    Output will be
    [[0,0,1]
     [1,1,0]
     [0,1,0]]
    
    """
    num_rows = input_arr.shape[0]
    num_cols = len(input_arr[0])
    bin_matrix = np.zeros((num_rows, num_cols))

    for i in range(num_rows):
        for j in range(num_cols):
            if input_arr[i][j] == "@":
                bin_matrix[i][j] = 1
    
    # padding the outside of the array with zeroes to help with the filter
    return np.pad(bin_matrix, 1, 'constant', constant_values=0)


def matrix_solutuion(input_array):
    bin_input_mat = create_binary_matrix(input_array)

    # what we will returning... the number of accessible rolls
    accessible_rolls = 0
    
    # these row/col counts should still keep us in bounds (using the original shape and NOT the shape of the bin padded array)
    num_rows = input_array.shape[0]
    num_cols = len(input_array[0])

    # print(bin_input_mat)

    found_a_roll_in_iter = 1
    while(found_a_roll_in_iter):

        round_accessible_rolls = 0

        for i in range(num_rows):
            for j in range(num_cols):
                
                # if the space does not have a roll (which means the binary=0), skip it 
                if bin_input_mat[i+1, j+1] == 0:
                    continue
                
                # grab the sum of the kernel window (subtract by 1 to not count for the roll in the middle)
                kernel_sum = np.sum(bin_input_mat[i:i+3, j:j+3]) - 1
   
                # if the sum is greater than 4, we cannot use the roll... onto the next
                if kernel_sum < 4:
                    round_accessible_rolls += 1
                    
                    # we can no longer use that roll, replace t with a 0
                    bin_input_mat[i+1, j+1] = 0

        
        accessible_rolls += round_accessible_rolls

        # we found a roll this round! try another loop to see if we find more
        if round_accessible_rolls > 0:
            found_a_roll_in_iter = 1
        # bail out, we did not find another roll
        else:
            found_a_roll_in_iter = 0

    print(f"How many rolls of paper in total can be removed by the Elves and their forklifts?\nBA answer: {accessible_rolls}")



def main(args):

    # using a set and sorting will do the trick
    if args.run_type == "t":
        lines = test_input

    elif args.run_type == "r":
        file = open("/Users/brizzybri/Documents/Coding/Python_Code/Misc Projects/AdventOfCode2025/2025-Advent-of-Code/brianna/Day-4/input-day-four.txt", "r")
        lines = file.readlines()
        lines = np.array([single_line.strip("\n") for single_line in lines])

    else:
        print(f"Incorrect flag used: {args.run_type}")


    matrix_solutuion(lines)


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(description="Run the code with test or real input.", formatter_class=argparse.RawTextHelpFormatter)
    
    argument_parser.add_argument("--run_type", type=str, default="r",
                                 help="Describes whether you wish to run the code with the test input or the real input.\n" \
                                      "Options:\n" \
                                      "\t 't' : use test input\n" \
                                      "\t 'r' : use real input ")
    
    args = argument_parser.parse_args()
    
    start_time = time.time()
    main(args)
    end_time = time.time()
    total_time = end_time - start_time

    print(f"total time = {total_time} sec")
