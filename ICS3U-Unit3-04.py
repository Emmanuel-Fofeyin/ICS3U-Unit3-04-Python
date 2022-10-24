#!/usr/bin/env python3

# Created by: Emmanuel Fofeyin
# Created on: Oct 2022
# This program checks if integers are positive, negative or just zero
# learning if...then...elseif...else... statements in python.


def main():

    # input
    number = int(input("Enter an integer: "))

    # process and output
    if number > 0:
        print("\n{0:,} is a positive number.".format(number))
    elif number < 0:
        print("\n{0:,} is a negative number.".format(number))
    else:
        print("\n{0} is Just zero.".format(number))

    print("\n\nDone.")


if __name__ == "__main__":
    main()
