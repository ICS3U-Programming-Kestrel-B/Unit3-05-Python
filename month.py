#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 13, 2022
# This program asks for an integer
# between 1 and 12 and tells you
# what month the integer is
# related to


def find_month(month):
    # assigning value to find_month
    months = {
        1: "January is the first month".format(month),
        2: "February is the second month".format(month),
        3: "March is the third month".format(month),
        4: "April is the fourth month".format(month),
        5: "May is the fifth month".format(month),
        6: "June is the sixth month".format(month),
        7: "July is the seventh month".format(month),
        8: "August is the eighth month".format(month),
        9: "September is the ninth month".format(month),
        10: "October is the tenth month".format(month),
        11: "November is the eleventh month".format(month),
        12: "December is the twelfth month".format(month),
    }
    # error message
    return months.get(
        month,
        "Please enter a valid number. {} is not valid.".format(month),
    )


if __name__ == "__main__":
    # introduction text
    print("This program asks for an integer")
    print("between 1 and 12 and tells you")
    print("what month the integer is")
    print("related to")
    print("")

    # getting month_num
    month_num = int(input("Enter a number (1 - 12): "))

    # line break
    print("")

    # printing month_num
    print(find_month(month_num))

    # line break
    print("")
