#!/usr/bin/env python3
import sys

"""
This file converts a postal zip code 
into a bar code, with a check at the end.
the check takes the sum of the zip code 
and brings the total to the next multiple 
of ten.
"""

barCodeList = ["||:::", ":::||", "::|:|", "::||:", ":|::|", ":|:|:"
        , ":||::", "|:::|", "|::|:", "|:|::"]

def printDigit(d):
    """
    This def is here as per assignment instructions,
    but was not needed. A better description of what
    function is expected to do would help alleviate confusion.
    """
    pass


def checkDigit(zipCode):
    """
    Calculates the check digit from the zipCode and returns it
    """
    sumNum = 0
    for num in zipCode:
        sumNum += int(num)
    mod = sumNum%10
    if mod == 0:         # if sum of zip numbers modulus 10 is zero return 0 for check digit
        return 0
    checkDigit = 10 - mod       # else check digit is 10 - (sumNum%10)
    return checkDigit


def printBarCode(zipCode):
    """
    Takes a String parameter called zipCode
    zipCode is iterated through with each char converted to an int
    The integer value is used to get its barcode from the index in barCodeList
    The integer number corresponds to the index in barCodeList
    The strings barCode concatonates all the pieces together including the check digit
    Then we print the barCode
    @Param
        : String named zipCode
    """
    barCode = "|"
    for num in zipCode:
        num = int(num)
        barCode += barCodeList[num]

    checkDigitIndex = checkDigit(zipCode)
    barCode += barCodeList[checkDigitIndex]
    barCode += "|"
    print(barCode)


# Main function
def main():
    """
    Test Function
    """
    pass


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
