
import sys

# yes I'm importing the file I used to train, I'm lazy
from train import Matrix,  nums_from_line


def main():
    if len(sys.argv) < 3:
        print(f"Insufficient argument count usage {sys.argv[0]} model_file data", file=sys.stderr)
        sys.exit(1)
    model = None
    with open(sys.argv[1], "r") as input:
        model = Matrix.load(input)
    data = []
    with open(sys.argv[2], "r") as input:
        data = [nums_from_line(line[:-2]) for line in input.readlines()]
    print(f"E = {measure_error(model, data)}")

def measure_error(model:"Matrix", data:list[list[float]])->float:...

