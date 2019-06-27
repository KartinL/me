# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 0
    guess = 0

    # first = 0
    # last = len(int(high)-1
    # found = False:

    # while first<=last and not found:
    #     midpoint = (first + last)//2
    #     if actual_number == range(low, high)[midpoint]:        
    #         found =  True 
    #     else:
    #         if actual_number < range(low, high)[midpoint]:
    #             last = midpoint-1
    #         else:
    #             if actual_number > midpoint:
    #                 first = midpoint+1  

    while True:
        x = (low + high)/2
        tries = tries + 1 
        if (int(x) == actual_number): 
            guess = int(x)
            break
        elif (math.ceil(x) == actual_number):  
            guess = math.ceil(x)
            break              
        elif (x < actual_number):
            low = math.ceil(x)
        elif (x > actual_number):
            high = int(x)
    
    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(0, 100, 76))
    print(binary_search(0, 100, 26))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
