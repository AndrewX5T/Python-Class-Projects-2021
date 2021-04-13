# Andrew Hein
# Advanced Programming - Week 9
# 2021/3/23
# calc_sum.py

import sys

args = sys.argv[1:]


def calc_sum(sum, args):
    if len(args) > 0:
        value = int(args.pop(0))
        return calc_sum(sum + value, args)
    else:
        return sum


def main():
    print(calc_sum(0, args))


if __name__ == "__main__":
    main()
