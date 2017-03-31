#!/usr/bin/env python3
import sys
import urllib.request
import mod3 # pull module 3 to test

"""
This module/file is to test the functionality of the module 3 program
against a url file. 
"""


url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt"  # file being pulled


# Main function
def main():
    """
    For each line in reader object returned from urllib.request.urlopen(url)
        print the digit with imported mod3.py function printDigit(d)
        print the bar code with imported mod3.py function printBarCode(zipCode)
    """
    index = 0
    txt = urllib.request.urlopen(url)   #to pull in web data
    for line in txt.readlines():
        decode = line.decode("utf-8")   #to decode from binary
        decode = decode.replace("\n", "")
        print("Reading in the zip code:")
        print("Zip code:", decode)
        print("Translating to bar code:")
        # Check that string is all numbers
        # Check that string is 5 characters
        # If either condition fails print appropriate error
        # Else print the barcode from imported function
                
                # For testing the if statements
        #if index == 0:
        #    decode = "84c03"
        #if index == 1:
        #    decode = "Real Madrid"
        #if index == 2:
        #    decode = "843"
        
        if(not decode.isdigit()):   # to show error for using letters
            print("Error: Zip code is not all numeric")
        elif(len(decode) < 5 or len(decode) > 5):   # to show error for length
            print("Error: Zip code is not 5 digits")
        else:
            mod3.printBarCode(decode)
        print() 
        index += 1


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
