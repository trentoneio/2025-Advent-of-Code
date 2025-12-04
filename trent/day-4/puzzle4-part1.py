import numpy as np
import time

def get_input():
    file = open("/home/trentoneio/git-clones/2025-Advent-of-Code/day-4/input.txt","r")
    lines = file.readlines()
    lines = np.array([single_line.strip("\n") for single_line in lines])
    return lines


def find_valid_count(input):
    rows=len(input)
    cols=len(input[0])
    validCnt = 0
    # print(f"rows: {rows}\tcols: {cols}")
    for i in range(rows):
        for j in range(cols):
            adjCnt=0
            if (input[i][j] == '@'):
                # 1: top left
                if (i-1 >= 0 and j-1 >= 0):
                    if (input[i-1][j-1] == '@'):
                        adjCnt+=1
                # 2: above
                if (i-1 >= 0):
                    if (input[i-1][j] == '@'):
                        adjCnt+=1
                # 3: top right
                if (i-1 >= 0 and j+1 < cols):
                    if (input[i-1][j+1] == '@'):
                        adjCnt+=1
                # 4: left
                if (j-1 >= 0):
                    if (input[i][j-1] == '@'):
                        adjCnt+=1
                # 5: right
                if (j+1 < cols):
                    if (input[i][j+1] == '@'):
                        adjCnt+=1
                # 6: bottom left
                if (i+1 < rows and j-1 >= 0):
                    if (input[i+1][j-1] == '@'):
                        adjCnt+=1
                # 7: below
                if (i+1 < rows):
                    if (input[i+1][j] == '@'):
                        adjCnt+=1
                # 8: bottom right
                if (i+1 < rows and j+1 < cols):
                    if (input[i+1][j+1] == '@'):
                        adjCnt+=1
                
                # Check adjacent count
                if (adjCnt < 4):
                    validCnt += 1
    return validCnt


def main ():
    layout = get_input()
    validCount = find_valid_count(layout)
    print(f"validCount = {validCount}")
    # print(layout)
    # print("\n\n")
    # print(layout[0])
    # print(layout[0][0])
    # print(layout[-1])



starTime = time.time()
main()
endTime = time.time()
print(f"Runtime: {endTime - starTime}")