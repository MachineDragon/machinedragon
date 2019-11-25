import stdio
import sys


# Returns a to the power b, computed recursively.
def power(a, b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return a * power(a, b - 1)
    return power(a * a, b / 2)


# Test client [DO NOT EDIT]. Reads integers a and b from command line and
# writes the value of a to the power b, computed recursively.
def _main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    stdio.writeln(power(a, b))


if __name__ == '__main__':
    _main()
