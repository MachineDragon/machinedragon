# three_dice.py: writes the sum of three random integers between 1 and 6, such
# as you might get when rolling three dice.

import random
import stdio

d1 = int(6 * random.random()) + 1
d2 = int(6 * random.random()) + 1
d3 = int(6 * random.random()) + 1
stdio.writeln(d1 + d2 + d3)
