# three_sort.py: Takes three integers as command-line arguments and prints
# them in ascending order, separated by spaces.

import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
minimum = min(x, y, z)
maximum = max(x, y, z)
middle = x + y + z - minimum - maximum
stdio.writeln(str(minimum) + " " + str(middle) + " " + str(maximum))
