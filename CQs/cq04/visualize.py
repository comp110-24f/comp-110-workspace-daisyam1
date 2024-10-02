"""CQ04 Visualize"""

__author__ = "730740592"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"

print(concat(x, y))

print(get_coords(x, y))
