# plotting the first 2 digits in the file given

import sys
import matplotlib.pyplot as plt


def main():
    line1 = ""
    line2 = ""

    with open(sys.argv[1], "r") as input:
        line1 = input.readline()[:-2]
        line2 = input.readline()[:-2]

    digit1 = nums_from_line(line1)
    digit2 = nums_from_line(line2)
    num1 = digit1[0]
    num2 = digit2[0]
    pixels1 = gridify(digit1[1:])
    pixels2 = gridify(digit2[1:])
    plt.figure(1)
    plt.imshow(pixels1, cmap="gray", vmin=-1, vmax=1)
    plt.figure(2)
    plt.imshow(pixels2, cmap="gray", vmin=-1, vmax=1)
    plt.show()


def nums_from_line(line):
    return [float(x) for x in line.split(" ")]


def gridify(pixels, *, width=16, height=16, func=lambda x: x):
    if len(pixels) != width * height:
        raise Exception("bad")
    idx = 0
    lines = []
    for _ in range(height):
        line = []
        for _ in range(width):
            line.append(func(pixels[idx]))
            idx += 1
        lines.append(line)
    return lines


if __name__ == "__main__":
    main()
