"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

for word in some_words:
    # This will print the words in some_words line by line. #
    print(word)

for x in some_words:
    # this will print the words in some_words line by line. #
    print(x)

print(some_words)
# this will print all the words in some_words in a bracket. #

if len(some_words) > 3:
    # i think the function will be printed and > will show. #
    print('some_words contains more than 3 words')

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # i think the function will print system, node, release, version, machine and processor in round brackets 
    print(platform.uname())

usefulFunction()
