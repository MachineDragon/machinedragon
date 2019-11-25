# wind_chill.py: Takes two floats t and v as command-line arguments and
# prints the wind chill w, calculated as w=35.74+0.6215t+(0.4275t-35.75)v^0.16.

import stdio
import sys

t = float(sys.argv[1])
v = float(sys.argv[2])
stdio.writeln(35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16)
