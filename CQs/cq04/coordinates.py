"""CQ04 Coordinates"""

__author__ = "730740592"


def get_coords(xs: str, ys: str) -> None:
    x = 0
    while x < len(xs):
        y = 0
        while y < len(xs):
            print(str((xs[x], ys[y])))
            y += 1
        x += 1
