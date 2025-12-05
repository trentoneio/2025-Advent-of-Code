import argparse


test_input = ["987654321111111",
              "811111111111119",
              "234234234234278,"
              "818181911112111"]

def main(args):

    # using a set and sorting will do the trick
    if args.run_type == "t":
        pass

    elif args.run_type == "r":
        file = open("", "r")
        lines = file.readlines()

    else:
        print(f"Incorrect flag used: {args.run_type}")

    
    

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(description="Run the code with test or real input.", formatter_class=argparse.RawTextHelpFormatter)
    
    argument_parser.add_argument("--run_type", type=str, default="r",
                                 help="Describes whether you wish to run the code with the test input or the real input.\n" \
                                      "Options:\n" \
                                      "\t 't' : use test input\n" \
                                      "\t 'r' : use real input ")
    
    args = argument_parser.parse_args()
    
    main(args)
