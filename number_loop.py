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

        while loop_number < number:
            loop_number = loop_number + 1
            total = total + loop_number
        else:
            print("The sum off all numbers from 1 to {0} is {1}.".format(number, total))

    except Exception:
        print("\nThat was not an integer")
    print("\nDone.")


if __name__ == "__main__":
    main()
