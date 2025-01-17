#!/usr/bin/env python

import sys

program = sys.argv[0]
args = sys.argv[1:]

if len(args) != 2:
    print("Invalid args")
    print("usage:", program, "<input file>", "<output file>")
    sys.exit(1)


filename = args[0]
output = args[1]

if filename == output:
    print("Invalid args: input file and output file are the same")
    sys.exit(1)

with open(filename) as infile:
    with open(output, "w") as outfile:
        while line := infile.readline():
            line = line.rstrip()
            if line == "":
                continue
            outfile.write(f"positive:{line}\n")
            outfile.write("negative:\n")
            outfile.write("----\n")
