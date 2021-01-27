def problem3_1(txtfilename):
    """ Opens file and prints it line by line, counting the characters."""
    infile = open(txtfilename)
    charct = 0          # initialise character counter.
    for line in infile:
        print(line, end='')
        charct = charct + len(line)
    print()
    print()
    print("There are", charct, "letters in the file.")
