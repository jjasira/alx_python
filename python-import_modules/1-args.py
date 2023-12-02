if __name__ == "__main__":
    from variable_load_2 import a
argv = ["Heloo"]

length = len(argv)

if length == 0:
    print("{} arguments.".format(length))
elif length == 1:
    print("{} argument: ".format(length))
    for i, element in enumerate(argv):
        print("{}: {}".format((i+1), element))
elif length > 1:
    
    print("{} arguments: ".format(length))
    for i, element in enumerate(argv):
        print("{}: {}".format((i+1), element))

        