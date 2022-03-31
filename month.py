#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that calculates a month from a Number


def main():
    # This function is the main program

    # input
    Number = int(input("Enter a number for a Month (1-12): "))

    # Process and output
    if Number == 1:
        print("Your month is January")

    elif Number == 2:
        print("Your month is February")

    elif Number == 3:
        print("Your month is March")

    elif Number == 4:
        print("Your month is April")

    elif Number == 5:
        print("Your month is May")

    elif Number == 6:
        print("Your month is June")

    elif Number == 7:
        print("Your month is July")

    elif Number == 8:
        print("Your month is August")

    elif Number == 9:
        print("Your month is September")

    elif Number == 10:
        print("Your month is October")

    elif Number == 11:
        print("Your month is November")

    elif Number == 12:
        print("Your month is December")

    else:
        print("That is none of the months")

    print("\nDone.")


if __name__ == "__main__":
    main()
