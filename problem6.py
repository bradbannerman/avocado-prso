# -problem3_6.py *- coding: utf-8 -*-

import sys

infilename = sys.argv[1]
outfilename = sys.argv[2]

infile = open(infilename)
outfile = open(outfilename, "w")

for line in infile:
    charct = 0
    line = line.strip("\n")
    charct = charct + len(line)
    outfile.write(str(charct))
    outfile.write("\n")

infile.close()
outfile.close()
