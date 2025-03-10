import sys
import random
import json
import math
from typing import Tuple

# if you explored the repo I made and found this file or run.py, the reason I didn't finish them is due to determining that the additional late penalty + effort wouldn't be worth the points gained

# setting up rng so I can print the seed
seed = random.randrange(sys.maxsize)
# set seed here if result needs to be recreated
rng = random.Random(seed)


def main():
    if len(sys.argv) < 3:
        print(
            f"Insufficient argument count usage {sys.argv[0]} input_file model_file_location",
            file=sys.stderr,
        )
        sys.exit(1)

    digits = []
    with open(sys.argv[1], "r") as input:
        digits = [nums_from_line(line[:-2]) for line in input.readlines()]
    print(f"seed: {seed}")
    # initialize random matrix
    model = Matrix.random(1, 256)
    visited = []
    for digit in digits:
        desired = 0
        match digit[0]:
            case 1:
                desired = 1
            case 5:
                desired = -1
            case _:
                raise Exception("???")
        prediction = super_ceil(clamp((model @ Matrix.col(digit[1:])).to_scalar()))
        adjusted = adjust(model, digit[1:], prediction == desired)
        model = better(model, adjusted, visited)
        visited.append(digit)

    print(f"training done writing model to file `{sys.argv[2]}`", sys.stderr)
    with open(sys.argv[2], "w+") as output:
        model.dump(output)
    print(f"finished writing model to file")


# my understanding is that  this is just subtracting the point(after the number) from the matrix if the guess was wrong
def adjust(m: "Matrix", point: list[float | int], correct: bool) -> "Matrix": ...
# just see which model classifies more points correctly and return it
def better(a: "Matrix", b: "Matrix", prior: list[list[float | int]]) -> "Matrix": ...


def clamp(x: float | int, mi: float | int = -1, ma: float | int = 1):
    return max(min(x, ma), mi)


def super_ceil(x: float | int):
    if x < 0:
        return math.floor(x)
    else:
        math.ceil(x)


# I think i'm not allowed to use numpy so I wrote my own Matrix class
class Matrix:
    _row_count: int = 0
    _column_count: int = 0
    _underlying: list[float | int] = []

    def __init__(self, row_count: int, column_count: int, data: list[float | int]):
        if len(data) != row_count * column_count:
            raise Exception("fuck")
        self._row_count = row_count
        self._column_count = column_count
        self._underlying = data

    @staticmethod
    def random(row_count: int, column_count: int):
        data = [rng.random() for _ in range(row_count * column_count)]
        return Matrix(row_count, column_count, data)

    @staticmethod
    def const(row_count: int, column_count: int, val: float = 0):
        data = [val for _ in range(row_count * column_count)]
        return Matrix(row_count, column_count, data)

    @staticmethod
    def row(some_list: list[float | int]):
        return Matrix(1, len(some_list), some_list)

    @staticmethod
    def col(some_list: list[float | int]):
        return Matrix(len(some_list), 1, some_list)

    def to_list(self) -> list[float | int]:
        if self._row_count != 1 and self._column_count != 1:
            raise Exception("cannot convert to list if rows or columns is not 1")
        return self._underlying

    def to_scalar(self) -> float:
        if self._row_count == 1 and self._column_count == 1:
            return self._underlying[0]
        raise Exception("cannot convert matrix to scalar if it isn't 1x1")

    # added so I can copy paste
    @staticmethod
    def load(file):
        obj: dict = json.load(file)
        return Matrix(obj["rows"], obj["columns"], obj["data"])

    def dump(self, file):
        obj = dict()
        obj["rows"] = self._row_count
        obj["columns"] = self._column_count
        obj["data"] = self._underlying
        json.dump(obj, file)

    def __add__(self, rhs: "Matrix") -> "Matrix":
        if type(rhs) is not Matrix:
            raise TypeError("cannot add a matrix to not a matrix")
        if self._row_count != rhs._row_count or self._column_count != rhs._column_count:
            raise Exception("Row or column counts don't match up")
        return Matrix(
            self._row_count,
            self._column_count,
            [a + b for a, b in zip(self._underlying, rhs._underlying)],
        )

    def __sub__(self, rhs: "Matrix") -> "Matrix":
        if type(rhs) is not Matrix:
            raise TypeError("cannot subtract not a matrix from a matrix")
        if self._row_count != rhs._row_count or self._column_count != rhs._column_count:
            raise Exception("Row or column counts don't match up")
        return Matrix(
            self._row_count,
            self._column_count,
            [a - b for a, b in zip(self._underlying, rhs._underlying)],
        )

    def __repr__(self) -> str:
        ret = ""
        for r in range(self._row_count):
            for c in range(self._column_count):
                ret += str(self[r, c]) + " "
            ret += "\n"
        return ret[:-1]

    def __matmul__(self, rhs: "Matrix") -> "Matrix":
        match rhs:
            case Matrix():
                return self._mat_mul(rhs)
            case _:
                raise TypeError("Can only matrix multiply with matrix or with list")

    def __rmatmul__(self, lhs: float | int):
        match lhs:
            case float():
                return Matrix(
                    self._row_count,
                    self._column_count,
                    [i * lhs for i in self._underlying],
                )
            case int():
                return float(lhs) @ self
            case _:
                raise TypeError(
                    "Cannot multiply matrix by left side by anything other than another matrix or scalar"
                )

    def _setitem(self, row: int, column: int, item: float | int):
        self._underlying[row * self._column_count + column] = item

    def _mat_mul(self, rhs: "Matrix") -> "Matrix":
        row_count = self._row_count
        col_count = rhs._column_count
        ret = Matrix(row_count, col_count, [0.0 for _ in range(row_count * col_count)])
        for row_num in range(row_count):
            for col_num in range(col_count):
                # definition of matrix multiplication
                # https://en.wikipedia.org/wiki/Matrix_multiplication#Matrix_times_matrix
                ret._setitem(
                    row_num,
                    col_num,
                    sum(
                        self[row_num, k] * rhs[k, col_num]
                        for k in range(self._column_count)
                    ),
                )
        return ret

    def __getitem__(self, row_col: Tuple[int, int]) -> int | float:
        return self._underlying[row_col[0] * self._column_count + row_col[1]]


def nums_from_line(line: str) -> list[float]:
    return [float(x) for x in line.split(" ")]


if __name__ == "__main__":
    main()
