#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args_count = len(sys.argv) - 1  # The first element in sys.argv is the script name
    
    if args_count == 0:
        print("0 arguments.")
    elif args_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_count))

    for i in range(1, args_count + 1):
        print("{}: {}".format(i, sys.argv[i]))