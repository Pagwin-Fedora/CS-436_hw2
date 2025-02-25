# done as preprocessing for Q5 and Q6

import sys

# there may be a more elegant way to open multiple files in python but whatever
with open(sys.argv[1], "r") as input:
    with open(sys.argv[2], "w+") as output:
        # each digit is a line which is convenient
        for line in input.readlines():
            # remove the ending newline and space char
            line = line[:-2]

            # parse nums (could just parse the first but whatever, can copy this code for other things)
            nums = [float(x) for x in line.split(" ")]
            if nums[0] == 1 or nums[0] == 5:
                print(line, file=output)
