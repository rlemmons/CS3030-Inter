#!/usr/bin/env python3
import sys

def get_code(codeList):
    """
    Checks that the left door and/or right door can open
    Also initially checks that the car is in a valid gear
    Return:
        3   - both doors open
        2   - right door opens
        1   - left door opens
        0   - both doors are locked
        -1  - invalid gear
    """
    # Print the states of each item in the code list
    print_states(codeList)

    # Check if left and/or right door open
    left = left_open(codeList)
    right = right_open(codeList)
    if(valid_gear(codeList)):       # if invalid gear return -1
        if(left and right):
            return 3
        elif(right and not left):
            return 2
        elif(left and not right):
            return 1
        else:
            return 0
    else:
        return -1


def print_states(codeList):
    """
    Prints the states of the various values of the control software
    """
    i = 0;
    for val in codeList:
        if(i == 1):
            print("Left dashboard switch (0 or 1):", val)
        elif(i == 2):
            print("Right dashboard switch (0 or 1):", val)
        elif(i == 3):
            print("Child lock switch (0 or 1):", val)
        elif(i == 4):
            print("Master unlock switch (0 or 1):", val)
        elif(i == 5):
            print("Left inside handle (0 or 1):", val)
        elif(i == 6):
            print("Left outside handle (0 or 1):", val)
        elif(i == 7):
            print("Right inside handle (0 or 1):", val)
        elif(i == 8):
            print("Right outside handle (0 or 1):", val)
        elif(i == 9):
            print("Gear shift positions (P, N, D, 1, 2, 3, R):", val)
        else:
            pass
        i += 1

def left_open(codeList):
    """
    Return:
        True    - left door opens
        False   - left door locked
    """
    return True

def right_open(codeList):
    """
    Return:
        True    - right door opens
        False   - left door locked
    """
    return True

def valid_gear(codeList):
    """
    Function checks if gear is valid to increase get_code() function performance
    Return:
        True    - valid gear
        False   - invalid gear
    """
    if codeList[9] in ['P', 'N', 'D', 'R', '1', '2', '3']:
        return True
    else:
        return False


# Main function
def main():
    """
    Test Function.
    """
    

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
