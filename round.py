#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program formats your address to a mailing address


def round_number(entered_input, decimal_input):
    rounded_num = entered_input[0] * 10.0 ** decimal_input
    rounded_num = int(rounded_num + 0.5)
    rounded_num = rounded_num / (10.0 ** decimal_input)

    entered_input[0] = rounded_num


def main():
    # This function is the main function
    entered_input = []

    try:
        number_input = input("Enter a number you want to round: ")
        number_input = float(number_input)
        decimal_input = input("Enter how many decimal places you want to round by: ")
        decimal_input = int(decimal_input)

        entered_input.append(number_input)

        round_number(entered_input, decimal_input)

        print("\nThe rounded number is {0}".format(entered_input[0]))
    except (Exception):
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
