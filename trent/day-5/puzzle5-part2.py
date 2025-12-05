import time
import intervaltree

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


def find_number_of_fresh_ids(freshRanges):
    intervals = []
    sum = 0
    numofFreshIDs = 0
    for freshRange in freshRanges:
        rangeStart = int(freshRange.split('-')[0])
        rangeEnd = int(freshRange.split('-')[1])
        if rangeStart != rangeEnd:
            intervals.append([rangeStart, (rangeEnd)])

    tree = intervaltree.IntervalTree.from_tuples(intervals)
    tree.merge_overlaps()
    for i in tree:
        # print(f"{i.begin}")
        sum += (i.end+1) - i.begin
    return sum


def main():
    freshRanges, IDList= get_input()
    numberOfIDs = find_number_of_fresh_ids(freshRanges)
    print(f"There are {numberOfIDs} available fresh IDs")
    return 0


starTime = time.time()
main()
endTime = time.time()
print(f"Runtime: {endTime - starTime}")