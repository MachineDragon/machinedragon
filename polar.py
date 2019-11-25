# polar.py: Takes two floats x and y representing the Cartesian coordinates of
# a point as command-line arguments and prints the corresponding polar
# coordinates, calculated as r=(x^2+y^2)^0.5 and theta=arctan(y/x).

import math
import stdio
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
stdio.writeln((x ** 2 + y ** 2) ** 0.5)
stdio.writeln(math.atan2(y, x))
