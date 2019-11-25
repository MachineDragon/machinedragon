import stdio
import sys


# Returns the sum S(n) = 1 + 2 + ... + n, computed iteratively.
def sum_iter(n):
    if n == 1:
        return n
    if n <= 0:
        return 'input value must be greater than o equal to one'
    s = 0
    for i in range(1, n+1):
        s += i
    return s


# Returns the sum S(n) = 1 + 2 + ... + n, computed recursively.
def sum_rec(n):
    if n == 1:
        return n
    if n <= 0:
        return 'input value must be greater than or equal to one'
    return n + sum_rec(n - 1)


# Test client [DO NOT EDIT]. Reads an integer n from command line and
# writes the sum S(n) = 1 + 2 + ... + n, computed both iteratively and
# recursively.
def _main():
    n = int(sys.argv[1])
    stdio.writeln(sum_iter(n))
    stdio.writeln(sum_rec(n))


if __name__ == '__main__':
    _main()
