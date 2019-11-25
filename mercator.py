# mercator.py: Takes three floats Lambda0, Phi, and Lambda as command-line
# arguments and prints its projection, i.e., the x and y values separated
# by a space, calculated using x=Lambda-Lambda0 and
# y=ln((1+sin(Phi))/(1-sin(Phi)))/2.

import math
import stdio
import sys

lam0 = float(sys.argv[1])
phi = math.radians(float(sys.argv[2]))
lam = float(sys.argv[3])
x = lam - lam0
y = 0.5 * math.log((1 + math.sin(phi)) / (1 - math.sin(phi)))
stdio.writeln(str(x) + " " + str(y))
