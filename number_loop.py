#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a loop number adder


def main():

    # This is aloop number adder with try and catch
    total = 0
    loop_number = 0

    # input
    number_string = input("Enter your number: ")

    # process & output
    try:
        number = int(number_string)
        if number < 0:
            print("Not Defined")
        elif number == 0:
            print("1")
        else:
            for loop_number in range(number + 1):
                total = loop_number * loop_number
                print("{0}² = {1}.".format(loop_number, total))
    except Exception:
        print("\nThat was not an integer")
    print("\nDone.")


if __name__ == "__main__":
    main()
