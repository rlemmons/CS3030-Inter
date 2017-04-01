#!/usr/bin/env python3
import sys

"""
This file converts a postal zip code 
into a bar code, with a check at the end.
the check takes the sum of the zip code 
and brings the total to the next multiple 
of ten.
"""

barCodeList = ["||:::", ":::||", "::|:|", "::||:", ":|::|", 
        ":|:|:", ":||::", "|:::|", "|::|:", "|:|::"]

binaryMap = ["11000", "00011", "00101", "00110", "01001",
        "01010", "01100", "10001", "10010", "10100"] 

def printDigit(d):
    """
    Calculates the check digit from the zipCode and returns it as its bar
    """
    checkDigit = ""
    sumNum = 0
    for num in d:
        sumNum += int(num)
    #print("sumNum:", sumNum)
    mod = sumNum%10
    #print("mod:", mod)
    if mod == 0:         # if sum of zip numbers modulus 10 is zero return 0 for check digit
        for binary in binaryMap[0]:
            if binary == "1":
                checkDigit += "|"
            elif binary == "0":
                checkDigit += ":"
        return checkDigit
    digit = 10 - mod       # else check digit is 10 - (sumNum%10)
    #print("digit:", digit)
    #print("binary:", binaryMap[digit])
    for binary in binaryMap[digit]:
        if binary == "1":
            checkDigit += "|"
        elif binary == "0":
            checkDigit += ":"
    return checkDigit

def printBarCode(zipCode):
    """
    Takes a String parameter called zipCode
    zipCode is iterated through with each char converted to an int
    The integer value is used to get its barcode from the index in barCodeList
    The integer number corresponds to the index in binaryMap
    The strings barCode concatonates all the pieces together including the check digit
    Then we print the barCode
    @Param
        : String named zipCode
    """
    barCode = "|"
    for num in zipCode:
        num = int(num)
        for binary in binaryMap[num]:
            if binary == "1":
                barCode += "|"
            elif binary == "0":
                barCode += ":"
    barCode += printDigit(zipCode)
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
