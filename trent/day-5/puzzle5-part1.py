import time

def get_input():
    emptyLineFound = 0
    rangeList = []
    IDList = []
    with open("/grmn/prj/aoem/garmin/misc/funbox/advent-of-code/trent/day-5/input.txt","r") as file:
        for line in file:
            if emptyLineFound == 0:
                if line != "\n":
                    line = line.strip("\n")
                    rangeList.append(line)
                else:
                    emptyLineFound = 1
            else:
                line = int(line.strip("\n"))
                IDList.append(line)
    file.close()
    return rangeList,IDList


def find_fresh_ingredients(freshRanges,IDList):
    freshIngredients = []
    for ID in IDList:
        for freshRange in freshRanges:
            rangeStart = int(freshRange.split('-')[0])
            rangeEnd = int(freshRange.split('-')[1])
            if (ID in range (rangeStart,rangeEnd+1)):
                freshIngredients.append(ID)
                break
    return freshIngredients

def main():
    freshRanges, IDList= get_input()
    freshIngredients = find_fresh_ingredients(freshRanges,IDList)
    print(f"There are {len(freshIngredients)} fresh ingredients")
    return 0


starTime = time.time()
main()
endTime = time.time()
print(f"Runtime: {endTime - starTime}")