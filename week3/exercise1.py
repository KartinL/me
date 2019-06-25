# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""

# cd me if youre not in the me folder 
# python3 ../course/week3/tests.py

def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range()
    Then look up the docs for range(), you can answer this with just the range 
    function, but we'd like you to do it the long way, probably using a loop.
    """

    # count = 0
    # while start <= stop:     
    #     start = count - 1 
    # answer = count 
    # return answer 

    i = []
    while start < stop:
        i.append(start)
        start = start + step 
    else:
        return i 

def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """

    answer = []

    for i in range(start, stop, step):

        answer.append(i)

    return answer


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    
    # answer = []
    
    # for i in range(start, stop, 2):
    #     answer.append(i)

    print(start, stop)
    return list(range(start, stop, 2))


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    """

    for i in range(low, high): 

        print(i)

    if low < i < high:

        print ("true")

    else:

        print ("false")

    answer = i

    return answer 

    # n = input(0)
    # n = int(n)
    # if n < 0:
    #     print("yes")
    # else:
    #     print("no")


    # print(low, high)

    # answer = 35

    # return answer 

    # # return range(low,high)


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """

    message = 5

    for i in str(message):

        print (i)

    answer = 5

    return answer 

    # for i in int(message):

    #     print str(i)
     
    # while True:
    #     try:
    #         x = int(raw_input('Enter your number: '))
    #     except ValueError:
    #         print 'That is not a number! Try again!'
    #     if x in [1, 2]:
    #         break
    
    # return


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """

    answer = [int]

    for i in range(low, high):

        if low < i < high:

            print("true")

        else:

            print("false")

    return answer 


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
