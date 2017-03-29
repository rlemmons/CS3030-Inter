#!/usr/bin/env python3
import sys
import requests
import csv
import t1mod1

url = 'http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv'

def help():
    """
    Help function displays a proper function call
    e.g.
        ./minivanTest.py
                -or-
        python3 minivanTest.py
    
    """
    print("Usage is: ./minivanTest.py")

def check_code(code):
    """
    Function checks the return code passed from another function imported from t1mod1.get_code(list)
    The return code determines the final output of the program
    """
    if(code == 0):
        print("Both doors stay closed.")
    elif(code == 1):
        print("Left door opens.")
    elif(code == 2):
        print("Right door opens.")
    elif(code == 3):
        print("Both doors open.")
    else:
        print("Invalid Record: Both doors stay closed.")


def read_csvFile():
    """
    Function gets the csv from a URL
    Return:
        return the csv reader
    """
    response = requests.get(url)
    data = response.text
    data = data.replace(" ", "")
    reader = csv.reader(data.splitlines(), delimiter=',')
    header = next(reader)    
    return reader


def test_module():
    """
    Function loops through each row of csvread returned from get_csvFile()
    Each row read is a list
    The list is then passed to function in t1mod1.py to output what each index item is
    t1mod1.py will then return a code to specify what door opens, or both, or error
    The return code is checked with the function check_code(code)
    This function then outputs the result of that return code
    """
    index = 1
    for row in read_csvFile():
        if row[9] in ['P', 'N', 'D', '1', '2', '3', 'R']:
            print("Reading Record", str(index)+":")
            index += 1
            check_code(t1mod1.get_code(row))
        else:
            print("Reading Record X:")
            check_code(t1mod1.get_code(row))
        print()


# Main function
def main():
    """
    Check to see that no args are passed
    If no args are passed call test_module() function
    Else call help function
    """
    if(len(sys.argv) == 1):
        #do stuff
        test_module()
    else:
        help()
        exit(1)
    

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
