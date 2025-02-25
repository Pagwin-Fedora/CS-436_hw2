# done as preprocessing for Q5 and Q6

import sys

with open(sys.argv[1], "r") as input:
    with open(sys.argv[2], "w+") as output:
        for line in input.readlines():
            line = line[:-2]
            nums = [float(x) for x in line.split(" ")]
            if nums[0] == 1 or nums[0] == 5:
                print(line, file=output)
