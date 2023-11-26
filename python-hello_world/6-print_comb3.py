for i in range(10):
    for j in range(i+1, 10):
        print("{:02d}".format(i * 10 + j), end=", " if (i, j) != (8, 9) else "\n")