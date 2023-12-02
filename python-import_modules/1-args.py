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

        